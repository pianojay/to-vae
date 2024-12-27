from random import *
import numpy as np
import os

from topopt_cholmod import main
from bc_options import *
from csv2fig import csv2fig

def createFolder(directory): # unused in this scope
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

if __name__ == "__main__":
    # Default input parameters
    nelx, nely = 64, 32
    volfrac_l, rmin = [0.2, 0.4, 0.6, 0.8], 2.0    # 5.4; TODO: adaptive filter radius? (x0.04?)
    penal, ft = 3.0, 1          # ft==0 -> sens, ft==1 -> dens

    for volfrac in volfrac_l:
        for bc in [Simple]:
            # FixFix is not working at any load-case. Hm...
            for side in [3]:
                test = bc(nelx, nely, side)

                dirname = f"{volfrac}_{test.dirname}"
                createFolder(dirname)
                print(f"Testing for {dirname}:")
                print(f"Minimum compliance problem with OC; {['Sensitivity based','Density based'][ft]}")
                print(f"ndes: {nelx} x {nely}, {volfrac=}, {rmin=}, {penal=}")

                # iterate over varying load condition

                for loadpoint in test.loadpoints():
                    num = 8
                    for theta_i, theta in enumerate(list(np.linspace(0, 2*np.pi, num=num, endpoint=False))):
                        try:
                            main(nelx, nely, volfrac, penal, rmin, ft, test.fixed, test.lp2f(loadpoint, theta), dirname, loadpoint, theta_i, num)
                        except:
                            continue

                # plot created results neatly
                try:
                    csv2fig(dirname, dirname+"/thetatest", False)
                except:
                    continue
    