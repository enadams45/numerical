import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Function to get input values
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

# Iteration numbers from 1 to 20
iterations = list(range(1, 21))

# Creating a DataFrame for the table
data = {
    "Iteration": iterations,
    "Newton-Raphson f(x)": newton_data,
    "Secant f(x)": secant_data
}

df = pd.DataFrame(data)

# Create the figure and the axis
fig, ax = plt.subplots(figsize=(8, 5))

# Hide the axes
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.set_frame_on(False)

# Create the table
table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

# Style adjustments
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

# Apply color to the header row
header_color = '#f2a900'
for (i, j), cell in table.get_celld().items():
    if i == 0:  # This is the header row
        cell.set_fontsize(12)
        cell.set_text_props(weight='bold')
        cell.set_facecolor(header_color)

# Apply different colors to each column
column_colors = ['#e8e8e8', '#d3e9d3', '#d3d3e9']
for j in range(3):  # 3 columns
    for i in range(1, len(df)+1):  # Iterate over rows (skip header)
        table[(i, j)].set_facecolor(column_colors[j])

# Save the table as a PNG image
plt.savefig('colored_newton_secant_table.png', bbox_inches='tight', dpi=300)

# Show the image
plt.show()
