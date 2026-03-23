import random

def solve_ivan_auto():
    
    n = int(input("Enter max number: ").strip())
    possible_numbers = set(range(1, n + 1))
    
    print(f"Game started! Possible numbers: 1-{n}")
    print("=" * 35)

    step = 1
    while len(possible_numbers) > 2:
        current_list = list(possible_numbers)
        k = random.randint(1, len(current_list))
        question_numbers = set(random.sample(current_list, k))
        
        print(f"Step {step}. Kate asks about: {' '.join(map(str, sorted(list(question_numbers))))}")
        
        intersection = possible_numbers.intersection(question_numbers)
        count_in = len(intersection)
        count_total = len(possible_numbers)
        
        if count_in > count_total / 2:
            print("Ivan says: Yes")
            possible_numbers = intersection
        else:
            print("Ivan says: No")
            possible_numbers = possible_numbers - question_numbers
        
        print(f"Remaining options: {len(possible_numbers)}\n")
        step += 1
        
        if step > 20: break 

    print("All done")
    result = sorted(list(possible_numbers))
    print(f"Numbers Ivan could have guessed: {' '.join(map(str, result))}")

if __name__ == "__main__":
    solve_ivan_auto()