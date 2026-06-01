import asyncio
import time
from typing import Callable, Any
import functools


#async def main():
#    start = time.time()
#
#    await asyncio.sleep(2)
#
#    end = time.time()
#
#    print(f"выспались {end - start}")
#
#asyncio.run(main())

def async_timer():
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f'выполняется {func}  аргументами  {args} {kwargs}')
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f'{func} завершилась за {total:.4f} с')
        return wrapped
    return wrapper 

@async_timer()
async def delay(delay_sec: int):
    print(f"sleep to {delay_sec}")
    await asyncio.sleep(delay_sec)
    print(f'wakeup after {delay_sec}')
    return delay_sec


print("=== Starting program ===")
@async_timer()
async def main():

    print("[MAIN] Creating tasks...")
    task_one = asyncio.create_task(delay(5))

    await asyncio.sleep(10)
    task_two = asyncio.create_task(delay(3))

    print("[MAIN] Waiting for tasks 1...")
    await task_one

    print("[MAIN] Waiting for tasks 2...")
    await task_two

    print("[MAIN] All tasks done")


asyncio.run(main())

print("=== Program finished ===")