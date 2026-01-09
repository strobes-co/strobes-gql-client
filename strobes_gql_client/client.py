import logging
from strobes_gql_client.base_client import BaseClient
from sgqlc.endpoint.requests import RequestsEndpoint
from sgqlc.operation import Operation
from strobes_gql_client import schema
import requests


class StrobesGQLClient(BaseClient):
    def __init__(self, host, api_token, verify=True):
        super().__init__(host=host, api_token=api_token)
        self.logger = logging.getLogger(self.__class__.__name__)
        session = requests.Session()
        session.verify = verify
        self.graphql_url = f"{self.app_url}api/graphql/"
        self.endpoint = RequestsEndpoint(
            self.graphql_url, self.headers, session=session
        )

    def execute_query(self, query_name, **variables):
        try:
            op = Operation(schema.Query)
            query = getattr(op, query_name)
            result = query(**variables)

            # NOTE:
            # Your backend error:
            #   "Field Bug.connector cannot be both deferred and traversed using select_related at the same time."
            # is typically raised by Django ORM when a queryset contains BOTH:
            #   - select_related('connector')
            #   - defer('connector') / only(...) that implicitly defers it
            #
            # GraphQL optimizers (graphene-django-optimizer / custom get_queryset) commonly
            # defer relations that are NOT requested in the GraphQL selection set.
            #
            # Workaround on the client: explicitly request a minimal connector selection
            # for allBugs so the backend won't "defer" it.
            if query_name == "all_bugs":
                # Pagination/meta fields
                result.has_next()
                result.has_previous()
                result.last_cursor()
                result.before_cursor()

                # Minimal, stable bug fields used by examples + a minimal connector selection
                result.objects.__fields__(
                    "id",
                    "title",
                    "severity",
                    "state",
                    "cvss",
                    "created",
                    "updated",
                )
                result.objects.connector.__fields__("id", "name", "slug")

            data = self.endpoint(op)
            if data:
                self.logger.debug(f"{query_name} executed successfully.")
                return data
            else:
                self.logger.error(
                    f"No data returned for {query_name} or an error occurred."
                )
                return None
        except AttributeError:
            self.logger.error(f"Query '{query_name}' not found in schema.")
            raise
        except Exception as e:
            self.logger.exception(
                f"An error occurred while executing {query_name}: {str(e)}"
            )
            raise

    def execute_mutation(self, mutation_name, **variables):
        try:
            op = Operation(schema.Mutation)
            mutation = getattr(op, mutation_name)
            mutation(**variables)
            data = self.endpoint(op)
            if data:
                self.logger.debug(f"{mutation_name} executed successfully.")
                return data.get(mutation_name)
            else:
                self.logger.error(
                    f"No data returned for {mutation_name} or an error occurred."
                )
                return None
        except AttributeError:
            self.logger.error(f"Mutation '{mutation_name}' not found in schema.")
            raise
        except Exception as e:
            self.logger.exception(
                f"An error occurred while executing {mutation_name}: {str(e)}"
            )
            raise
