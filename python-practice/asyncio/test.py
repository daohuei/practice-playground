import asyncio
import multiprocessing
import time


class SenderPipeline:
    def __init__(self, receiver_queue):
        self.receiver_queue = receiver_queue

    async def run(self):
        print("sender running")
        while True:
            await asyncio.sleep(5)
            self.receiver_queue.put_nowait("packet event")


class ReceiverPipeline:
    def __init__(self, name, pipeline_queue: asyncio.Queue = None):
        self.name = name
        self.queue = asyncio.Queue() if pipeline_queue is None else pipeline_queue

    async def run(self):
        print("receiver running")
        while True:
            event = await self.queue.get()
            print(event)


class Manager(multiprocessing.Process):
    def __init__(self):
        self.loop = None
        self.pipelines = []
        self.tasks = []
        self.initialize_pipelines()
        self.initialize_asyncio_tasks()
        print("init tasks and pipelines")
        super(Manager, self).__init__()

    def initialize_pipelines(self):
        self.loop = asyncio.get_event_loop()
        receiver_pipeline = ReceiverPipeline(name="Receiver")
        sender_pipeline = SenderPipeline(receiver_pipeline.queue)
        self.pipelines = [sender_pipeline, receiver_pipeline]

    def initialize_asyncio_tasks(self):
        self.tasks = list(
            map(lambda pipeline: asyncio.ensure_future(pipeline.run()), self.pipelines)
        )

    def run(self):
        self.loop.run_until_complete(
            asyncio.wait(self.tasks, return_when=asyncio.FIRST_COMPLETED)
        )
        print("manger closing")
        self.loop.close()


if __name__ == "__main__":
    manager = Manager()
    manager.start()