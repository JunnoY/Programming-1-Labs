import re


def get_choice():
    choice = input("Enter encrypt or decrypt: ")
    while not (re.search("encrypt", choice) or re.search("decrypt", choice)):
        print("You entered:", choice, "this is not a valid option")
        choice = input("Enter encrypt or decrypt: ")
    if choice[0] == 'e' or choice[0] == 'E':
        return -3
    else:
        return 3


def do_conversion(input_text, shift_value):
    resulting_text = ""
    input_text_position = 0
    while (input_text_position < len(input_text)):
        input_text_char = input_text[input_text_position]
        ascii_value = ord(input_text_char)
        ascii_value += shift_value
        resulting_text = resulting_text + chr(ascii_value)
        input_text_position += 1
    return(resulting_text)


def decrypt_conversion(content, shift_value):
    original_text = ""
    content_position = 0
    while (content_position < len(content)):
        content_char = content[content_position]
        ascii_value = ord(content_char)
        ascii_value += shift_value
        original_text = original_text + chr(ascii_value)
        content_position += 1
    return(original_text)


def main():
    shift_value = get_choice()
    if shift_value == 3:
        readname = input("Enter a filename:")
        rh = open(readname, "r")
        content = rh.read()
        original_text = decrypt_conversion(content, shift_value)
        rh.close()
        print(original_text)
    else:
        input_text = input('Input text: ')
        resulting_text = do_conversion(input_text, shift_value)
        text_choice = input('Enter \'wf\' to write to file ' + ' or \'ds\''
                            'to display on screen: ')
        while not (re.search("wf", text_choice) or
                   re.search("ds", text_choice)):
            print("You entered:", text_choice, "this is not a valid option")
            text_choice = input('Enter \'wf\' to write to file ' + ' or \'ds\''
                                'to display on screen: ')
        if text_choice == 'wf':
            write_to_file(resulting_text)
        else:
            print(resulting_text)


def write_to_file(resulting_text):
    while True:
        try:
            filename = input("Enter a filename:")
            fh = open(filename, "x")
            fh.write(resulting_text)
            fh.close()
            break
        except IOError:
            print("Something went wrong, perhaps file already exists?")


main()
