from ..exo2.command import Command


def test_command_add_item():
    command = Command(user_email="toto@mail.com")

    command.add_item("tshirt", 15)

    assert command.items == ["tshirt"]
    assert command.price == 15

    command.add_item("shoes", 40)

    assert command.items == ["tshirt", "shoes"]
    assert command.price == 55


def test_command_send(mocker, capfd):
    command = Command("toto@mail.com")
    command.add_item("jewelry", 125)

    email_service = mocker.Mock()

    command.send(email_service)

    email_service.send.assert_called_once_with(
        coupon="5%", email="toto@mail.com")
    assert email_service.send.call_count == 1
    assert email_service.send.call_args.kwargs == {
        "coupon": "5%",
        "email": "toto@mail.com"
    }

    out, _ = capfd.readouterr()
    assert out == f"Command sent for 125 euros.\n"
