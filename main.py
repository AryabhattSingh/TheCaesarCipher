from game_utilities import *

# printing a coloured logo
print(f"\033[31m{logo}\033[00m")

operation_list = ["exit", "encoding", "decoding"]
should_loop_continue = True

while should_loop_continue:
    operation_choice = input("\nWhat do you want to do? Type the option number to perform an action:\n"
                             "0. Exit\n"
                             "1. Encode a message\n"
                             "2. Decode a message\n"
                             "\nEnter your choice : """)

    if operation_choice not in ["0", "1", "2"]:
        print("\nKindly enter a valid input!")
    elif operation_choice == "0":
        print("\nGoodbye!")
        should_loop_continue = False
    else:
        operation_choice = int(operation_choice)
        original_choice = operation_choice
        message = input(f"\nEnter your message for {operation_list[operation_choice]} : ").lower()
        try:
            # If user enters any value other than an integer (-ve, 0, or +ve), the control would go into
            # except block
            shift_number = int(input("\nEnter the shift number : "))

            # if shift_number is negative then obtain absolute value and flip the operation_choice
            if shift_number < 0:
                shift_number = abs(shift_number)
                if operation_choice == 1:
                    operation_choice = 2
                else:
                    operation_choice = 1

            # As Ceaser Cipher works in a circular way, 26 will become 0, 27 -> 1 and so on.
            if shift_number >= 26:
                shift_number = shift_number % 26

            # printing the operation that user wanted
            if original_choice == 1:
                print("\nEncoded Message: ", end="")
            else:
                print(f"\nDecoded Message: ", end="")

            # calling the encoding/decoding functions
            if operation_choice == 1:
                print(encode(message, shift_number))
            else:
                print(decode(message, shift_number))

        except ValueError:
            print("\nKindly enter an integer shift value.")
