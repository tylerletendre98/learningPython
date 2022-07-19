def main():
    personsanswer = input('Enter a enter a word, phrase, or number to test for pallendrom or exit to exit ')

    if (personsanswer == "exit"):
        print('thankyou for playing')
    else:
        answerinstring = personsanswer.split(personsanswer)
        print(answerinstring)

main()