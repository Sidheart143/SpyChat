from __builtin__ import raw_input
from default_spy import spy
from default_user import details
from choices import choices
from termcolor import colored, cprint

while True:
    cprint("welcome!!", "cyan", attrs=['dark', 'underline', 'bold'])
    choice = raw_input(colored("Continue as "+spy['name']+" "+spy['salutation']+" or not (Y/N)\n", "yellow"))
    # Asking user to choose default or not
    if choice == "y" or choice == "Y":
        cprint("Welcome " + spy['name']+" "+spy['salutation'], "magenta", attrs=["bold"])
        while True:
                choices()
    # if user wants to create new Spy
    elif choice == "n" or choice == "N":
        print "Enter Your Details:"
        details()
        choices()
    else:
        # if user wants to exit
        if choice == "e" or choice == "E":
            cprint("Please visit again \n     GoodBye!!!", "red")
            exit()
        cprint("please try again", "red")
        cprint("Press E for exit", "red", attrs=["bold"])
