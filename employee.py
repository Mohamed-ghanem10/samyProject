from person import Person

class Employee(Person):
    def __init__(self, name, money, mood, healthRate, emp_id, car, email, salary, distanceToWork):
        super().__init__(name, money, mood, healthRate)
        self.id = emp_id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        elif hours < 8:
            self.mood = "lazy"
        else:
            self.mood = "tired"

    def drive(self, distance):
        print(f"Driving for {distance} km...")
        self.car.run(self.car.velocity, distance)

    def refuel(self, gasAmount=100):
        self.car.fuelRate += gasAmount
        print(f"Refueled. Current fuel rate: {self.car.fuelRate}%")

    def send_mail(self, to, subject, body):
        print(f"Sending mail to {to} with subject '{subject}' and body: {body}")

    # ✅ New method to check lateness
    def check_if_late(self, moveHour):
        travel_time = self.distanceToWork / self.car.velocity
        arrival_hour = moveHour + travel_time
        return arrival_hour
