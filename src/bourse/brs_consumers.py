import requests
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import sync_to_async
import asyncio


class Watch:
    def __init__(self):
        self.task: asyncio.Task = None
        self.future: list[asyncio.Future] = []

    def start(self):
        if self.task:
            return
        self.task = asyncio.create_task(self.get_price_loop())

    async def get_price_loop(self):
        while True:
            await self.get_price()
            await asyncio.sleep(15)

    async def get_price(self):
        url = 'https://sourcearena.ir/api/?token={}&market=market_bourse'
        my_token = '50bdfd94ca6de1102156676eb400d539'
        result = await sync_to_async(requests.get)(url.format(my_token))
        get_data = result.json()
        coins_list = get_data.get('bourse')
        price = coins_list

        for future in self.future:
            if future.cancelled():
                continue
            future.set_result(price)
        self.future.clear()

    def add_future(self, future):
        self.future.append(future)


watch = Watch()


class WatchConsumers(AsyncJsonWebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.task = None

    async def connect(self):
        await self.accept()
        self.task = asyncio.create_task(self.send_price_info())

    async def send_price_info(self):
        watch.start()
        while True:
            future = asyncio.Future()
            watch.add_future(future)
            price = await future
            await self.send_json({"price": price})

    async def disconnect(self, code):
        self.task.cancel()
