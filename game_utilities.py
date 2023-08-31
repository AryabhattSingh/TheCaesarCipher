logo = """
░█████╗░░█████╗░███████╗░██████╗░█████╗░██████╗░  ░█████╗░██╗██████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗  ██╔══██╗██║██╔══██╗██║░░██║██╔════╝██╔══██╗
██║░░╚═╝███████║█████╗░░╚█████╗░███████║██████╔╝  ██║░░╚═╝██║██████╔╝███████║█████╗░░██████╔╝
██║░░██╗██╔══██║██╔══╝░░░╚═══██╗██╔══██║██╔══██╗  ██║░░██╗██║██╔═══╝░██╔══██║██╔══╝░░██╔══██╗
╚█████╔╝██║░░██║███████╗██████╔╝██║░░██║██║░░██║  ╚█████╔╝██║██║░░░░░██║░░██║███████╗██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝  ░╚════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
"""

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
             'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encode(user_message, shift_value):
    encoded_message = ""
    for letter in user_message:
        if letter in alphabets:
            index_of_letter = alphabets.index(letter)
            # new index after adding shift value
            new_index = index_of_letter + shift_value
            if new_index >= 26:
                new_index = new_index - 26  # This will give a value between [0,25]
            encoded_message += alphabets[new_index]
        else:
            encoded_message += letter
    return encoded_message


def decode(user_message, shift_value):
    decoded_message = ""
    for letter in user_message:
        if letter in alphabets:
            index_of_letter = alphabets.index(letter)
            # new index after subtracting shift value
            new_index = index_of_letter - shift_value
            if new_index < 0:
                new_index = 26 + new_index  # This will give a value between [0,25]
            decoded_message += alphabets[new_index]
        else:
            decoded_message += letter
    return decoded_message
