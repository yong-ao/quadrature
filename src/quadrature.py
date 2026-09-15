def trapezoid(f, a, b, n):
    """Approximate the integral of f over [a, b] using n equal subintervals."""
    h = (b - a) / n
    s = (f(a) + f(b)) / 2
    for i in range(1, n):
        s += f(a + i*h)
    return h * s

# this is a test

def simpson(f, a, b, n):
    """Approximate the integral of f over [a, b] using Simpson's rule.

    n must be even.
    """
    if n % 2 != 0:
        raise ValueError("simpson requires an even number of subintervals")
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 == 1 else 2) * f(a + i*h)
    return h * s / 3
