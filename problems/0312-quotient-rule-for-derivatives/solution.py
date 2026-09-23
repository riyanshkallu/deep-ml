import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """

    g_len = len(g_coeffs)
    h_len = len(h_coeffs)

    g = 0
    h = 0
    g_deriv = 0
    h_deriv = 0


    for num in range(g_len):
        g += g_coeffs[num]*(x**(g_len-num))
        g_deriv += g_coeffs[num] * (g_len-num) * (x**(g_len-num-1))

    for num in range(h_len):
        h += h_coeffs[num]*(x**(h_len-num))
        h_deriv += h_coeffs[num] * (h_len-num) * (x**(h_len-num-1))

    if h == 0:
        return -1
        
    return ((h*g_deriv)-(g*h_deriv))/(h**2)


    # Your code here
    pass