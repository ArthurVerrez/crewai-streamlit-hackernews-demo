from functools import wraps
from typing import Callable, Any


def tool_wrapper(display_name: str):
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            print(
                f"[{display_name}] Calling {func.__name__} with args: {args} and kwargs: {kwargs}"
            )
            return func(*args, **kwargs)

        return wrapper

    return decorator
