class Restaurant:
    
    def __init__ (self, restauran_name, cuisine_type):  
        self.restauran_name = restauran_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'{self.restauran_name}')
        print(f"{self.cuisine_type}")


    def open_restauran(self):
        print(f"{self.restauran_name} is open")


#Создаём три разных экземпляра
restaurants = {
    Restaurant("У Палыча", "Русская"),
    Restaurant("La Bella Italia", "Итальянская"),
    Restaurant("Sakura", "Японская")
}

for restauran in restaurants:
    restauran.describe_restaurant()

