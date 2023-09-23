import sympy as sym

def get_cdf(pdf, lower_bound=0, upper_bound=infty):
  return sym.integrate(pdf, (x, lower_bound, upper_bound))

def inverse_cdf(pdf, lower_bound=0, upper_bound=infty):
  cdf = get_cdf(pdf, lower_bound=lower_bound, upper_bound=upper_bound)
  eq = sym.Eq(cdf, u)
  return sym.latex(sym.solve(eq, x))
