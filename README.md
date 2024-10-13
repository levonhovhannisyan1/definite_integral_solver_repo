# definite_integral_solver_repo

Definite Integral Solver using Darboux Sums
This Python project solves primitive definite integrals using Darboux sums and visualizes the area under the curve using matplotlib. The accuracy may be limited due to the simplicity of the Darboux sum approach, but this project serves as an excellent introduction to numerical integration and function visualization.


Features

1. Evaluate definite integrals using Darboux sums.
2. Handles a wide variety of mathematical functions, including trigonometric, logarithmic, and exponential functions.
3. Generates a graphical representation of the function and highlights the area enclosed between the bounds.


Installation

Clone the repository to your local machine:
git clone https://github.com/yourusername/definite-integral-solver.git
cd definite-integral-solver

Install the required dependencies:
pip install numpy matplotlib


Usage

You can run the script by providing a mathematical function and the integration bounds.
python definite_integral_solver.py

The program will prompt you for:
A function expression (e.g., x**2, sin(x), etc.).
Lower bound of the integral.
Upper bound of the integral.
After calculating the result, the script will display a graph showing the function and the area under the curve.


Example

Enter function expression (e.g., x**2): x**2
Enter lower bound: 0
Enter upper bound: 2
The program will calculate the definite integral of x**2 from 0 to 2 and plot the area under the curve.


Notes

1. Functions must be entered as Python expressions.
2. The bounds can include mathematical constants like pi and e.
3. The results may have some inaccuracy due to the basic nature of Darboux sums.


Structure

The code is structured around the DefiniteIntegral class, which encapsulates all functionality related to defining the integral, calculating the area, and generating the graph.

Class: DefiniteIntegral

Attributes
function: A string representing the mathematical expression to be integrated.
lower_bound: A float representing the lower limit of integration.
upper_bound: A float representing the upper limit of integration.

Methods
__init__(self, function, lower_bound, upper_bound)
1. Initializes the instance with the function and bounds.
2. Validates that the function is a non-empty string and that bounds are numeric values.
3. Raises ValueError if the input is invalid.

to_dict(self)
1. Converts the instance attributes into a dictionary format for easier access in calculations.
2. Returns a dictionary with keys: 'y', 'a', 'b', 'length', and 'delta_x'.

get_function_expression(self, x)
1. Translates the user-defined function into a format suitable for evaluation with NumPy.
2. Uses regular expressions to replace common mathematical functions (e.g., sin, cos, log) with their 3. NumPy equivalents.
3. Returns the modified expression as a string.

calculate(self)
1. Implements the Darboux sum to compute the definite integral.
2. Divides the interval into rectangles (based on the delta_x) and sums the areas of these rectangles.
3. Uses eval to compute the height of each rectangle based on the function.
4. Returns the total area formatted to two decimal places.

graph(self)
1. Generates a plot of the function over the specified bounds.
2. Uses NumPy to create an array of x-values and evaluates the function at each point.
3. Fills the area under the curve between the specified bounds, providing a visual representation of the integral.
4. Displays the graph with appropriate labels, legends, and gridlines.


Error Handling

The code includes error handling for:
1. Invalid function expressions.
2. Non-numeric bounds.
3. Errors during function evaluation (e.g., division by zero).