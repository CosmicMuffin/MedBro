import calendar
import sqlite3
from datetime import datetime
import funcs


funcs.cursor.execute("""
CREATE TABLE IF NOT EXISTS appointments (
	type text,
	year integer,
	month integer,
	date integer,
	avenue text
);
""")



posible_entries = ['appmonth', 'appyear', 'addapp', 'closeapp', 'upcmng']


while(True):
    usr_input_1 = str(input("""
    Enter one of the following:
    addperson --> Keep track of One's Medical Data
    fittrack --> Fitness Tracker
    appmonth --> Appointments this month
    appyr --> Appointments this year
    addapp --> New Appointment
    upcmng --> Upcoming Appointments
    closeapp ---> Close MedBro
    """))

    if usr_input_1 == 'appmonth':
        funcs.print_appointments_this_month()
    elif usr_input_1 == 'appyr':
        funcs.print_appointments_this_year()
    elif usr_input_1 == 'addapp':
        funcs.add_appointment()
    elif usr_input_1 == 'upcmng':
        funcs.upcoming_appointments()
    elif usr_input_1 == 'closeapp':
        break
    elif usr_input_1 == 'sabotage':
        print('You have ben SHANKARsabotaged.exe')
    elif usr_input_1 == 'fittrack':
        funcs.fitness_tracker()
    elif usr_input_1 == 'addperson':
        funcs.add_person()
    else:
        print('That is not a command')
        # while usr_input_1 not in posible_entries:
        #     usr_input_1 = str(input('Enter one of the given values'))
        #     if usr_input_1 == 'appmonth':
        #         print("Appointments in this month")
        #     elif usr_input_1 == 'appyr':
        #         print('Appointments in this year')
        #     elif usr_input_1 == 'addapp':
        #         newtype = str(input('What type of doctor will you be visiting?'))
        #         newdate = input('Date on which you visit the doctor?(dd)')
        #         newmonth = str(input('In which month will you be visiting the doctor?(Name of month)'))
        #         newyear = input('Which year will you be visiting the doctor?(yyyy)')
        #         newavenue = str(input('Name of the Hospital/CLinic?'))
        #
        #         apnew = funcs.appointment(newtype, newdate, newmonth, newyear, newavenue)
        #         funcs.med_appointments.append(apnew)











