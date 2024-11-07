import calendar
import locale
from typing import Callable, List


def short_form(func: Callable) -> Callable:
    """
    Decorator that shortens day names to their standard three-letter abbreviations.
    Example: 'Monday' -> 'Mon'
    """

    def wrapper() -> List[str]:
        days_full_to_short = dict(zip(calendar.day_name, calendar.day_abbr))
        data = func()
        return [days_full_to_short.get(day, day) for day in data]

    return wrapper


def translate(language: str) -> Callable:
    """
    Decorator that translates the names of the days of the week to the specified language.
    The 'language' parameter should be a valid locale string, such as 'de_DE.utf8' for German.
    """

    def decorator(func: Callable) -> Callable:
        def wrapper() -> List[str]:
            original_locale = locale.getlocale(locale.LC_TIME)
            try:
                locale.setlocale(locale.LC_TIME, language)
                return func()
            except locale.Error:
                print(f"Locale {language} is not supported.")
                return func()
            finally:
                locale.setlocale(locale.LC_TIME, original_locale)

        return wrapper

    return decorator


@translate("de_DE.utf8")
@short_form
def get_data() -> List[str]:
    """Returns the full names of the days of the week."""
    return list(calendar.day_name)
