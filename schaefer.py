#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:37:35 2022

@author: zaccheuslines
"""

from ode_euler import ODE_Euler

class Schaefer(ODE_Euler):
    
    def __init__(self, N, dt, t0, Y):
        
        super().__init__(N,dt=dt,t0=t0)
        self.Y = Y
    
    def F(self, t, N):
        
        return N*(1-N)-self.Y


if __name__ == "__main__":
    pop = Schaefer(0.25, t0=0,dt=0.01,Y=0.19)
    pop.iterate(20) # We perform 20 steps of integration
    pop.plot()      # and display the result

        
