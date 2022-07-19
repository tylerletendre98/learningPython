
from cgitb import reset
from unittest import result


def main(): 
    x, y = 10, 100

    # traditional if else statements

    # if x < y :
    #     result = "x is less than y"
    # elif x == y:
    #     result="x is equal to y" 
    # else: 
    #     result="x is greater than y"
    # print(result)


    # handles one line if else statements

    # result = "x is less than y" if x < y else "x is greater than y"
    # print(result)

    # match-case
    # value = input('type one, two, three, or four ')
    # match value:
    #     case "one":
    #         result = 1
    #     case "two":
    #         result = 2
    #     case "three" | "four":
    #         result = (3,4)
    #     case _:
    #         result = -1
    # print(result)
    
main()