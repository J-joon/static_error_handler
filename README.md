# static_error_handler

A minimal Python adaptation of Rust's `Result` type. Provides `Ok` and `Err`
classes with helper methods for error handling.

Requires Python 3.12 or later.

## Installation

Install the library from PyPI:

```bash
pip install static_error_handler
```

## Usage

```python
from static_error_handler import Err, Ok, Result


def divide(a: int, b: int) -> Result[int, str]:
    if b == 0:
        return Err("division by zero")
    return Ok(a // b)


result = divide(10, 2)
print(result.unwrap())  # 5
```

Collect several results, returning the first error without calling the
transformation:

```python
from static_error_handler import Err, Ok, Result, process_results

values: list[Result[int, str]] = [Ok(1), Ok(2), Ok(3)]
result = process_results(values, sum)
print(result.unwrap())  # 6

invalid_values: list[Result[int, str]] = [Ok(1), Err("invalid")]
failed = process_results(invalid_values, sum)
print(failed.unwrap_err())  # invalid
```
