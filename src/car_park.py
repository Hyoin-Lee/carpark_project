from sensor import Sensor
from display import Display

class CarPark:
    def __init__(self,
                 location='Moondalup',
                 capacity=100,
                 plates=None,
                 sensors=None,
                 displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []

    def __str__(self):
        return f'Welcome to {self.location} car park'

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be Sensor or Display")

        if isinstance(component, Sensor):
            self.sensors.append(component)

        elif isinstance(component, Display):
            self.displays.append(component)


    def add_car(self, plate):
        self.plates.append(plate)
        self.update_display()

    def remove_car(self, plate):
        if plate in self.plates:
            self.plates.remove(plate)
            self.update_display()

    def update_displays(self):
        data = {"available_bays": self.available_bays, "temperatrue": 25}



    @property
    def available_bays(self):
        if len(self.plates) >= self.capacity:
            return 0
        return self.capacity - len(self.plates)