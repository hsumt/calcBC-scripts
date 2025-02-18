import math
def f(x):
   """ f(x) = sqrt(1 + ( (3pi/20))) * cos^2(3pi/20 *x) )) """
   factor = 3* math.pi / 20
   return math.sqrt(1+(factor**2) * (math.cos(factor * x)**2))
def simpson(f, a, b, N): #f the function, a and b are the endpoints and N is the subintervals
   if N & 2 != 0:
    raise ValueError("N must be even int")
   dx = (b-a)/N
   # list of all the a to b x values so we can apply them later
   x_values = [a + i * dx for i in range(N + 1)]
   y_values = [f(x) for x in x_values]
   #printing a table so it looks nice when i submit assignment
   print("{:>3s} {:>10s} {:>15s}".format("i", "x_i", "f(x_i)"))
   print("-" * 32)
   for i, (x_val, y_val) in enumerate(zip(x_values, y_values)):
     print("{:>3d} {:>10.5f} {:>15.8f}".format(i, x_val, y_val))
    # next part we compute the sums
   odd_sum = 0.0
   even_sum = 0.0
   for i in range(1, N):
       if i % 2 == 1:  # odd index 1,3,5,etc.
        odd_sum += y_values[i]
       else: #even index 2,4,6,etc.
         even_sum += y_values[i]
   print("\nDetailed Summation:")
   print("f(x_0) =", y_values[0])
   print("f(x_N) =", y_values[-1])
   print("Sum of odd-indexed values (i = 1,3,...,N-1):", odd_sum)
   print("Sum of even-indexed values (i = 2,4,...,N-2):", even_sum)
   
   long_sum = y_values[0] + y_values[-1] + 4 * odd_sum + 2 * even_sum
   print("\nLong Sum = f(x_0) + f(x_N) + 4*(odd sum) + 2*(even sum) =", long_sum)
   print ("0.5 / 3 *", long_sum)
   S = dx / 3 * long_sum
   print("Final Simpson's Approx is", S)

   # S = dx / 3 * (y_values[0] + y_values[-1] + 4 * odd_sum + 2 * even_sum)

   return S
def main():
  a = 0.0
  b = 20.0
  N = 40
  approx = simpson(f,a,b,N)
  print("Approx the integral from 0 --> 20 using Simpson's with N = 40")
  print("Result =", approx)

if __name__ == '__main__':
    main()