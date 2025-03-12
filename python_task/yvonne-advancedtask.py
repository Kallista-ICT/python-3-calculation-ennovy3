import math

# Function to compute the roots using the quadratic formula
def quadratic_formula(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2
    elif discriminant == 0:
        x1 = x2 = -b / (2*a)
        return x1, x2
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        return real_part + imaginary_part*1j, real_part - imaginary_part*1j

# Function to display the factorized form of the quadratic equation
def factorize_quadratic(a, b, c):
    x1, x2 = quadratic_formula(a, b, c)
    if isinstance(x1, complex):
        return f'{a}(x - ({x1}))(x - ({x2}))'
    else:
        return f'{a}(x - {x1})(x - {x2})'

# Accepting user input from the terminal
def main():
    print("Enter the coefficients of the quadratic equation (ax^2 + bx + c = 0):")
    
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    
    factorized_form = factorize_quadratic(a, b, c)
    print(f"The factorized form of the quadratic equation {a}x^2 + {b}x + {c} is:")
    print(factorized_form)

# Run the main function
if __name__ == "__main__":
    main()

