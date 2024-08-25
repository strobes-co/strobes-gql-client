from setuptools import find_packages, setup

with open('./requirements.txt') as f:
    required = f.read().splitlines()

with open("README.md") as file:
    setup(
        name="Strobes Graphql Client",
        license="GPLv3",
        description="This is client that wraps strobes GrapqhQL.",
        long_description=file.read(),
        author="Akhil Reni",
        version=0.1,
        author_email="akhil@wesecureapp.com",
        url="https://strobes.co/",
        python_requires='>=3.6',
        install_requires=required,
        packages=find_packages(
            exclude=('test')),
        package_data={
            'strobes_gql_client': [
                '*.txt',
                '*.json']},
        include_package_data=True)