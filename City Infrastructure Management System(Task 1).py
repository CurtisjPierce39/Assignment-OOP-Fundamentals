#Question 1 Task 1

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.reg_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner

    def display_owners(self):
        print(f"Registration #: {self.reg_number}, Type: {self.type}, Owner: {self.owner}")

vehicles = {}

def register_vehicles(reg_num, type, owner):
    if reg_num in vehicles:
        print("Error!! Please try again!")
        return
    vehicles[reg_num] = Vehicle(reg_num, type, owner)
    print(f"Vehicle '{reg_num}' now fully registered.")

def update_owner(reg_num, new_owner):
    if reg_num in vehicles:
        vehicles[reg_num].update_owner(new_owner)
        print(f"Registration number '{reg_num}' has a new owner!")
    else:
        print("No vehicle by that registration number.")

def display_all_vehicles():
    if not vehicles:
        print("No vehicles to display!")
    for vehicle in vehicles.values():
        vehicle.display_owners()

while True:
    print("1. Register Vehicle \n2. Update Owner \n3. Display All Vehicles \n4. Quit")
    choice = input("Please select an option: ")
    try:
        if choice == '1':
            reg_num = input("Please enter registration number: ")
            type = input("Please enter vehicle type: ")
            owner = input("Please enter owner name: ")
            register_vehicles(reg_num, type, owner)
        elif choice == '2':
            reg_num = input("Please enter registration number: ")
            new_owner = input("Please enter new owner name: ")
            update_owner(reg_num, new_owner)
        elif choice == '3':
            display_all_vehicles()
        elif choice == '4':
            print("Thank you. Come Again!")
            break
    except Exception as e:
        print(f"An error has occurred: {e}")