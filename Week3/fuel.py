"""
Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein X is a non-negative integer and Y is a positive integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.


"""

def main():
    while True:
        try:
            z = input("Fraction: ")
            a,b = z.split("/")
            a = int(a)
            b = int(b)

            if a<0 or b < 0 or a > b or b == 0:
                continue
            x = a/b
            
        except ValueError:
            continue

        except ZeroDivisionError:
            continue

        else:
            guage(x)
        break

def guage(x):
    y = round(x*100)

    if 0<=y<=1:
        print("E")

    elif 1<y<99:
        print(y,"%",sep="")

    elif 99<=y<=100:
        print("F")

main()