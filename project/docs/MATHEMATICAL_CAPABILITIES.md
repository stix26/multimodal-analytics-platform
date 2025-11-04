# 🧮 Mathematical Analysis Capabilities

## Comprehensive Function Support

The AI-Powered Multi-Modal Analytics Platform provides professional-grade symbolic mathematics powered by **SymPy**, supporting calculus operations including derivatives, integrals, simplification, and equation solving.

### ✅ **Supported Function Types**

#### 1. **Polynomial Functions**
```python
# Examples
"x**4 - 3*x**3 + 2*x**2 - x + 5"
"(x + 1)**3"  # Expands to x**3 + 3*x**2 + 3*x + 1

# Results
✅ Derivative: 4*x**3 - 9*x**2 + 4*x - 1
✅ Integral: x*(12*x**4 - 45*x**3 + 40*x**2 - 30*x + 300)/60
```

#### 2. **Trigonometric Functions**
```python
# Examples
"sin(x) + cos(x) + tan(x)"
"sin(x)**2 + cos(x)**2"  # Simplifies to 1

# Results
✅ Derivative: sqrt(2)*cos(x + pi/4) + cos(x)**(-2)
✅ Integral: -log(cos(x)) - sqrt(2)*cos(x + pi/4)
```

#### 3. **Exponential & Logarithmic Functions**
```python
# Examples
"exp(x) + log(x) + x*exp(-x)"
"log(x**2) + exp(2*x)"

# Results
✅ Derivative: -x*exp(-x) + exp(x) + exp(-x) + 1/x
✅ Integral: Complex expression with exponential integrals
```

#### 4. **Hyperbolic Functions**
```python
# Examples
"sinh(x) + cosh(x) + tanh(x)"
"sech(x) + csch(x)"

# Results
✅ Derivative: sinh(x) + cosh(x) + cosh(x)**(-2)
✅ Integral: x - log(tanh(x) + 1) + sinh(x) + cosh(x)
```

#### 5. **Inverse Trigonometric Functions**
```python
# Examples
"asin(x) + acos(x) + atan(x)"
"atan2(y, x)"  # Two-argument arctangent

# Results
✅ Derivative: 1/(x**2 + 1)  # Note: asin + acos derivatives cancel
✅ Integral: x*acos(x) + x*asin(x) + x*atan(x) - log(x**2 + 1)/2
```

#### 6. **Radical Functions**
```python
# Examples
"sqrt(x) + x**(1/3) + sqrt(x**2 + 1)"
"sqrt(x**2 - 1) + cbrt(x)"

# Results
✅ Derivative: x/sqrt(x**2 + 1) + 1/(2*sqrt(x)) + 1/(3*x**(2/3))
✅ Integral: Includes asinh(x) and power functions
```

#### 7. **Rational Functions**
```python
# Examples
"(x**2 + 1) / (x**2 - 1)"
"1 / (x**2 + 1)"

# Results
✅ Derivative: -4*x/(x**2 - 1)**2
✅ Integral: x + log(x - 1) - log(x + 1)  # Partial fractions
```

#### 8. **Composite Functions**
```python
# Examples
"sin(x**2) + exp(cos(x)) + log(sqrt(x))"
"exp(sin(x)) + ln(cos(x**2))"

# Results
✅ Derivative: 2*x*cos(x**2) - exp(cos(x))*sin(x) + 1/(2*x)
✅ Integral: May include special functions (Fresnel integrals, etc.)
```

#### 9. **Absolute Value Functions**
```python
# Examples
"abs(x) + abs(x**2 - 4)"
"abs(sin(x))"

# Results
✅ Derivative: Piecewise expressions with conditions
✅ Integral: Often requires piecewise integration
```

#### 10. **Multivariable Functions**
```python
# Examples
"x**2 + y**2 + x*y"
"sin(x) * cos(y) + exp(x*y)"

# Results
✅ Partial derivatives with respect to default variable (x)
✅ Integration treats other variables as constants
```

### 🔧 **Advanced Features**

#### Equation Solving
```python
# Available via solve_equation method
solve_equation("x**2 - 4")  # Returns [-2, 2]
solve_equation("sin(x)")    # Returns [0, pi, 2*pi, ...]
```

#### Expression Evaluation
```python
# Available via evaluate_expression method
evaluate_expression("x**2 + 1", {"x": 3})  # Returns 10
```

#### Simplification
```python
# Automatic simplification
"x**2 + 2*x + 1"     # May factor to (x+1)**2
"sin(x)**2 + cos(x)**2"  # Simplifies to 1
"exp(log(x))"        # Simplifies to x
```

### ⚡ **Performance Guidelines**

#### ✅ **Fast Operations**
- Polynomials (any degree)
- Basic trigonometric expressions
- Simple exponential/logarithmic functions
- Rational functions with polynomial numerator/denominator

#### ⚠️ **Moderate Speed**
- Composite functions (2-3 levels deep)
- Hyperbolic and inverse functions
- Multi-term mixed expressions

#### 🐌 **Slower Operations**
- Deeply nested composite functions
- Complex absolute value expressions
- Special functions (gamma, factorial)
- Very high-degree polynomials (>10)

### 📝 **Syntax Guide**

| Mathematical Notation | SymPy Syntax | Example |
|---|---|---|
| x² | `x**2` | `x**2 + 1` |
| √x | `sqrt(x)` | `sqrt(x**2 + 1)` |
| eˣ | `exp(x)` | `exp(-x**2)` |
| ln(x) | `log(x)` | `log(x + 1)` |
| sin⁻¹(x) | `asin(x)` | `asin(x/2)` |
| |x| | `abs(x)` | `abs(x - 1)` |
| π | `pi` | `sin(pi*x)` |
| ∞ | `oo` | `limit(1/x, x, oo)` |

### 🎯 **Example API Usage**

```bash
# Basic polynomial
curl -X POST -H "Content-Type: application/json" \
  -d '{"expression": "x**3 + 2*x**2 - x + 1"}' \
  http://127.0.0.1:5000/api/math

# Complex trigonometric
curl -X POST -H "Content-Type: application/json" \
  -d '{"expression": "sin(x)*cos(x) + tan(x**2)"}' \
  http://127.0.0.1:5000/api/math

# Mixed functions
curl -X POST -H "Content-Type: application/json" \
  -d '{"expression": "exp(x) * log(x) + sqrt(x**2 + 1)"}' \
  http://127.0.0.1:5000/api/math
```

### 🚀 **Professional Applications**

This mathematical engine supports:
- **Engineering calculations** (control systems, signal processing)
- **Physics modeling** (mechanics, electromagnetics, quantum)
- **Economics/Finance** (optimization, derivatives pricing)
- **Data science** (statistical distributions, curve fitting)
- **Machine learning** (activation functions, loss functions)

---

**The platform provides university-level symbolic mathematics comparable to Mathematica, Maple, or advanced graphing calculators.**
