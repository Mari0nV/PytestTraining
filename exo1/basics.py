from typing import List


def multiply_by_two(number: int) -> int:
    return number * 2


def format_response(status: int, message: str = None, error: str = None) -> bool:
    if status in [404, 500]:
        return {
            "status": status,
            "error": error
        }
    else:
        return {
            "status": status,
            "message": message
        }


def check_word_in_list(word: str, word_list: List[str]):
    if word_list == []:
        raise Exception("Word list should not be empty")

    if word in word_list:
        return True
    return False
