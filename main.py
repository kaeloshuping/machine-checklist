import obtain_user_input
import data
import get_reading

user_input = input("Please input either the machine name or last 3 digits of Serial Number:\n").upper()
print(user_input)

if user_input not in data.printers["B&W"]:
    print("Invalid input. Please input last 3 digits of printer serial number or finishing equipment name!")
    user_input = input("Please input either the machine name or last 3 digits of Serial Number:\n").upper()
elif user_input not in data.printers["COLOUR"]:
    print("Invalid input. Please input last 3 digits of printer serial number or finishing equipment name!")
    user_input = input("Please input either the machine name or last 3 digits of Serial Number:\n").upper()
elif user_input not in data.finishing_equipment:
    print("Invalid input. Please input last 3 digits of printer serial number or finishing equipment name!")
    user_input = input("Please input either the machine name or last 3 digits of Serial Number:\n").upper()


# else:
user_input_object = obtain_user_input.GetUserInput(user_input)

machine_type = user_input_object.check_machine()
print(machine_type)
new_current_readings = obtain_user_input.get_readings(machine_type)
print(new_current_readings)

excel_readings_object = get_reading.GetReadings(user_input)

current_reading = excel_readings_object.get_reading_dict(3)
previous_reading = excel_readings_object.get_reading_dict(5)
difference = excel_readings_object.get_reading_dict(6)

print(current_reading)
print(previous_reading)
print(difference)

if user_input_object.selected_machine in data.printers["B&W"] or user_input_object.selected_machine in \
        data.printers["COLOUR"]:
    ask_user = True

else:
    ask_user = False

while ask_user:
    # prompt user on whether they would like to modify the "CONDITION" or "COMMENTS" columns
    modify_further = input("Would you like to modify the 'CONDITION' or 'COMMENTS'? (Y/N)\n").upper()
    if modify_further == "Y":
        obtain_user_input.modify_further()
        ask_user = False

    elif modify_further == "N":
        ask_user = False

    else:
        print("Invalid input. Please rectify!")
        continue

