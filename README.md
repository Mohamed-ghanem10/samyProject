
This project applies Object-Oriented Programming concepts using Python by simulating a real-life scenario involving employees, offices, and cars.

✅ Implemented Classes:
Person

Attributes: name, money, mood, healthRate

Methods:

sleep(hours) – sets mood based on sleep hours

eat(meals) – sets health rate

buy(items) – reduces money per item

Employee (inherits from Person)

Attributes: id, car, email, salary, distanceToWork

Methods:

work(hours) – sets mood based on work hours

drive(distance) – initiates car run

refuel(gasAmount) – refuels the car

send_mail() – (not fully detailed)

Car

Attributes: name, fuelRate, velocity

Methods:

run(velocity, distance) – reduces fuel, changes speed

stop() – sets velocity to 0 and prints status

Constraints:

Velocity: 0–200

Fuel rate: 0–100

Office

Attributes: name, employees

Methods:

hire(), fire(), get_employee(), get_all_employees()

deduct(), reward()

check_lateness(), calculate_lateness() (static)

Class variable: employeesNum

Class method: change_emps_num(num)

🛠 Scenario Overview:
Samy is an employee at ITI.

He drives 20 km daily to work with a Fiat 128.

He must arrive before 9:00 AM.

Fuel decreases by 10% every 10 km.

"A GUI was added for some inputs using the Tkinter library, and the required task was executed."


