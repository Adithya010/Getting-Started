def pnz_check():
    n = float(input("Enter the digit:"))
    if n > 0:
        print("Number is a positive number.")
    elif n == 0:
        print("Number is a zero number.")
    else:
        print("Number is a negative number.")


pnz_check()
