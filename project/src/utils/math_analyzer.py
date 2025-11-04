import sympy as sp
from sympy import symbols, diff, integrate, simplify


class MathAnalyzer:
    def __init__(self):
        """Initialize mathematical analyzer."""
        pass
    
    def symbolic_analysis(self, expression_str):
        """
        Perform symbolic mathematical analysis.
        
        Args:
            expression_str: String representation of mathematical expression
            
        Returns:
            Dictionary with original, derivative, and integral
        """
        try:
            x = symbols('x')
            expr = sp.sympify(expression_str)
            
            derivative = diff(expr, x)
            integral = integrate(expr, x)
            
            return {
                'original': str(expr),
                'derivative': str(simplify(derivative)),
                'integral': str(simplify(integral)),
                'simplified': str(simplify(expr))
            }
        except Exception as e:
            return {
                'error': str(e),
                'original': expression_str
            }
    
    def evaluate_expression(self, expression_str, variable_values):
        """
        Evaluate expression with given variable values.
        
        Args:
            expression_str: String representation of expression
            variable_values: Dictionary of variable names to values
            
        Returns:
            Numeric result
        """
        try:
            expr = sp.sympify(expression_str)
            result = expr.subs(variable_values)
            return float(result.evalf())
        except Exception as e:
            return {'error': str(e)}
    
    def solve_equation(self, equation_str):
        """
        Solve symbolic equation.
        
        Args:
            equation_str: String representation of equation (e.g., "x**2 - 4")
            
        Returns:
            List of solutions
        """
        try:
            x = symbols('x')
            expr = sp.sympify(equation_str)
            solutions = sp.solve(expr, x)
            return [str(sol) for sol in solutions]
        except Exception as e:
            return {'error': str(e)}

