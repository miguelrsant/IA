import os
from database.connection import execute_query


def get_version():
    results = execute_query("SHOW server_version;")

    if results:
        return results[0][0]
    return None


def get_max_connections():
    results = execute_query("SHOW max_connections;")

    if results:
        return results[0][0]
    return None


def count_connections_to_maindb():
    db_name = os.getenv("POSTGRES_DB")

    query = """
        SELECT count(*)::int 
        FROM pg_stat_activity 
        WHERE datname = :datname;
    """

    params = {"datname": db_name}

    result = execute_query(query, params=params, fetch_results=True)

    return result[0][0] if result else 0
