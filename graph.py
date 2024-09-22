import matplotlib.pyplot as plt

# Function to plot the data
def plot_newton_secant(newton_data, secant_data):
    iterations = list(range(1, 21))  # Iteration numbers from 1 to 20

    # Plot for Newton-Raphson
    plt.plot(iterations, newton_data, label='Newton-Raphson', color='blue', marker='o')

    # Plot for Secant Method
    plt.plot(iterations, secant_data, label='Secant Method', color='green', marker='x')

    # Labeling the axes
    plt.xlabel('Iteration Number')
    plt.ylabel('f(x)')

    # Adding a title
    plt.title('Comparison of Newton-Raphson and Secant Method')

    # Adding a legend to differentiate the lines
    plt.legend()

    # Show the plot
    plt.grid(True)
    plt.show()

# Input function to get 20 f(x) values
def get_fx_values(method_name):
    print(f"Enter 20 f(x) values for {method_name}, separated by spaces:")
    user_input = input()
    values = list(map(float, user_input.split()))
    
    if len(values) != 20:
        print(f"Error: You must enter exactly 20 values for {method_name}.")
        exit(1)
    
    return values

# Getting input values for Newton-Raphson and Secant methods
newton_data = get_fx_values("Newton-Raphson")
secant_data = get_fx_values("Secant")

# Call the function to plot the graph
plot_newton_secant(newton_data, secant_data)
