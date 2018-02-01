# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 09:22:46 2017

@author: surakum2
"""

# Invoke this function if the command is 'list'
def listdir(*args):
    print("Listing contents of", args)

# Invoke this function if the command is 'whoami'
def show_user(*args):
    from getpass import getuser
    print(getuser())

# Invoke this function if the command is 'date'
def print_date(*args):
    from time import ctime
    print(ctime())

# Invoke this function if the command is 'pwd'
def show_curr_dir(*args):
    from os import getcwd
    print(getcwd())

# Invoke this function if the command is 'exit'
def exit_shell(*args):
    global quit
    quit = True

# Invoke this function if the command is anything else
def invalid_command(*args):
    print("Invalid command - ", args[0])

commands={
    "list":listdir,
    "whoami": show_user,
    "pwd": show_curr_dir,
    "date": print_date,
    "exit": exit_shell
}
def run():
    while not quit:
        command = input("PyShell> ")
        args=commands.split()
        commands.get(args[0],invalid_command)(*args)

if __name__ == '__main__':
    run()
