class JWTRequired(Exception):
    def __str__(self):
        return "JWT is require."


class EmailException(Exception):
    def __str__(self):
        return "Username is required."


class PasswordException(Exception):
    def __str__(self):
        return "Password is required."


class LoginFailure(Exception):
    def __str__(self):
        return "Failed to login."


class GraphQLRequestError(Exception):
    """Raised when a GraphQL request comes back with `errors`.

    sgqlc's RequestsEndpoint doesn't raise on a gateway timeout or a 5xx —
    it converts them into `{"data": None, "errors": [...]}` and returns
    that like any other response. Without this check, `execute_query` /
    `execute_mutation` treated that as success, so a batch that hit a
    gateway timeout partway through a paginated export (e.g. `all_bugs` at
    page_size=500) came back as an empty/partial page instead of a
    failure, and callers had no way to tell "done" from "the request
    failed silently".
    """

    def __init__(self, operation_name, errors):
        self.operation_name = operation_name
        self.errors = errors
        super().__init__(f"{operation_name} returned GraphQL errors: {errors}")