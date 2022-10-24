import matplotlib.pyplot as plt 
import numpy as np

class ODE_Euler:
  """A class to compute the time evolution of a population using the
     Euler method. Contains variables which store the current
     population as well as a history.  You need to implement the
     function F(self, t, N) in a subclass in order to use this class.
  """

  def __init__(self, N=0, dt=0.001, t0=0):
      """ Initialise and set the parameters for an ODE integration.
        : param N  : initial population.
        : param dt : integration time step.
        : param t0 : initial time.
      """
      self.reset(N, dt=dt, t0=t0)
      
  def reset(self, N, dt, t0=0):
      """ Reset the integration parameters; see __init__ for more info.
        : param N  : initial population.
        : param dt : integration time step.
        : param t0 : initial time.
      """
      self.N  = N
      self.dt = dt
      self.t  = t0
      self.t_list = []   # to store t values for plots 
      self.N_list = []   # to store N values for plots 

  def F(self, t, N):
      """ Return the value of dN/dt = F(t,N). You need to implement this
          in a subclass. 
        : param t : current value of integration variable t
        : param N : current value of function N
        : return : the value of the right hand side of the equation at time t
      """
      pass
       
  def one_step(self):
      """ Perform a single integration step using the Euler method.
      """

      self.N += self.dt*self.F(self.t, self.N)
      self.t += self.dt

  def iterate(self, tmax):
      """ Solve the equation dN(t)/dt = F(N(t))  until time tmax.
          Update N, t and append all values to N_list and t_list.
        : param tmax : upper bound of integration.
      """

      while(self.t < tmax):
        self.one_step()
        self.N_list.append(self.N)
        self.t_list.append(self.t)

  def plot(self, style='b-'):
      """ Display function N(t).
        : param style: matplotlib style string for the plot.
      """
      plt.plot(self.t_list, self.N_list, style)
      plt.show()


# Tests for this module; only run when not importing the module.

if __name__ == "__main__":
   # Implement a concrete ODE to solve
   class EulerTest(ODE_Euler):
      def __init__(self, N, dt, t0, R):
          super().__init__(N, dt=dt, t0=t0)
          self.R=R
          
      def F(self, t, N):
          return self.R*N

   pop = EulerTest(0.01, dt=0.01, t0=0, R=-0.5)
   pop.iterate(10)
   pop.plot()
   


