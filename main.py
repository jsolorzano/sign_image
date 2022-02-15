import os
import time
from classes.validations import Validations
from classes.processimg import ProcessImg
from prettytable import PrettyTable
validator = Validations()

def print_options():
    print('IMAGE PROCESSING')
    print('*' * 50)
    print('Select an option:')
    print('[S]ign image')
    print('[E]xit')
    
def sign_image():
    print('IMAGE SIGNATURE')
    print('*' * 50)
    name = check_name()
    
    process = ProcessImg(name)
    if process.process_image():
        _print_table_result('Successfully signed image')
        _show_image()
    else:
        _print_table_result('Error signing image')
      
def check_name():
    print('Enter the name:')
    name = input()
    try:
        validator.validateName(name)
        return name
    except ValueError as err:
        print(err)
        check_name()

def _print_table_result(result):
    table = PrettyTable(['Result'])
    table.add_row([
		result
	])

    print(table)
    print('Press any letter to continue')
    command = input()

def _show_image():
    process = ProcessImg("", "result.jpg")
    process.show_image()

def run():
    print_options()

    command = input()
    command = command.upper()

    if command == 'S':
        sign_image()
    elif command == 'E':
        os._exit(1)
    else:
        print('Invalid command')
        time.sleep(1)
        run()

if __name__ == '__main__':
	run()
