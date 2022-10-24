import matplotlib.pyplot as plt 
import numpy as np

class ODE_Euler_N:
  """A class to compute the time evoluation of a population of multiple
     species using the Euler method. Contains variables which store
     the current population as well as a history.  You need to
     implement the function F(self, t, V) in a subclass in order to
     use this class.
  """

  def __init__(self, V0=np.array([], dtype='float64'), dt=0.001, t0=0):
      """ Set the variables used by the class:

      : param V0 : initial value (as an array or a list) 
      : param dt : integration time step
      : param t0 : initial time
      """
      self.reset(V0, dt=dt, t0=t0);
      
  def reset(self, V0, dt=0.001, t0=0):
      """ Reset the integration parameters : 

      : param V0 : initial value (as an array or a list) 
      : param dt : time step
      : param t0 : initial time
      """
      self.V = np.array(V0, dtype='float64') # ensure we use floats!
      self.t = t0
      self.dt = dt
      self.t_list = []
      self.V_list = []
      
  def F(self, t, V):
      """ Return the right hand side of the equation dV/dt = F(t,V)

      : param t  : current time
      : param V0 : current function values
      : return : the right hand side of the equation at time t
      """
      pass

  def one_step(self):
      """ Performs a single integration step using the Euler method.
      """
      self.V += self.dt*self.F(self.t, self.V)
      self.t += self.dt
    
  def iterate(self, tmax, fig_dt=-1):
      """ Solve the system of equations DN/dt = F(N)  until tmax
          Save N and t in lists N_list and t_list every fig_dt

      : param tmax   : integration upper bound
      : param fig_dt : interval between data point for figures (use dt if < 0)
      """
       
      if(fig_dt < 0) : fig_dt = self.dt*0.99 # Save all data
      
      next_fig_t = self.t*(1-1e-15) # Ensure we save the initial values
      
      tmax -= self.dt*0.1         # Stop as close to tmax as possible
      while(self.t < tmax):       # Integrate until tmax
        self.one_step()
        if(self.t >= next_fig_t): # Save fig when next_fig_t is reached       
          self.V_list.append(np.array(self.V)) # force a copy of V!
          self.t_list.append(self.t)
          next_fig_t += fig_dt    # Set the next figure time

  def plot(self, i, j=0, style="k-"):
    """ plot V[i] versus t    (i > 1 and j = 0)  using style
        plot V[i] versus V[j] (i > 1 and j > 1)  using style
        plot t    versus V[j] (i = 0 and j > 1)  using style

      : param i    : index of function for y-axis 
      : param j    : index of function for x-axis
      : param style: style string for the plot function
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


# Only run this when not importing the module.

if __name__ == "__main__":
    class EulerNTest(ODE_Euler_N):
        def F(self, t, V):
          """Example below:  
             du/dt = v; 
             dv/dt = -u.
          """
          u = V[0]
          v = V[1]
          return(np.array([v, -u]))
        
    pop = EulerNTest(V0=[1.0,0.0], dt=0.001, t0=0)
    pop.iterate(tmax=10, fig_dt=0.1)
    pop.plot(1, 0, "r-")          # Plot u(t) in red
    pop.plot(2, 0, "b-")          # Plot v(t) in blue
    plt.show()                    # Show the 2 curves on the same figure
    pop.plot(1, 2, "g-")          # Plot u(v) in green
    plt.axis('equal')             # Ensures a square is shown as a square
    plt.margins(0.1, 0.1)         # add extra space on the edges
    plt.show()                    # Show the trajectory
  


