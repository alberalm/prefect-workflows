from prefect import flow, task
from prefect.logging import get_run_logger
from prefect_sqlalchemy import SqlAlchemyConnector


@task
def count_species():
    database_block = SqlAlchemyConnector.load("biosenda-database")
    with database_block as engine:
        return len(engine.execute("""
        SELECT DISTINCT t.taxonid
        FROM Taxonomia t;
        """).fetchall())


@flow
def query_biosenda_database():
    logger = get_run_logger()
    n = count_species()
    logger.info(f"Species in database: {n}")
