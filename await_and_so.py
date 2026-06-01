import asyncio
from asyncio import CancelledError

async def add_one(number: int) -> int:
    return number + 1

def sync_add_one(number: int) -> int:
    return number + 1

async def delay(delay_seconds: int) -> int:
    print(f'засыпаю на {delay_seconds} с')
    await asyncio.sleep(delay_seconds)
    print(f'сон в течение {delay_seconds} с закончился')
    return delay_seconds

async def hello_every_second():
    for i in range(2):
        print("sleep 3")
        await asyncio.sleep(3)
        print("пока я жду, исполняется другой код!")

async def main():    
    one_plus_one = sync_add_one(1)    
    print(one_plus_one)    
    print("sleep 2 sec")
    await asyncio.sleep(2)
    two_plus_one = await add_one(0)
    print(two_plus_one)

    sleep_for_tree = asyncio.create_task(delay(3))
    print(type(sleep_for_tree))
    result = await sleep_for_tree
    print(result)
    
    print("DELAY TASK")
    
    first_delay = asyncio.create_task(delay(3))
    second_delay = asyncio.create_task(delay(4))

    await hello_every_second()

    await first_delay
    await second_delay

    print("CancelledError")

    long_task = asyncio.create_task(delay(10))
    print("CancelledError with sleep 10")
    
    try:
        await asyncio.wait_for(long_task, timeout=5)
    except TimeoutError:
        print('Таймаут: задача не успела завершиться за 5 секунд')
        long_task.cancel()
        try:
            await long_task
        except CancelledError:
            print('Наша задача была снята после таймаута')

asyncio.run(main())