class Office:
    employeesNum = 0  # Class variable

    def __init__(self, name):
        self.name = name
        self.employees = []

    def get_all_employees(self):
        return self.employees

    def get_employee(self, empId):
        for emp in self.employees:
            if emp.id == empId:
                return emp
        return None

    def hire(self, employee):
        self.employees.append(employee)
        Office.employeesNum += 1
        print(f"{employee.name} hired. Total employees: {Office.employeesNum}")

    def fire(self, empId):
        emp = self.get_employee(empId)
        if emp:
            self.employees.remove(emp)
            Office.employeesNum -= 1
            print(f"Employee {empId} fired. Total employees: {Office.employeesNum}")

    def deduct(self, empId, deduction):
        emp = self.get_employee(empId)
        if emp:
            emp.salary -= deduction
            print(f"Deducted {deduction} from {emp.name}. New salary: {emp.salary}")

    def reward(self, empId, reward):
        emp = self.get_employee(empId)
        if emp:
            emp.salary += reward
            print(f"Rewarded {reward} to {emp.name}. New salary: {emp.salary}")

    def check_lateness(self, empId, moveHour):
        emp = self.get_employee(empId)
        if not emp:
            print(f"Employee with ID {empId} not found.")
            return

        is_late = Office.calculate_lateness(targetHour=9, moveHour=moveHour,
                                            distance=emp.distanceToWork, velocity=emp.car.velocity)
        if is_late:
            self.deduct(empId, 10)
        else:
            self.reward(empId, 10)

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        travel_time = distance / velocity
        arrival_hour = moveHour + travel_time
        if arrival_hour > targetHour:
            print(f"Late! Arrival hour: {arrival_hour} > {targetHour}")
            return True
        print(f"On time! Arrival hour: {arrival_hour} <= {targetHour}")
        return False

    @staticmethod
    def change_emps_num(num):
        Office.employeesNum = num
        print(f"Total employees in all offices updated to: {Office.employeesNum}")
