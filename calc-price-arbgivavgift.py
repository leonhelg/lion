#!/usr/bin/env python

"""This application calculates useful numbers for my companies"""

def input_price(prompt = 'Please write the price you want converted:'):
    return input(prompt)

def arbgivavgift(amount):
    return amount*0.141,amount*1.141

def tax(amount):
    return amount*0.25,amount*1.25

def view():
    input_p = input_price()
    arbgivavg, arbgivavgift_total = arbgivavgift(input_p)
    tax_base,tax_total = tax(arbgivavgift_total)
    print(f'Ferdig pris i kr inkl.mva: {tax_total} \n\n Skatt 25%: {tax_base}')
    print(f'Arbeidsgiveravgift 14,1%: {arbgivavg} \n Forrige pris: {input_p}')

def isRunning():
    isRunning = True
    while isRunning == True:
        usr_input = input('\n\nThis application makes a new price for Aksjeselskap\n\nMain Menu\nPress enter to run the program or q to quit\n')
        if usr_input.lower != 'q':
            view()
            usr_input = input('The program has ended, press ENTER to run again or "q" to quit')
            if usr_input.lower == 'q':
                isRunning = False