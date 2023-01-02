import time

def calculate_pi(iterations):
    # Initialize Pi to 0
    pi = 0

    # Start the timer
    start_time = time.time()

    # Iterate through the number of iterations
    for i in range(1, iterations+1):
        # Calculate the current term and add it to Pi
        pi += (-1)**i * (-4/(2*i-1))

    # Stop the timer
    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = end_time - start_time

    # Return the final value of Pi and the elapsed time
    return pi, elapsed_time

# Test the function with different values for the number of iterations
pi, elapsed_time = calculate_pi(1000000)
print(f"Pi = {pi}, elapsed time = {elapsed_time} seconds")

pi, elapsed_time = calculate_pi(10000000)
print(f"Pi = {pi}, elapsed time = {elapsed_time} seconds")

pi, elapsed_time = calculate_pi(100000000)
print(f"Pi = {pi}, elapsed time = {elapsed_time} seconds")

def calculate_pi(iterations):
    # Initialize Pi to 0
    pi = 0

    # Iterate through the number of iterations
    for i in range(1, iterations+1):
        # Calculate the current term and add it to Pi
        pi += (-1)**i * (-4/(2*i-1))

    # Return the final value of Pi
    return pi

