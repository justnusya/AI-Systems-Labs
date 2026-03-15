import math

def calculate_y():
    print("Lazy calculator: only for one function. No chance for mistake.")

    try:
        user_input = input("\nEnter value of x (in degrees): ")

        x_deg = float(user_input)
        x_rad = math.radians(x_deg)
        
        result = None
        reason = ""

        if x_deg < 1:
            argument = math.sin(x_rad) + 0.5
            if argument <= 0:
                reason = f"Argument of the logarithm ({argument:.2f}) <= 0. The logarithm is not defined."
            else:
                result = math.log(argument)
                print(f"Calculated using the first formula: ln(sin({x_deg}) + 0.5)")

        elif x_deg > 10:
            # arcsin працює тільки для радіан від -1 до 1
            if x_rad > 1 or x_rad < -1:
                reason = f"Argument of arcsin({x_rad:.2f} rad) is outside the range [-1, 1]."
            else:
                tan_val = math.tan(x_rad**2)
                if tan_val == 0:
                    reason = "ctg(x^2) does not exist (division by zero in tan)."
                else:
                    under_root = 1 - math.asin(x_rad)
                    if under_root <= 0:
                        reason = "The expression under the square root is <= 0 or the denominator is zero."
                    else:
                        result = (1 / tan_val) / math.sqrt(under_root)
                        print(f"Calculated using the second formula: ctg(x^2) / sqrt(1 - arcsin x)")
        else:
            reason = "The value of x is in the range [1, 10], where the function is not defined."

        if result is not None:
            print(f"Result y = {result:.2f}")
        else:
            print(f"Error: {reason}")

    except ValueError:
        print("Error: Please enter a numeric value.")

if __name__ == "__main__":
    calculate_y()