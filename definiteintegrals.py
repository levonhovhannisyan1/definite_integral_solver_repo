import numpy as np
import re
import matplotlib.pyplot as plt

class DefiniteIntegral:
    def __init__(self, function, lower_bound, upper_bound):
        if not isinstance(function, str) or not function:
            raise ValueError("Function must be a non-empty string.")
        self.function = function

        try:
            self.lower_bound = float(lower_bound)
            self.upper_bound = float(upper_bound)
        except ValueError:
            raise ValueError("Lower and upper bounds must be numeric values.")

        if self.lower_bound >= self.upper_bound:
            raise ValueError("Lower bound must be less than upper bound.")

    def to_dict(self):
        return {
            'y': self.function,
            'a': self.lower_bound,
            'b': self.upper_bound,
            'length': self.upper_bound - self.lower_bound,
            'delta_x': 1 / 10000,
        }

    def get_function_expression(self, x):
        expression = self.function
        expression = re.sub(r'sin\(', 'np.sin(', expression)
        expression = re.sub(r'cos\(', 'np.cos(', expression)
        expression = re.sub(r'tan\(', 'np.tan(', expression)
        expression = re.sub(r'log\(', 'np.log(', expression)
        expression = re.sub(r'log10\(', 'np.log10(', expression)
        expression = re.sub(r'sqrt\(', 'np.sqrt(', expression)
        expression = re.sub(r'exp\(', 'np.exp(', expression) 
        expression = re.sub(r'arcsin\(', 'np.arcsin(', expression)
        expression = re.sub(r'arccos\(', 'np.arccos(', expression)
        expression = re.sub(r'arctan\(', 'np.arctan(', expression)
        expression = re.sub(r'sinh\(', 'np.sinh(', expression) 
        expression = re.sub(r'cosh\(', 'np.cosh(', expression)
        expression = re.sub(r'tanh\(', 'np.tanh(', expression)
        expression = re.sub(r'abs\(', 'np.abs(', expression)
        expression = re.sub(r'floor\(', 'np.floor(', expression)
        expression = re.sub(r'ceil\(', 'np.ceil(', expression)  
        return expression

    def calculate(self):
        parameters = self.to_dict()
        total_area = 0
        num_rectangles = int(parameters['length'] / parameters['delta_x'])

        for i in range(num_rectangles):
            x = parameters['a'] + (i * parameters['delta_x'])
            expression = self.get_function_expression(x)

            try:
                height = eval(expression, {"x": x, "np": np})
                area = parameters['delta_x'] * height
                total_area += area 
            except Exception as e:
                raise ValueError(f"Error evaluating function at x={x}: {e}")

        return '{:.2f}'.format(total_area)

    def graph(self):
        parameters = self.to_dict()
        x_vals = np.linspace(parameters['a'], parameters['b'], 1000)
        y_vals = []

        for x in x_vals:
            expression = self.get_function_expression(x)

            try:
                y_val = eval(expression, {"x": x, "np": np})
                y_vals.append(y_val)
            except Exception as e:
                raise ValueError(f"Error evaluating function for graphing at x={x}: {e}")

        plt.plot(x_vals, y_vals, label='f(x)',)
        plt.fill_between(x_vals, y_vals, where=((x_vals >= parameters['a']) & (x_vals <= parameters['b'])), alpha=0.3)
        plt.title(f'The surface area enclosed by the graph of the function and the bounds from {parameters["a"]} to {parameters["b"]}')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.axhline(0, color='black', lw=0.5, ls='--')
        plt.axvline(parameters['a'], color='red', lw=1.5, ls='--', label='Lower Bound')
        plt.axvline(parameters['b'], color='green', lw=1.5, ls='--', label='Upper Bound')
        plt.legend()
        plt.grid()
        plt.show()


try:
    function_expression = str(input('Enter function expression (e.g., x**2): '))
    lower_bound = input('Enter lower bound: ')
    upper_bound = input('Enter upper bound: ')

    lower_bound = lower_bound.replace('pi', '3.14').replace('e', '2.71')
    upper_bound = upper_bound.replace('pi', '3.14').replace('e', '2.71')
    lower_bound = float(lower_bound)
    upper_bound = float(upper_bound)

    integral = DefiniteIntegral(function_expression, lower_bound, upper_bound)
    print('The answer: ', integral.calculate())
    integral.graph()

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")