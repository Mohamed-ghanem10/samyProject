class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self._fuelRate = 100
        self._velocity = 0
        self.fuelRate = fuelRate  # invokes the setter
        self.velocity = velocity  # invokes the setter

    @property
    def fuelRate(self):
        return self._fuelRate

    @fuelRate.setter
    def fuelRate(self, value):
        self._fuelRate = max(0, min(value, 100))

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        self._velocity = max(0, min(value, 200))

    def run(self, velocity, distance):
        self.velocity = velocity
        fuel_needed = (distance / 10) * 10  # 10% per 10 km
        if self.fuelRate >= fuel_needed:
            self.fuelRate -= fuel_needed
            self.stop(0)
        else:
            distance_covered = (self.fuelRate / 10) * 10  # km
            self.fuelRate = 0
            remaining = distance - distance_covered
            self.stop(remaining)

    def stop(self, remaining_distance):
        self.velocity = 0
        if remaining_distance > 0:
            print(f"Car stopped before arriving. Remaining distance: {remaining_distance} km")
        else:
            print("Car arrived at destination.")
