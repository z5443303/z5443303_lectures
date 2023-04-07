
test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 22, 23, 25, 29, 30, 31]
def is_even_num(lis):
    evennum = []
    for n in lis:
        if n % 2 == 0:
            evennum.append(n)
            return evennum

is_even_num(test_list)

test_list = [2, 3, 10, 14, 20, 21, 25, 13, 15]
1st = [2, 3, 10, 14, 20, 21, 25, 13, 15]

new_1st = [x**2 for x in 1st if x**2>150]

print(f'the new list with value if square greater than 150 in{new_list}')





