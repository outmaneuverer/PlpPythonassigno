class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")
    
    def send_message(self, number, message):
        print(f"Message to {number}: {message}")
    
    def phone_info(self):
        return f"{self.brand} {self.model}, Price: ${self.price}"


# Subclass (Inheritance)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, price, gpu):
        #  parent constructor
        super().__init__(brand, model, price)
        self.gpu = gpu
    
    # Polymorphism: phone_info()
    def phone_info(self):
        return f"{self.brand} {self.model} (Gaming Edition, GPU: {self.gpu}), Price: ${self.price}"
    
    def play_game(self, game):
        print(f"Playing {game} on {self.brand} {self.model} with {self.gpu} GPU 🚀")
        

phone1 = Smartphone("Samsung", "Galaxy S22", 800)
print(phone1.phone_info())
phone1.call("0722334455")
phone1.send_message("0722334455", "Hello!")

gaming_phone = GamingPhone("Asus", "ROG Phone 6", 1200, "Adreno 730")
print(gaming_phone.phone_info())
gaming_phone.play_game("PUBG Mobile")
