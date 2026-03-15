import math

def simple_cycle():
    print("Simple cycle test:")

    while True:
        input_val = input("Type a number in a range of 1 to 10 or 'EXIT' to quit the program: ").strip()

        if input_val.lower() == "exit":
            print("Okay, bye!")
            break
        try:
            num = int(input_val)
            if 1<= num <= 10:
                print("Good job! Bye~")
                break
            else: 
                print("Try again")
                continue
        except ValueError:
            print("I am a surgeon!")
            continue 

# simple_cycle()