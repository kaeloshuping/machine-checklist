import data


def get_colour_readings():
    total_reading = int(input("Please input the Total meter reading:\n"))
    colour_reading = int(input("Please input the Colour meter reading:\n"))
    black_reading = int(input("Please input the Black meter reading:\n"))
    colour_readings = {
        "T": total_reading,
        "C": colour_reading,
        "B": black_reading
    }
    if colour_reading + black_reading != total_reading:
        # if the sum does not equal the total, print a statement highlighting the issue
        print(f"The sum of the Colour Reading: {colour_reading} and Black Reading: {black_reading} "
              f"does not equal to the Total Reading: {total_reading}!. Please correct!")

        # request for all meter readings again T,C,B
        get_colour_readings()
    return colour_readings


# this function prompts the user on whether they would like to modify any of either the "CONDITION" or "COMMENTS"
# columns
def modify_further():
    # prompt which column the user wishes to modify further
    column_to_modify = input("Choose the column to modify. 'CONDITION' or 'COMMENTS'\n").upper()

    if column_to_modify == "CONDITION":

        # if they choose the "CONDITION" column, prompt which way they would like to toggle the condition (N/NW)
        change_condition = input("What condition would you like to change the 'CONDITION' to? (W/NW)\n").upper()

        if change_condition == "NW":
            # if they change the condition to "NW" for "NOT WORKING", they need to modify the "COMMENTS" column with
            # the reason as to why the corresponding machine is in a NOT WORKING condition
            print("You have to provide comments as to why machine is Not Working.")
            comments = input("What is the problem with the machine?\n")
            condition_and_comment = {
                "CONDITION": "NOT WORKING",
                "COMMENT": comments,
            }
            return condition_and_comment

        return "WORKING"

    elif column_to_modify == "COMMENTS":

        # otherwise if they choose the "COMMENTS" column, prompt them for the comments that they would like to add
        comments = input("What comments would you like to add?\n")
        return comments

    else:
        print("\nInvalid input please choose the correct options")
        modify_further()


"""
This Class prompts the user for either the serial number of a machine or the name of the machine incase it belongs
to the finishing equipment and checks whether to prompt the user further for meter readings or the condition of 
the machine
"""


class GetUserInput:

    def __init__(self, selected_machine):
        # prompt user for either serial number (last 3 digits) or machine name
        self.selected_machine = selected_machine

    def check_machine(self):
        # check whether serial number is in the dictionary for B&W printers
        if self.selected_machine in data.printers["B&W"]:
            # give 1 prompt for the TOTAL meter reading if it is
            black_reading = int(input("Please input the Total meter reading:\n"))
            return {"B": black_reading}

        # check whether serial number is in the dictionary for COLOUR printers and
        elif self.selected_machine in data.printers["COLOUR"]:

            # give 3 prompts for the TOTAL, COLOUR and B&W meter reading if it is
            return get_colour_readings()

        # check whether the machine name is in the list of finishing equipment
        elif self.selected_machine in data.finishing_equipment:
            return modify_further()

        # else:
        #     print("Invalid input. Please input last 3 digits of printer serial number or finishing equipment name!")
        #     user_input = input("Please input either the machine name or last 3 digits of Serial Number:\n").upper()
        #     user_input_object = self.GetUserInput(user_input)
        #     new_current_readings = user_input_object.check_machine()

