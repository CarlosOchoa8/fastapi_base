from os import getenv


def get_postgres_uri():
    host = getenv("POSTGRES_HOST")
    port = getenv("POSTGRES_PORT", 5432)
    password = getenv("POSTGRES_PASSWORD")
    user = getenv("POSTGRES_USER")
    db_name = getenv("POSTGRES_DB")
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
