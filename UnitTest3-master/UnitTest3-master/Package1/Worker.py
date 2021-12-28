
import datetime
import requests


class Worker:
    """The Worker class holds information and methods about workers"""

    def __init__(self, fname, lname, byear, bmonth, bday, adr, country):
        self.first_name = fname
        self.last_name = lname
        self.birth_year = byear
        self.birth_month = bmonth
        self.birth_day = bday
        self.address = adr
        self.cntry = country

    def full_name(self):
        """Returns the full name of the worker"""
        return f'{self.first_name} {self.last_name}'

    def age(self):
        """Returns the age of the worker"""
        return f'{self.first_name} is {datetime.datetime.now().year - self.birth_year} years old'

    def days_to_birthday(self):
        """Returns the number of days until the next birthday"""
        now = datetime.date.today()
        if self.birth_month < int(now.month):
            new_year = int(now.year) + 1
            birthday_this_year = datetime.date(new_year, self.birth_month, self.birth_day)
        else:
            birthday_this_year = datetime.date(int(now.year), self.birth_month, self.birth_day)
        return str(birthday_this_year - now)

    def greet(self, other):
        return f'{self.first_name} says hello to {other.first_name}'

    # def location(self):
    #     """Returns the location coordinates of the worker's address"""
    #     param = self.address + ',' + self.cntry
    #     url = f'https://geocode.xyz/?locate={param} &json=Alon'
    #
    #     response = requests.get(url)
    #
    #     if response.ok:
    #         return response.text
    #     else:
    #         return 'Bad response!'
