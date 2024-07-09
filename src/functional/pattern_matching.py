from typing import Optional, Union

maybe_five: Optional[int]
maybe_five: Optional[int] = 5

maybe_seven: Union[int | None]
maybe_seven = 7


def option_pattern_match(maybe_number: Optional[int]) -> str:
    match maybe_number:
        case None:
            print(f"uh oh found nothing")
            return "returned None"
        case int() as number:
            print(f"yay found a number: {number}")
            return f"returned {number}"


if __name__ == "__main__":
    option_pattern_match(maybe_five)
    option_pattern_match(maybe_seven)

    maybe_five = None
    option_pattern_match(maybe_five)
