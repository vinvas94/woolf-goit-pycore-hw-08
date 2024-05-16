from collections import UserDict
from datetime import datetime,timedelta
import pickle

class AddressBook(UserDict):
    def __init__(self):
        self.data = {}

    def add_record(self,record):
           self.data[record.name.value] = record
          
    def find(self,name):
        return self.data.get(name)
    
    def delete(self,name):
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self):
        upcoming_birthdays = []
        today = datetime.today()
        next_week = today + timedelta(days=7)
        current_year=today.year
        for record in self.data.values():
            try:
                birthday_this_year = record.birthday.value.replace(year=current_year)
            except AttributeError:
                continue
            if today <= birthday_this_year <= next_week:
                upcoming_birthdays.append(record)
        if upcoming_birthdays:
            result = "\n".join([f"{record.name}: {record.birthday.value.strftime('%d.%m.%Y')} ({record.birthday.value.strftime('%A')}) - Birthday upcoming🎉" for record in upcoming_birthdays])
            return result
        else:
            return "No upcoming birthdays.🙃"
    
    @staticmethod
    def save_data(book, filename="addressbook.pkl"):
        with open(filename, "wb") as f:
            pickle.dump(book, f)

    @staticmethod
    def load_data(filename="addressbook.pkl"):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return AddressBook() 