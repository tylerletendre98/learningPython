try: 
    answer = input('What do you want to divide 10 by ')
    num = int(answer)
    print(10/num)
except ZeroDivisionError as e:
    print('You cant divide by zero')
except ValueError as e:
    print('You didnt give a valid number')
finally:
    print('this code always runs')