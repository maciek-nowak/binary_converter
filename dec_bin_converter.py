def print_result(number, system):
    print()
    print('/' + (len(number + system) + 5) * '-' + '\\')    #printing border around result
    print('|', number, '|', system, '|')
    print('\\' + (len(number + system) + 5) * '-' + '/' + '\033[0m')

def bin_to_dec(binary_nr):
    weight = len(binary_nr)-1  #counter is the weight of digit in binary number
    number = 0  #in the end it will contain the result of conversion
    for digit in binary_nr:
        number += int(digit) * 2 ** weight
        weight -= 1
    print_result(str(number), '10')

def dec_to_bin(decimal_nr):
    decimal_nr = int(decimal_nr)
    if decimal_nr != 0:
        number = ''
    else:
        number = '0'
    while decimal_nr > 0:
        reminder = decimal_nr % 2
        number = str(reminder) + number
        decimal_nr = decimal_nr // 2
    print_result(number, '2')

def check_user_input(user_input):
    user_input = user_input.split(' ')
    error_message = '\033[31m' + "Your input doesn't match the pattern. Try again." + '\033[0m'
    if len(user_input) == 2:    #checking nr of given parameters
        if user_input[1] == '10' and user_input[0].isdigit():   #checking if nr is decimal
            dec_to_bin(user_input[0])
        elif user_input[1] == '2' and user_input[0].count('0') + user_input[0].count('1') == len(user_input[0]): #checking if nr is binary
            bin_to_dec(user_input[0])
        else:
            print(error_message)    #error when there are 2 parameters but they are not binary nor decimal
    else:
        print(error_message)    #error when nr of parameters is different than 2

def main():
    user_input = ''
    print(chr(27) + "[2J")  #clear terminal screen
    print('Welcome to Binary Converter!')
    while user_input != 'exit': #main loop, continue until user type 'exit'
        print()
        user_input = input('Input number in decimal system with 10 after the space or number in binary system with 2 after the space. Type exit to close the application [eg. 101 2 or 519 10 or exit]: ' + '\033[32m')
        if user_input != 'exit':
            check_user_input(user_input)
    print('\033[0m' + 'Have a nice day! See you next time :)')

main()
