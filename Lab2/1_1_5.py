import random

def auto_fill():
    n = int(input("Enter the number of values: "))
    a = int(input("Enter the start value: "))
    b = int(input("Enter the end value: "))
    
    vals_list = []
    for i in range(n):
        vals_list.append(random.randint(a, b))

    return vals_list

if __name__ == "__main__":
    print(auto_fill())