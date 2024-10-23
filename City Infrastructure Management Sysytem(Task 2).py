# Question 1 Task 2

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0
        
    def add_participant(self):
        self.participant_count += 1
        return self.participant_count

    def get_participant_count(self):
        return self.participant_count
    
    def display_count(self):
        print(f"Event: {self.name}, Date: {self.date}, Number of participants: {self.participant_count}")

first_event = Event("Toy Drive", "10-31-2002")
second_event = Event("Food Drive", "02-15-1986")

toy_drive = first_event.add_participant()
food_drive = second_event.add_participant()
food_drive = second_event.add_participant()

first_event.display_count()
second_event.display_count()