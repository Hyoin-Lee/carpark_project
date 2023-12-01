from sensor import Sensor
from display import Display
from pathlib import Path
from datetime import datetime
# import json


class CarPark:
    def __init__(self,
                 location,
                 capacity,
                 log_file='log.txt',
                 plates=None,
                 sensors=None,
                 displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []
        # convert file name to path and create it
        self.log_file = Path(log_file)
        if not self.log_file.exists():
            self.log_file.touch()

    @property
    def available_bays(self):
        # car_park.available_bays
        return max(0, self.capacity - len(self.plates))

    def __str__(self):
        return f'Welcome to {self.location} car park'

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be Sensor or Display")

        if isinstance(component, Sensor):
            self.sensors.append(component)

        elif isinstance(component, Display):
            self.displays.append(component)

    def _log_car(self, action, plate):
        with self.log_file.open(mode='a') as file:
            file.write(f'{plate} {action} on the {datetime.now().strftime("%d-%m %H:%M")}\n')

    def add_car(self, plate):
        self.plates.append(plate)
        self._log_car("entered", plate)
        # print (f"Car with plate '{plate}' registered n the car park.")
        # self.update_displays()

    def remove_car(self, plate):
        if plate in self.plates:
            self.plates.remove(plate)
            self._log_car("exited", plate)
            # print(f"Car with plate '{plate}' removed from the car park.")
            # self.update_displays()
        # else:
        #    raise ValueError("This car has not been registered in this car park")

    def update_displays(self):
        for display in self.displays:
            display.update({"Bays": self.available_bays,
                            "Temperature": 42}
                           )
            print(f"Updating: {display}")
