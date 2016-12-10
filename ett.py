#!/usr/bin/python
#Eye Time Tracker
#Copyright (C) 2016 Saksham Mittal
#Defines all functions necessary for functioning of Eye Time Tracker.
#Dependencies - time, notify2 (python3 modules)


import time

#This function asks the user how many minutes they want the program to wait.
def ask():
    print("Welcome to Eye Time Tracker, by Saksham Mittal.")
    proceed_create = input("Proceed? [y or n] ")
    choice_1 = "y"
    choice_2 = "n"
    if proceed_create == choice_1:
        print("How many minute(s) would you like Eye Time Tracker to wait?")            
        global minute_wait
        minute_wait = input("> ")
    elif proceed_create == choice_2:
         print("Eye Time Tracker is now quitting. Goodbye.")
         quit()

#Defines the rest of the variables needed for ett to work
def all_vars(x): 
    try:
       x  = int(x)
    except ValueError:
        x = float(x)  
    global second_wait
    second_wait = x * 60

#Does the waiting and notifiying part
#Needs - time.sleep() and notify2 modules
def wait_a_lot(x):
    from time import sleep
    time.sleep(second_wait)
    worked = "You have worked for " + str(x) + " minute(s). Take a little break."
    import notify2
    notify2.init('Eye Time Tracker')
    n = notify2.Notification('Eye Time Tracker', worked)
    n.show()
    print(worked)
    print ('\a')

#Asks if you are taking a break right now
def break2():
    print("Are you taking a break right now? [y or n]")
    yon = input("> ")
    if yon == "y":
        print("How long?")
        global lng
        lng = input("> ")
        try:
            lng = int(lng)
        except ValueError:
            lng = float(lng)
        print("Ok. You are taking a break for " + str(lng) + " minute(s). Eye Time Tracker will ask you if you are here after " + str(lng) + " minutes.")
        # To be continued in break3(). Stay tuned and go down to learn what happens next! ;)


#Continuing from where we last left off in break2(), this function manages stuff to happen after 'lng' minutes have passed.        
def break3(x):
    from time import sleep
    time.sleep(x * 60)
    import notify2
    worked = str(x) + " minutes have passed. Your break is over. :("
    notify2.init('Eye Time Tracker')
    n = notify2.Notification('Eye Time Tracker', worked)
    n.show()
    print("Hello? Anyone there? [y or n]")
    print (worked)
    print ('\a')
    there = input("> ")
    if there == "y":
        print("Ok. Let's do this.")
        loop() 
    elif there == "n":
        print("Eye Time Tracker is now quitting. Goodbye.")
        quit() 
    
#The loop() function nests all of the above functions and executes them in a loop, with some conditions to fulfill to avoid errors like "variable 'foo' not defined"
def loop():
    while True:
        all_vars(minute_wait)
        wait_a_lot(minute_wait)
        break3(lng) 
        
ask() 
all_vars(minute_wait)
wait_a_lot(minute_wait)
break2()
break3(lng)
loop()
