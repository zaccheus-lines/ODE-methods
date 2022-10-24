import matplotlib.pyplot as plt 
import numpy as np
from ode_rk4 import ODE_RK4
from lotka_volterra import LotkaVolterra
from lotka_volterra_rk4 import LotkaVolterraRK4


# Compare accuracy of Euler and RK4 integration method
# Compute a reference solution using RK4 and a small dt
tmax=1
lv = LotkaVolterraRK4(V0=[0.1,0.1],dt=1e-5)  # Create a RK4 LV object
lv.K = 1                  # Set the parameter
lv.iterate(tmax, 0.1)     # Compute reference value
V_ref = lv.V              # Make copy of reference function values 
print("REF: t="+str(lv.t))

lve = LotkaVolterra()     # LV for Euler method
lve.K = 1

# Scan a range of integration time steps
for dt in [0.2, 0.1, 0.05, 0.02, 0.01] :
  lv.reset(V0=[0.1,0.1], dt=dt) # Solve LV using RK4
  lv.iterate(tmax,0.1)
  V = lv.V
  print("RK4 : dt="+str(dt)+": Error =", np.sqrt((V_ref-V).dot(V_ref-V))) 
  #print("t="+str(lv.t))
  lve = LotkaVolterra(V0=[0.1,0.1], dt=dt) # Solve LV using Euler
  lve.K = 1               
  lve.iterate(tmax,0.1)
  V = lve.V
  # Compare the errors using V_ref as reference solution
  print("Euler dt="+str(dt)+": Error =", np.sqrt((V_ref-V).dot(V_ref-V))) 
  #print("t="+str(lv.t))
  print("")
