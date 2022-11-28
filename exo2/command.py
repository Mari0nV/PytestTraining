class Command:
    """ Represents a command made on a shop online """

    def __init__(self, user_email: str):
        self.user_email = user_email
        self.items = []
        self.price = 0

    def add_item(self, item: str, price: float):
        """ Add item to list of items and update the total price """
        self.items.append(item)
        self.price += price

    def send(self, email_service):
        """ Send the command to the user and if the command is more than 100 euros, send a coupon to the user. """
        print(f"Command sent for {self.price} euros.")
        if self.price > 100:
            email_service.send(coupon="5%", email=self.user_email)
