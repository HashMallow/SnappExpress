import asyncio

class AsyncPool:
    def __init__(self, max_workers):
        self.max_workers = max_workers
        self.semaphore = asyncio.Semaphore(max_workers)
        self.tasks = []

    async def add_task(self, coro):
        async with self.semaphore:
            task = asyncio.create_task(coro)
            self.tasks.append(task)
            try:
                return await task
            finally:
                self.tasks.remove(task)

    async def map(self, func, args_list):
        return await asyncio.gather(*[self.add_task(func(arg)) for arg in args_list])

    async def wait_completion(self):
        if self.tasks:
            await asyncio.gather(*self.tasks)

# Test function
async def function(name):
    print(f"Processing {name}")
    await asyncio.sleep(1)  # Simulate some work
    print(f"Finished {name}")
    return name

async def main():
    pool = AsyncPool(100)
    results = await pool.map(function, range(1000))
    print("All tasks completed")
    print(f"Number of results: {len(results)}")

if __name__ == "__main__":
    asyncio.run(main())