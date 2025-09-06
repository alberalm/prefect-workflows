from prefect import flow
from prefect.client.schemas.schedules import CronSchedule


if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/alberalm/prefect-workflows.git",
        entrypoint="keep_database_on.py:query_biosenda_database"
    ).deploy(
        name="keep-db-on",
        schedule=CronSchedule(
            cron="0 3 * * *",
            timezone="Europe/Madrid",
        ),
        work_pool_name="default",
        work_queue_name="default",
        push=False,
    )