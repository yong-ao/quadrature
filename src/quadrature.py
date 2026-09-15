def trapezoid(f, a, b, n):
    """Approximate the integral of f over [a, b] using n equal subintervals."""
    h = (b - a) / n
    s = (f(a) + f(b)) / 2
    for i in range(1, n):
        s += f(a + i*h)
    return h * s
