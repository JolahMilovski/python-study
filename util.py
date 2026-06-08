import functools
import time
from typing import Callable, Any



#Декоратор времени выполнения функции
def async_timed():
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f"выполняется {func} с фргументами {args} {kwargs}")
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f"ФУНКЦИЯ {func} завершилась за {total:.2f} c")
        return wrapped
    return wrapper

