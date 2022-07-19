def main():
    x=0

    # while loop

    # while(x<=5):
    #     print(x)
    #     x += 1

    #for loop

    # for x in range(2,10):
    #     print(x)

    # interating over a list
    # days=['mon','tues',"weds",'thurs',"fri","sat",'sun']

    # for x in days:
    #     print(x)

    # using break and continue
    # for x in range(2,10):
    #     if x == 7:
    #         break
    #     print(x)
    #     if x % 2 == 0:
    #         continue
    #     print(x)

    days=['mon','tues',"weds",'thurs',"fri","sat",'sun']
    for i,d in enumerate(days):
        print(i,d)

main()