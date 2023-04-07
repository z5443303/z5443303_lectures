hours = input('Enter number of hours you worked this week: ')
#python 3 output numeric value as a string in input () function
hours = int(hours)
normal_rate = 51.45
overload_rate = 88.9

if hours > 35 :
    pay = (35 * normal_rate) + ((hours - 35) * overload_rate)
else :
    pay = hours * noamal_rate

print(f'This weekly payment is: {pay}')

  