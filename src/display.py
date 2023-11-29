class Display:
    def __init__(self, id, car_park, message="", is_on = False):
        self.id = id
        self.car_park = car_park
        self.message = message
        self.is_on = False


    def __str__(self):
        print(f"Display {id}: Welcome to the car park.")



    def update(self, data):
        for key, value in data.items():
            print(f"{key}: {value}")