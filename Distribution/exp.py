import numpy as np
from unif import runif
from constants import *

def dexp(x, rate = 1, log = FALSE):
  """
    f(X=x) = ue^-(u*x), u > 0, x > 0
  """
  return rate*np.exp(-rate*x)

def pexp(q, rate = 1, lower_tail = TRUE, log_p = FALSE):
  """
    f(X <= x) = 1 - e^(-u*x)
  """
  return 1 - np.exp(-rate*q)

def qexp(p, rate = 1, lower_tail = TRUE, log_p = FALSE):
  """
    Solve \int^x_0 u*e^(-u*x) dx = p for lowerTail=T
  """
  return -np.log(1-p)/rate

def rexp(n, rate = 4):
  """
    X ~ exp(u), u > 0, x > 0
  """
  return -np.log(runif(n))/rate

def eexp(rate=1):
  """
    E(X) = 1/u
  """
  1/rate

def vexp(rate=1):
  """
    V(X) = 1/u**2
  """
  1/rate**2