from .itertools import collect_results, process_results
from .static_error_handler import Err, Ok, PanicError, Result, panic

__version__ = "0.2.0"

__all__ = [
    "Err",
    "Ok",
    "PanicError",
    "Result",
    "__version__",
    "collect_results",
    "panic",
    "process_results",
]
