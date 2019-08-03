#!/usr/bin/env python3
#!
# user_input_template.py
#
# 1. Functions for obtaining boolean, integer or float input from the console.
# 2. Function to provide a menu which returns an index into the menu list.
#    If menu is empty, returns -1
#
# Ian Stewart
# 2019-08-03
# CC0

import sys

def query_user_bool(prompt="Proceed?", default=True,):
    # Submit a boolean query to the User. Return True or False
    # No need for a while loop
    yes_tuple = ("y", "t", "1")
    no_tuple = ("n", "f", "0")
    # Build the prompt as [Y/n] or [N/y]
    if default:
        prompt = prompt + " [Y/n]: " 
        response = input(prompt)
        if response == "": response = "y"
        if response.lower()[0] in yes_tuple:
            return True
        else:
            return False
    else:
        prompt = prompt + " [N/y]: "
        response = input(prompt)
        if response == "": response = "n"
        if response.lower()[0] in no_tuple:
            return False
        else:
            return True


def query_user_integer(prompt="Enter an integer", min_int=0, max_int=10, default=None):
    # Query User to return an integer within a range. Allow default return value
    if default == None:  
        range_prompt = " [Min={}, Max={}]: ".format(min_int, max_int)  
        prompt = prompt + range_prompt
    else:
        full_prompt = (" [Min={}, Max={}][{}]: "
            .format(min_int, max_int, default))      
        prompt = prompt + full_prompt

    while True:
        response = input(prompt)
        if response == "":
            if default == None:
                print("Invalid response")
                continue
            else:
                response = int(default)
        try:
            response = int(response)
            if response < min_int or response > max_int:
                print("Invalid value. Requires an integer between {} and {}"
                    .format(min_int, max_int))
                continue
            else:
                return response
        except ValueError as e:
            print("Value Error. Requires an integer between {} and {}"
                    .format(min_int, max_int))
            continue


def query_user_float(prompt="Enter a float", min_val=0, max_val=10, default=None):
    # Query User to return a floating point value within a range
    if default == None:  
        range_prompt = " [Min={}, Max={}]: ".format(min_val, max_val)  
        prompt = prompt + range_prompt
    else:
        full_prompt = (" [Min={}, Max={}][{}]: "
            .format(min_val, max_val, default))      
        prompt = prompt + full_prompt


    while True:
        response = input(prompt)
        if response == "":
            if default == None:
                print("Invalid response")
                continue
            else:
                response = float(default)
        try:
            response = float(response)
            if response < min_val or response > max_val:
                print("Invalid value. Requires a value between {} and {}"
                    .format(min_val, max_val))
                continue
            else:
                return response
        except ValueError as e:
            print("Value Error. Requires a value between {} and {}"
                    .format(min_val, max_val))
            continue

def query_user_menu(menu_list, prompt=None, default=1):
    # User selects from a list. Return an index into the list
    if len(menu_list) == 0:
        return -1
    print()
    for index, item in enumerate(menu_list):
        print("{:>3}. {}".format(index + 1, item))
    if prompt == None:
        prompt = ("\nEnter the number of the item [{}]: "
                .format(default))
    else:
        prompt = ("\n{} [{}]: ".format(prompt, default))

    while True:     
        response = input(prompt)
        if response == "": response = default
        try:
            response = int(response)
            if response < 1 or response > len(menu_list):
                print("Invalid.  Requires a value between {} and {}"
                    .format(1, len(menu_list)))
                continue
            else:
                return response - 1
        except ValueError as e:
            print("Value Error. Requires a value between {} and {}"
                    .format(1, len(menu_list)))
            continue


def main():

    ##### Simple test boolen, integer, float using defaults

    response = query_user_bool()
    print(response)

    value = query_user_integer()
    print(value)

    value = query_user_float()
    print(value)

    ##### Test Boolean

    prompt = "Are you tall?"
    default = False
    response = query_user_bool(prompt, default,)
    print(response)


    ##### Test Integer

    prompt = "How old are you?"
    min_value = 1
    max_value = 100
    value = query_user_integer(prompt, min_value, max_value)
    print(value)

    prompt = "How old are you?"
    min_value = 1
    max_value = 100
    default = 50
    value = query_user_integer(prompt, min_value, max_value, default)
    print(value)


    ##### Test Float

    prompt = "Enter value for Pi"
    min_value = 3.0
    max_value = 3.2
    default = 3.14
    value = query_user_float(prompt, min_value, max_value, default)
    print(value)


    ##### Test Menu option

    prompt = "Choose a colour"
    menu = ["red", "green", "blue"]
    default = 2
    index = query_user_menu(menu, prompt, default)
    print(index, menu[index])

    prompt = "Choose a colour"
    menu = ["red", "green", "blue"]
    #default = 2
    index = query_user_menu(menu, prompt)
    print(index, menu[index])

    #prompt = "Choose a colour"
    menu = ["red", "green", "blue"]
    #default = 2
    index = query_user_menu(menu)
    print(index, menu[index])

    #prompt = "Choose a colour"
    menu = []
    #default = 2
    index = query_user_menu(menu)
    print("Returned index:", index) #, menu[index])


if __name__ == "__main__":

    main()
