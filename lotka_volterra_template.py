import matplotlib.pyplot as plt 
import numpy as np
from ode_euler_N import ODE_Euler_N

class LotkaVolterra(ODE_Euler_N):

    def __init__(self, V0=np.array([], dtype='float64'), dt=0.001, t0=0, K=0):
        """ Initialiser: set all the parameter for the integration
        : param V0  : initial value of NV
        : param dt : integration time step
        : param t0 : initial time (usualy 0)
        : param K  : equation parameter value (default is 0)
        """
        super().__init__(V0, dt=dt, t0=t0)
        self.K = K
        
    def F(self, t, V):
        """ Equation dN/dt = F(t,V)
        : param t : current value of integration variable t
        : param V : current value of function (N, P)
        : return : the value of the right hand side of the equation at time t
        """
        N = V[0]
        P = V[1]
        ### TO DO

      
# Only run this when not importing the module.

if __name__ == "__main__":
   lv = LotkaVolterra(V0=[0.1,0.1], dt=0.001, K=1)
   lv.iterate(40, 0.01)
   lv.plot(1,0, "r-")
   lv.plot(2,0, "b-")
   plt.legend(['Preys', 'Predators'])   
   plt.show()
   lv.plot(1,2,"g-")
   plt.axis('equal')
   plt.margins(0.1, 0.1) 
   plt.xlabel('Preys')
   plt.ylabel('Predators')
   plt.show()
  
