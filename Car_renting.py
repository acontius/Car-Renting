#Mohammad Amin Shahabi
#Computer Scince 1401
#40111262114

print("Hello Babe")

class Car:
    def __init__(self, name, price, seats, quantity):
        self.name = name
        self.price = price
        self.seats = seats
        self.quantity = quantity

car_list = [
    Car("Ford Fiesta", 120, 4, 8),
    Car("Mazda2", 100, 4, 10),
    Car("Audi A4", 200, 4, 3),
    Car("Lexus Ls", 210, 5, 4),
    Car("Cadillac CTS", 260, 4, 3),
    Car("Porsche 911", 400, 2, 2),
    Car("BMW Z4", 300, 2, 5),
    Car("Mazda CX-3", 120, 5, 12),
    Car("Hyundai SANTA FE", 120, 5, 10),
    Car("Toyota Camary", 100, 4, 10),
    Car("Amir abas almasi",0,5,1)
]

invoice_list = []

class Menu:
    def __init__(self):
        self.run_menu()

    def run_menu(self):
        while True:
            print("MENU")
            print("1 - Car List")
            print("2 - Check Your Invoice")
            print("3 - Admin Panel")
            print("4 - Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.show_car_list()
            elif choice == "2":
                self.show_invoice()
            elif choice == "3":
                self.admin_panel()
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")

    def show_car_list(self):
        print("------------------------------------------------------------------")
        print("Item Name          | Price   | Seat   | Quantity")
        print("------------------------------------------------------------------")

        for i, car in enumerate(car_list):
            print(f"{i+1} | {car.name:<17} | {car.price:<7} | {car.seats:<6} | {car.quantity}")

        car_choice = int(input("Select a car: ")) - 1

        if 0 <= car_choice < len(car_list):
            self.show_car_details(car_choice)
            cont = input("Do you want to order another car? (1-Yes, 2-No): ")

            if cont == "1":
                self.add_car_to_invoice(car_choice)
            elif cont == "2":
                self.run_menu()
            else:
                print("Invalid choice. Returning to main menu.")
        else:
            print("Invalid car choice. Returning to main menu.")

    def show_car_details(self, car_index):
        car = car_list[car_index]
        print(f"\nCar Details:")
        print(f"Name: {car.name}")
        print(f"Price: {car.price}$")
        print(f"Seats: {car.seats}")
        print(f"Quantity: {car.quantity}")

    def add_car_to_invoice(self, car_index):
        car = car_list[car_index]
        invoice_list.append(car)
        print("Car added to invoice.")

    def show_invoice(self):
        total_price = sum(car.price for car in invoice_list)
        print("\nYour Invoice:")
        for car in invoice_list:
            print(f"Name: {car.name}")
            print(f"Price: {car.price}$")
            print(f"Seats: {car.seats}")
            print(f"Quantity: {car.quantity}")
            print()

        print(f"Total Price: {total_price}$")
        input("Press Enter to return to the main menu.")

    def admin_panel(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username == "admin" and password == "admin":
            print("Login successful!\n")
            print("ADMIN PANEL")
            print("1 - Add/Edit Car")
            print("2 - Delete Car")
            print("3 - Exit")

            admin_choice = input("Enter your choice: ")

            if admin_choice == "1":
                self.add_edit_car()
            elif admin_choice == "2":
                self.delete_car()
            elif admin_choice == "3":
                self.run_menu()
            else:
                print("Invalid choice. Returning to main menu.")
        else:
            print("Login failed. Returning to main menu.")

    def add_edit_car(self):
        edit_choice = input("Add or Edit? ")

        if edit_choice.lower() == "add":
            new_car_name = input("Enter the new car name: ")
            new_car_price = int(input("Enter the new car price: "))
            new_car_seats = int(input("Enter the number of seats: "))
            new_car_quantity = int(input("Enter the quantity available: "))

            car_list.append(Car(new_car_name, new_car_price, new_car_seats, new_car_quantity))
            print("Car added successfully.")
        else:
            car_to_edit = int(input("Enter the car number to edit: ")) - 1

            if 0 <= car_to_edit < len(car_list):
                car = car_list[car_to_edit]
                print(f"Editing car: {car.name}")
                car.name = input("Enter the updated car name: ")
                car.price = int(input("Enter the updated car price: "))
                car.seats = int(input("Enter the updated number of seats: "))
                car.quantity = int(input("Enter the updated quantity available: "))
                print("Car edited successfully.")
            else:
                print("Invalid car number.")

        self.run_menu()

    def delete_car(self):
        car_to_remove = int(input("Enter the car number to delete: ")) - 1

        if 0 <= car_to_remove < len(car_list):
            car = car_list[car_to_remove]
            car_list.remove(car)
            print("Car deleted successfully.")
        else:
            print("Invalid car number.")

        self.run_menu()

Menu()
