from sensor import Sensor
from display import Display
from pathlib import Path
from datetime import datetime
import json


class CarPark:
    def __init__(self,
                 location,
                 capacity,
                 plates=None,
                 sensors=None,
                 displays=None,
                 log_file='log.txt'):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        # create the file if it doesn't exist:
        self.log_file.touch(exist_ok=True)

    def write_config(self):
        with open("config.json", "w") as f:  # TODO: use self.config_file; use Path; add optional parm to __init__
            json.dump({"location": self.location,
                       "capacity": self.capacity,
                       "log_file": str(self.log_file)}, f)

    @staticmethod
    def from_config(config_file=Path("config.json")):
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open() as f:
            config = json.load(f)
        return CarPark(config["location"], config["capacity"], log_file=config["log_file"])

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

    def _log_car_activity(self, action, plate):
        with self.log_file.open(mode='a') as file:
            file.write(f'{plate} {action} at {datetime.now() :%Y-%m"%d %H:%M:%S")}\n')

    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays()
        self._log_car_activity("entered", plate)

    def remove_car(self, plate):
        if plate in self.plates:
            self.plates.remove(plate)
            self._log_car_activity("exited", plate)

    def update_displays(self):
        for display in self.displays:
            display.update({"Bays": self.available_bays,
                            "Temperature": 42}
                           )
            print(f"Updating: {display}")
