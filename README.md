# calculate_pi

This is a Python script for calculating the value of Pi using Newton's infinite series method. The script includes a function called calculate_pi() which takes in a single parameter, iterations, and returns the calculated value of Pi as well as the elapsed time for the calculation.

To use the script, simply call the calculate_pi() function and pass in the desired number of iterations as an argument. The function will return a tuple with the calculated value of Pi and the elapsed time in seconds.

Example:

```pi, elapsed_time = calculate_pi(1000000)
print(f"Pi = {pi}, elapsed time = {elapsed_time} seconds")
```
Output:

```Pi = 3.141592653589793, elapsed time = 0.03717913627624512 seconds
Note: The larger the number of iterations, the more accurate the calculated value of Pi will be, but the longer the elapsed time will be.
```
