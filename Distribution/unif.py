import numpy as np
from constants import *

def dunif(x, min = 0, max = 1, log = FALSE):
  """
    P(X=x) = 1/(b-a)
  """
  p_x = 1/(max-min)
  if log: return np.log(p_x)
  return p_x

def punif(q, min = 0, max = 1, lower_tail = TRUE, log_p = FALSE):
  """
    P(X <= x) = (x-a)/(b-a)
  """
  PX_x = (q-min) / (max-min)
  PX_x = PX_x if lower_tail else (1 - PX_x)
  PX_x = np.log(PX_x) if log_p else PX_x
  return PX_x,

def qunif(p, min = 0, max = 1, lower_tail = TRUE):
  """
    Solve \int^x_a 1/(b-a) dx = p for lowerTail=T
    or \int^b_x 1/(b-a) = 1 - p
  """
  if lower_tail:
    x = p*(max-min) + min
  else: 
    p = 1-p
    x = max - p*(max-min)
  return x

def runif(n, min=0,max=1):
  """
    X ~ U(a,b); a <= b
  """
  return np.array([np.random.uniform(min,max), for i in range(n)])

def eunif(min=0,max=1):
  """
    E(x) = (a+b) / 2
  """
  return (min+max)/2

def vunif(min=0,max=1):
  """
    V(x) = (b-a)**2/12
  """
  return (max-min)**2/12