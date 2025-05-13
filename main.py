import asyncio
from src.tasks import start_worker


def run_tasks():
    try:
        asyncio.run(start_worker())
    except KeyboardInterrupt:
        return


if __name__ == '__main__':
    run_tasks()
