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


first_owner = Vehicle("abc-123", "car", "Bob Belcher")
second_owner = Vehicle("def-456", "truck", "Linda Belcher")

first_owner.display_owners()
second_owner.display_owners()