from collections.abc import Iterator

from static_error_handler import Err, Ok, Result, collect_results, process_results


def test_process_results_all_ok() -> None:
    items: list[Result[int, str]] = [Ok(1), Ok(2), Ok(3)]

    out = process_results(items, lambda xs: sum(xs))

    assert out.is_ok()
    assert out.unwrap() == 6


def test_process_results_stops_on_first_err_and_returns_err() -> None:
    callback_called = False

    def items() -> Iterator[Result[int, str]]:
        yield Ok(1)
        yield Err("boom")
        raise AssertionError("iteration continued past the first Err")

    def consume(xs: list[int]) -> tuple[int, ...]:
        nonlocal callback_called
        callback_called = True
        return tuple(xs)

    out = process_results(items(), consume)

    assert out.is_err()
    assert out.unwrap_err() == "boom"
    assert callback_called is False


def test_process_results_checks_for_errors_before_calling_func() -> None:
    items: list[Result[int, str]] = [Ok(1), Err("boom")]

    out = process_results(items, lambda _: 0)

    assert out.is_err()
    assert out.unwrap_err() == "boom"


def test_process_results_empty_iterable() -> None:
    items: list[Result[int, str]] = []
    out = process_results(items, list)

    assert out.is_ok()
    assert out.unwrap() == []


def test_collect_results_all_ok() -> None:
    items: list[Result[int, str]] = [Ok(1), Ok(2), Ok(3)]

    out = collect_results(items)

    assert out.is_ok()
    assert out.unwrap() == [1, 2, 3]


def test_collect_results_returns_first_err() -> None:
    items: list[Result[int, str]] = [Ok(1), Err("first"), Err("second")]

    out = collect_results(items)

    assert out.is_err()
    assert out.unwrap_err() == "first"


def test_collect_results_empty_iterable() -> None:
    items: list[Result[int, str]] = []

    out = collect_results(items)

    assert out.is_ok()
    assert out.unwrap() == []
