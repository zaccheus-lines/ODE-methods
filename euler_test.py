from ode_euler import ODE_Euler

class EulerTest(ODE_Euler):
    
    def __init__(self, N, dt, t0=0, R=-1):
        """ Initialiser: set all the parameter for the integration
        : param N  : initial value of N 
        : param dt : integration time step
        : param t0 : initial time (usualy 0)
        : param R  : equation parameter value (default is -1)
        """
        super().__init__(N, dt=dt, t0=t0)
        self.R = R

    def F(self, t, N):
        """ The right hand side of the equation dN/dt = R*N
        : param t : current value of integration variable t
        : param N : current value of function N
        : return : the value of the right hand side of the equation at time t
        """
        return self.R*N

if __name__ == "__main__":
    pop = EulerTest(0.01, dt=0.01) # R takes the default value: -1
    pop.R = -0.5    # We change the value of R
    pop.iterate(10) # We perform 10 steps of integration
    pop.plot()      # and display the result

    # Another way to do the same
    pop2 = EulerTest(0.01, dt=0.01, t0=0, R=-0.5) # Set R value
    pop2.iterate(20) # We perform 20 steps of integration
    pop2.plot("r-")  # and display the result in red this time
    
