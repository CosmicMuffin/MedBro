import calendar
from datetime import datetime
import sqlite3
some_text1 = '%B'
med_appointments = []
persons = []
days_in_month = (31,29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


connection = sqlite3.connect("medbrodata.db") #setting up database
cursor = connection.cursor()#setting up a cursor

class personData():
    def __init__(self, name, weight, height, sugarlvl, cholestlvl, rbc, wbc):
        self.name = name

        self.sugarlvl = sugarlvl
        self.cholestlvl = cholestlvl
        self.wbc = wbc
        self.rbc = rbc

        self.weight = weight
        self.height = height
        self.bmi = weight/(height*height)

    def preview_text(self):
        print(f'A person named {self.name} has been created with the data that you have entered.')



class appointment(): #object type for an appointment
    def __init__(self, type, date, month, year, avenue):
        self.type = type
        self.date = date
        self.month = month
        self.avenue = avenue
        self.year = year
        self.date_time = datetime.strptime(f'{self.date}/{month}/{self.year}', '%d/%m/%Y')


    def reminder_text(self): #text to be displayed for an appointment
        return(f"{self.type.title()} appointment at {self.avenue.title()} on {self.date}/{self.month}/{self.year}.")

    def upload_data(self):
        cursor.execute(f"""
        INSERT 
        """)


def appointments_this_month(): #appointments in the current month
    print('These are the medical appointments that you have in this month:')
    for appointment in med_appointments: #indexing the med_appointments list
        i = 1
        if appointment.year == datetime.now().year: # checking if an appointment belongs to the current month
            if appointment.month == datetime.now().month:
                print(f"{i}. {appointment.reminder_text()}")
                i = i + 1



def appointments_this_year(): #appointments in the current year
    print('These are the medical appointments that you have this year:')
    for appointment in med_appointments:
        i = 1
        if appointment.year == datetime.now().year:
            print(f"{i}. {appointment.reminder_text()}")
            i = i + 1


def upcoming_appointments(): #upcoming appointments
    print('These are some upcoming medical appointments:')
    for appointment in med_appointments:
        i = 1
        if datetime.now() <= appointment.date_time:
            print(f"{i}. {appointment.reminder_text()}")
            i = i + 1
        # this is not showing the appointments on the same date maybe datetime works with GST

def add_appointment(): #adding an appointment
    newtype = str(input('What type of doctor will you be visiting?'))
    newyear = int(input('Which year will you be visiting the doctor?(yyyy)'))
    while (True):
        newmonth = int(input('In which month will you be visiting the doctor?(mm)'))

        if newmonth < 1 or newmonth > 12: #range check
            print('Not in Range')
            continue
        break
    while (True):
        newdate = int(input('Date on which you visit the doctor?(dd)'))

        if newdate < 1 or (newdate > days_in_month[newmonth - 1] or (newmonth == 2 and (
                (newyear % 100 == 0 and newyear % 400 != 0) or (
                newyear % 100 != 0 and newyear % 4 != 0)) and newdate == 29)): #leap year check
            print('Not in Range')
            continue
        break

    newavenue = str(input('Name of the Hospital/CLinic?'))
    apnew = appointment(newtype, newdate, newmonth, newyear, newavenue)
    med_appointments.append(apnew)
    print(f"""Here is a preview of your appointment:
{apnew.reminder_text()}""")

def print_appointments_this_month():
    print(appointments_this_month())

def print_appointments_this_year():
    print(appointments_this_year())

def add_person(): #adds a person object
    print('Answer the following questions to create a person. If not avalaiable enter -.')
    new_name = input('What is the name of this person?')
    new_sugarlvl = float(input('What is the Sugar level? in mg/dL'))
    new_cholestlvl = float(input('What is the Cholesterol Level? bad cholesterol only... in mg/dL'))
    new_rbc = float(input('What is the Red Blood Corpuscles Count? in millions per milimeter cube'))
    new_wbc = float(input('What is the White Blood Corpuscles Count? in WBCs per microlitre'))
    new_height = float(input('What is the height in cm?'))/100
    new_weight = float(input('What is the weight in Kg?'))

    new_person = personData(new_name, new_weight, new_height, new_sugarlvl, new_cholestlvl, new_rbc, new_wbc)
    print(new_person.preview_text())
    persons.append(new_person)

# #fitness tracker:
# def fitness_tracker():
#
#     name_input = input(f"""
# Enter the name of a person whose profile has been created:
#
# """)