import json


class GameStatus:
    def __init__(self, status, file_path):
        self.status = status
        self.file_path = file_path

    def __getitem__(self, key):
        return self.status[key]

    def __len__(self):
        return len(self.status)

    def update(self, status_dict: dict):
        """
        Update one or multiple status.
        The parameter status_dict is a dictionary with the following format:
            { <category1>: <value1>, <category2>: <value2> }
        This function will update all status categories present in the parameter dictionary.
        Examples :
            { "place": "city" } will update the place the player is in and set the "previous_place" key with the place he was in before.
            { "duration": 2 } will update the day of the game by adding the value given.
            { "alive" : False } will update the living state of the player.
        """
        for category, value in status_dict.items():
            if category == "place":
                self.status["previous_place"] = self.status["place"]
                self.status["place"] = value
            elif category == "duration":
                self.status["day"] += value
            else:
                self.status[category] = value

    def is_dead(self):
        """
        Check whether the player is dead.
        """
        if not self.status["alive"]:
            return True
        return False

    def save(self):
        """ Save status in a json file, replacing the previous version. """
        with open(self.file_path, "w") as fd:
            json.dump({"status": self.status}, fd)
