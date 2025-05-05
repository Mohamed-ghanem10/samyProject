import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from car import Car
from employee import Employee
from office import Office

# GUI Window
class SamyProjectGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Samy Project GUI")
        self.root.geometry("600x550")
        
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Create office
        self.iti_office = Office("ITI")

        # Create employee Samy
        self.samy_car = Car("Fiat 128", fuelRate=80, velocity=60)
        self.samy = Employee(name="Samy", money=100, mood="neutral", healthRate=100,
                             emp_id=1, car=self.samy_car, email="samy@iti.com", salary=3000, distanceToWork=20)

        # Initialize UI elements
        self.init_ui()

    def init_ui(self):
        frame = ttk.Frame(self.root, padding=20)
        frame.pack(fill=tk.BOTH, expand=True)

        self.info_label = ttk.Label(frame, text="Samy Project", font=("Helvetica", 16))
        self.info_label.grid(row=0, column=0, columnspan=3, pady=10)

        self.hire_button = ttk.Button(frame, text="Hire Samy", command=self.hire_employee)
        self.hire_button.grid(row=1, column=0, padx=10, pady=10)

        self.list_button = ttk.Button(frame, text="List Employees", command=self.list_employees)
        self.list_button.grid(row=1, column=1, padx=10, pady=10)

        self.lateness_button = ttk.Button(frame, text="Check Lateness", command=self.check_lateness)
        self.lateness_button.grid(row=1, column=2, padx=10, pady=10)

        self.fire_button = ttk.Button(frame, text="Fire Samy", command=self.fire_employee)
        self.fire_button.grid(row=2, column=1, padx=10, pady=10)

        # Car Control Buttons
        self.drive_button = ttk.Button(frame, text="Drive Car", command=self.drive_car)
        self.drive_button.grid(row=5, column=0, padx=10, pady=5)

        self.refuel_button = ttk.Button(frame, text="Refuel Car", command=self.refuel_car)
        self.refuel_button.grid(row=5, column=1, padx=10, pady=5)

        self.stop_button = ttk.Button(frame, text="Stop Car", command=self.stop_car)
        self.stop_button.grid(row=5, column=2, padx=10, pady=5)

        self.update_button = ttk.Button(frame, text="Update Employees Count", command=self.update_employees_count)
        self.update_button.grid(row=3, column=0, columnspan=3, pady=10)

        self.scrollbar = ttk.Scrollbar(frame)
        self.scrollbar.grid(row=4, column=3, sticky="ns", pady=10)

        self.message_box = tk.Text(frame, height=10, width=60, wrap=tk.WORD, font=("Helvetica", 12))
        self.message_box.grid(row=4, column=0, columnspan=3, pady=10)
        self.message_box.config(state=tk.DISABLED)

        self.scrollbar.config(command=self.message_box.yview)
        self.message_box.config(yscrollcommand=self.scrollbar.set)

    def display_message(self, message):
        self.message_box.config(state=tk.NORMAL)
        self.message_box.insert(tk.END, message + "\n")
        self.message_box.config(state=tk.DISABLED)
        self.message_box.yview(tk.END)

    def hire_employee(self):
        self.iti_office.hire(self.samy)
        self.display_message(f"{self.samy.name} hired!")

    def list_employees(self):
        employees = self.iti_office.get_all_employees()
        employee_list = "\n".join([f"{emp.name}, ID: {emp.id}" for emp in employees])
        self.display_message(f"Employees:\n{employee_list if employee_list else 'No employees!'}")

    def check_lateness(self):
        arrival_hour = self.samy.check_if_late(moveHour=7.5)
        if arrival_hour <= 9:
            self.samy.salary += 10
            self.display_message(f"On time! Arrival hour: {arrival_hour} <= 9\nRewarded 10 to {self.samy.name}. New salary: {self.samy.salary}")
        else:
            self.display_message(f"Late! Arrival hour: {arrival_hour} > 9")

    def fire_employee(self):
        self.iti_office.fire(1)
        self.display_message(f"{self.samy.name} fired!")

    def update_employees_count(self):
        Office.change_emps_num(5)
        self.display_message("Total employees in all offices updated to 5.")

    def drive_car(self):
        try:
            distance = 10  # مثال: قيادة 10 كم
            self.samy.drive(distance)
            self.display_message(f"Samy drove {distance} km. Remaining fuel: {self.samy.car.fuelRate:.2f}%")
        except Exception as e:
            self.display_message(f"Error driving car: {e}")

    def refuel_car(self):
        try:
            self.samy.refuel(20)  # تزود بالوقود 20%
            self.display_message(f"Car refueled. Current fuel: {self.samy.car.fuelRate:.2f}%")
        except Exception as e:
            self.display_message(f"Error refueling car: {e}")

    def stop_car(self):
        try:
            remaining_distance = 0  # أو أي قيمة منطقية حسب السياق
            self.samy.car.stop(remaining_distance)
            self.display_message(f"Car has stopped. Remaining distance: {remaining_distance} km")
        except Exception as e:
            self.display_message(f"Error stopping car: {e}")
# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = SamyProjectGUI(root)
    root.mainloop()
