import base64
import io
from concurrent.futures import ThreadPoolExecutor
import aio_pika
import asyncio
from aio_pika.patterns import Master
from config import RABBITMQ_URL, REQUEST_JOB_NAME, IMAGE_JOB_NAME
from src.schemas import ImageRequestSchema, ImageSchema
from src.service import generate_image


async def start_worker():
    connection = await aio_pika.robust_connection.connect_robust(RABBITMQ_URL, timeout=1800, heartbeat=10)
    executor = ThreadPoolExecutor(max_workers=1)

    async with connection:
        channel = await connection.channel()
        master = Master(channel)

        async def generate_image_worker(*, request: ImageRequestSchema) -> None:
            loop = asyncio.get_event_loop()
            image = await loop.run_in_executor(executor, generate_image, request.prompt)

            if not image:
                return
            buffered = io.BytesIO()
            image.save(buffered, format="PNG")
            img_bytes = buffered.getvalue()
            img_base64 = base64.b64encode(img_bytes).decode('utf-8')

            image = ImageSchema(id=request.id, img=img_base64)
            await channel.default_exchange.publish(
                aio_pika.Message(body=image.model_dump_json().encode()),
                routing_key=IMAGE_JOB_NAME
            )
            print('[x] Image sent')

        await master.create_worker(REQUEST_JOB_NAME, generate_image_worker)
        await asyncio.Future()
