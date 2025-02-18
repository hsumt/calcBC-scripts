# Description: Using Simpson's Rule to approximate an integral approximation of the arc length of a sinusoidal modeling of bent sheet metal to the degree of 6 digit Desmos precision.
import math
def f(x):
   #f(x) = sqrt(1 + ( (3pi/20)) * cos^2(3pi/20 *x))
   factor = 3* math.pi / 20
   return math.sqrt(1+(factor**2) * (math.cos(factor * x)**2))
def simpson(f, a, b, N): #f the function, a and b are the endpoints and N is the subintervals
   if N & 2 != 0:
    raise ValueError("N must be an even integer")
   dx = (b - a) / N
   # list of all the a to b x values so we can apply them later
   x_values = [a + i * dx for i in range(N + 1)]
   y_values = [f(x) for x in x_values]
   #printing a table for my teacher nuke for debugging
   show_table = input("Full table of values? (y/n): ").strip().lower()
   if show_table == 'y':
     print("[Simpson Table approx]")
     print(f"{'i':>3} {'x_i':>8} {'f(x_i)':>15}")
     print("-" * 32)
     for i, (x_val, y_val) in enumerate(zip(x_values, y_values)):
       print(f"{i:>3} {x_val:>10.5f} {y_val:>15.8f}")
   show_sum = input("Detailed summation (y/n): ").strip().lower()
   odd_sum = sum(y_values[i] for i in range(1, N, 2))
   even_sum = sum(y_values[i] for i in range(2, N, 2))
   if show_sum == 'y':
    print("\nDetailed Summation:") #for debugging go and comment this out
    print("f(x_0) =", y_values[0])
    print("f(x_N) =", y_values[-1])
    print("Sum of odd-indexed values: ", odd_sum)
    print("Sum of even-indexed values: ", even_sum)

   long_sum = y_values[0] + y_values[-1] + 4 * odd_sum + 2 * even_sum
   # print("\nLong Sum = f(x_0) + f(x_N) + 4*(odd sum) + 2*(even sum) =", long_sum) this is only for testing
   # print ("0.5 / 3 *", long_sum)
   S = dx / 3 * long_sum
   print("Final Simpson's Approx is", S)

   # simpson S = dx / 3 * (y_values[0] + y_values[-1] + 4 * odd_sum + 2 * even_sum)

   return S
def main():
  while True:
    negateValue = False
    try:
        a = float(input("Enter lower bound: ").strip())
        b = float(input("Enter upper bound: ").strip())
        if a >= b:
           c = a
           a = b
           b = c
           negateValue = True
           
        temp_N = input("How many subintervals are you computing? (pick an even number): ").strip().lower()
        N = int(temp_N)
        if N % 2 != 0:
            raise ValueError("User entered non-even integer")
        break
    except ValueError as e:
        print("Invalid input. Please enter an even int")
  approx = simpson(f,a,b,N)
  if negateValue == True:
    approx = -approx
  print("The approximate of the integral from 0 --> 20 using Simpson's with N = 40")
  print("Result =", approx)
#def complete. run main

if __name__ == '__main__':
    main()
