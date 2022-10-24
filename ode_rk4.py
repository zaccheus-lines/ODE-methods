import matplotlib.pyplot as plt 
import numpy as np

class ODE_RK4:
  """ A class to compute the time evolution of a population using the
      fourth order Runge-Kutta method.
  """

  def __init__(self, V0=[0], dt=0.1, t0=0 ):
      """ Set the variables used by the class:

      :param V0 : initial value (as an array or a list) 
      :param dt : integration time step
      :param t0 : initial time
      """
      self.reset(V0, dt=dt, t0=t0)
      
  def reset(self, V0, dt, t0=0):
      """ Reset the integration parameters; see __init__ for more info."""

      self.V  = np.array(V0, dtype='float64') # Ensure we use floats!
      self.dt = dt
      self.t  = t0
      self.t_list = [] # To store t values for plots
      self.V_list = [] # To store f values for plots
      
  def F(self, t, V):
      """ Return the right hand side of the equation dV/dt = F(t,V)."""
      pass

  def one_step(self):
      """ Perform a single integration step of the 4th order Runge Kutta method."""

      k1 = self.F(self.t, self.V)
      K = self.V+0.5*self.dt*k1

      k2 = self.F(self.t+0.5*self.dt, K)
      K = self.V+0.5*self.dt*k2

      k3 = self.F(self.t+0.5*self.dt, K)
      K = self.V+self.dt*k3
 
      k4 = self.F(self.t+self.dt, K)
      # self.v -> v(t+dt)
      self.V += self.dt/6.0*(k1+2.0*(k2+k3)+k4)
      # t -> t + dt
      self.t += self.dt
    
  def iterate(self, tmax, fig_dt=-1):
      """ Solve the system of equations DN/dt = F(N) until t=tmax.
          Save N and t in lists N_list and t_list every fig_dt.

      :param tmax   : integration upper bound
      :param fig_dt : interval between data point for figures (use dt if < 0)
      """
       
      if(fig_dt < 0) : fig_dt = self.dt*0.99 # Save all data
      
      next_fig_t = self.t*(1-1e-15) # Ensure we save the initial values

      tmax -= self.dt*0.01        # Stop as close to tamx as possible
      while(self.t < tmax):       # Integrate until tmax
        self.one_step()
        if(self.t >= next_fig_t): # Save fig when next_fig_t is reached       
          self.V_list.append(np.array(self.V)) # force a copy of V!
          self.t_list.append(self.t)
          next_fig_t += fig_dt    # Set the next figure time

  def plot(self, i, j=0, style="k-"):
      """ plot V[i] versus t    (i > 1 and j = 0)  using format
          plot V[i] versus V[j] (i > 1 and j > 1)  using format
          plot t    versus V[j] (i = 0 and j > 1)  using format

      :param i : index of function for abscissa 
      :param j : index of function for ordinate
      :param format : format for the plot function
      """

      if(j==0):
        lx = self.t_list
      else: # Extra item i-1 from each element of f_list
        lx = list(map (lambda v : v[j-1] , self.V_list))
      if(i==0):
        ly = self.t_list
      else:
        ly = list(map (lambda v : v[i-1] , self.V_list))
      plt.plot(lx, ly, style);


# Tests for this module; only run when not importing the module.
      
if __name__ == "__main__":
   class RK4Test(ODE_RK4):
     def F(self, t, V):
         """ Sample of two ODEs: du/dt = v; dv/dt = -u. """
         return(np.array([self.V[1], -self.V[0]]))
            
   pop = RK4Test(V0=[1.0, 0.0], dt=0.001)
   pop.iterate(10, 0.1)
   pop.plot(1,0, "r-")
   pop.plot(2,0, "b-")
   plt.show()
   pop.plot(1,2, "g-")
   plt.axis('equal')
   plt.margins(0.1, 0.1) 
   plt.show()
  


