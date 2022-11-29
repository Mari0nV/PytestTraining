import pytest

from ..exo1.basics import check_word_in_list, format_response, multiply_by_two, send_requests


@pytest.mark.parametrize("number, expected_result", [
    (0, 0),
    (2, 4),
    (101, 202)
])
def test_multiply_by_two(number, expected_result):
    assert multiply_by_two(number) == expected_result


@pytest.mark.parametrize("status, message, error, formatted_response", [
    (200, "success", None, {"status": 200, "message": "success"}),
    (500, None, "failure", {"status": 500, "error": "failure"})
])
def test_format_response(status: int, message: str, error, formatted_response):
    assert format_response(status=status, message=message,
                           error=error) == formatted_response


@pytest.mark.parametrize("word, word_list, expected_boolean", [
    ("cat", ["dog", "cat"], True),
    ("cat", ["dog", "fish"], False)
])
def test_check_word_in_list(word, word_list, expected_boolean):
    assert check_word_in_list(
        word=word, word_list=word_list) == expected_boolean


def test_check_word_in_list_fail():
    with pytest.raises(Exception):
        check_word_in_list("cat", [])


def test_send_requests(mocker):
    mock_send_requests = mocker.Mock()
    mocker.patch("requests.post", mock_send_requests)

    send_requests("test-url", 3, {"param": 1})

    assert mock_send_requests.call_count == 3

    # assert mock_send_requests.call_args.args == ("test-url/3",)
    assert mock_send_requests.call_args.kwargs == {"data": {"param": 1}}

    for i in range(3):
        assert mock_send_requests.call_args_list[i][0] == (f"test-url/{i+1}",)
