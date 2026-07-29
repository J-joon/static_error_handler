from collections.abc import Callable, Iterable

from .static_error_handler import Err, Ok, Result


def collect_results[T, E](iterable: Iterable[Result[T, E]]) -> Result[list[T], E]:
    """Collect Ok values, stopping at and returning the first Err."""
    values: list[T] = []
    for item in iterable:
        if item.is_err():
            return Err(item.unwrap_err())
        values.append(item.unwrap())
    return Ok(values)


def process_results[T, E, R](
    iterable: Iterable[Result[T, E]], func: Callable[[list[T]], R]
) -> Result[R, E]:
    """
    Collect Ok values and transform them only when every item is Ok.

    The iterable is consumed eagerly up to the first Err. The callback is never
    called when an Err is present.
    """
    return collect_results(iterable).map(func)


__all__ = ["collect_results", "process_results"]
