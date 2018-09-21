#!user/bin/env python3
"""
MA305 - CW2 : Piers Chapman 20SEP18
Purpose: Convert from Celsius to Fahrenheit
"""
#Receive the input
print('Please enter the temperature in Celsius:')
cel = float(input('Celsius='))

#Calculate the temperature
fah = (9/5)*cel+32
print(cel,' degrees Celsius converts to ',fah,' degrees Fahrenheit.')
