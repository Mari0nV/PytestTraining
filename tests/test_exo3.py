import json


def test_that_game_status_is_similar_to_dictionary(game_status):
    assert game_status["place"] == "forest.north"
    assert game_status["alive"] == True
    assert game_status["day"] == 1
    assert len(game_status) == 3


def test_game_status_update(game_status):
    update = {
        "place": "forest.south",
        "alive": False,
        "duration": 2
    }

    game_status.update(update)

    assert game_status.status["place"] == "forest.south"
    assert game_status.status["previous_place"] == "forest.north"
    assert not game_status.status["alive"]
    assert game_status.status["day"] == 3


def test_game_status_player_is_dead(game_status):
    assert not game_status.is_dead()

    game_status.update({"alive": False})

    assert game_status.is_dead()


def test_game_status_save(game_status, generated_test_folder):
    game_status.save()

    with open(game_status.file_path, "r") as fd:
        content = json.load(fd)

    assert content == {
        "status": {
            "place": "forest.north",
            "day": 1,
            "alive": True
        }
    }
