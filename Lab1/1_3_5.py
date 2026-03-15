import math

def calc_y_for(x, n):
    print("\nCalculation with 'for' loop started")
    cur_arithm_sum = (n * (n + 1)) // 2
    result = 0 

    for i in range (n,0,-1):
        result = math.sqrt(cur_arithm_sum + x + result)
        cur_arithm_sum -= i
    print(f"Result: y={result:.2f}\n")

def calc_y_while(x, n):
    print("\nCalculation with 'while' loop started")
    cur_arithm_sum = (n * (n + 1)) // 2
    result = 0 
    temp_n = n

    while temp_n>0:
         result = math.sqrt(cur_arithm_sum + x + result)
         cur_arithm_sum -= temp_n
         temp_n -= 1
    print(f"Result: y={result:.2f}\n")

def calc_y_recursive(i, x, n):
    print("\nCalculation with 'recursive' loop started")
    result = recursive_sqrt(1, x, n, 0)
    print(f"Result: y={result:.2f}")

def recursive_sqrt(i, x, n, current_sum):
    #exit condition
    if i > n:
        return 0
    #calculation
    sum_i = (i * (i + 1)) // 2
    inner_root = recursive_sqrt(i + 1, x, n, current_sum)

    return math.sqrt(sum_i + x + inner_root)



print("\nLet's calculate this function!")
print("Function is defined as follows: sqrt(1+x+sqrt(1+2+x+sqrt(...)))\n")

while True:
    try: 
        input_vals = input("\nEnter value of X (degr) and N (or 'exit'): ").strip()
        if input_vals.lower() == 'exit':
            break
        
        vals = input_vals.split()
        if len(vals) != 2:
            print("Error: Please enter two values.")
            continue

        input_x = float(vals[0])
        input_n = int(vals[1])
        
        if input_n <= 0:
            print("N must be > 0.")
            continue
            
    except (ValueError, IndexError):
        print("Invalid input format.")
        continue

    while True:
        choice = input("Press:\n 1 - FOR loop\n 2 - WHILE loop\n 3 - REQURSION\n 4 - New numbers\n 5 - Exit\n").strip().lower()

        match choice:
                case '1': calc_y_for(input_x, input_n)
                case '2': calc_y_while(input_x, input_n)
                case '3': calc_y_recursive(1, input_x, input_n)
                case '4': break
                case '5': exit()
                case _: print("Wrong input. Please, try again.")