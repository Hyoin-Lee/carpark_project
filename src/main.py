from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display



# TODO Create a car park object with the location Moondalup, capacity 100, and log_file "moondalup.txt"
car_park = CarPark(location="Moondalup", capacity=100, log_file="moondalup.txt")

# TODO Create an entry sensor object with ID 1, is_active True, and linked to the car park
entry_sensor = EntrySensor(id=1, is_active=True, car_park=car_park)

# TODO Create an exit sensor object with ID 2, is_active True, and linked to the car park
exit_sensor = ExitSensor(id=2, is_active=True, car_park=car_park)

# TODO Create a display object with ID 1, message "Welcome to Moondalup", is_on True, and linked to the car park
display = Display(id=1, message="Welcome to Moondalup", is_on=True, car_park=car_park)

# TODO Drive 10 cars into the car park using the entry sensor
for _ in range(10):
    entry_sensor.detect_vehicle()

# TODO Drive 2 cars out of the car park using the exit sensor
for _ in range(2):
    exit_sensor.detect_vehicle()


car_park.write_config()
car_park.from_config()
