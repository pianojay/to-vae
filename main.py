from random import *
import numpy as np
import os

from topopt_cholmod import main
from bc_options import *
from csv2fig import csv2fig

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

if __name__ == "__main__":
    # Default input parameters
    nelx, nely = 96, 32
    volfrac, rmin = 0.4, 2.0    # 5.4; TODO: adaptive filter radius? (x0.04?)
    penal, ft = 3.0, 1          # ft==0 -> sens, ft==1 -> dens

    for bc in [Simple, Bridge, Cantil, CantilProp, FixFix, MBB, MBeamHalf, MBeamFull, MTruss]:
        # FixFix is not working at any load-case. Hm...
        for side in [0, 1, 2, 3]:
            test = bc(nelx, nely, side)
            
            dirname = test.dirname
            print(f"Testing for {dirname}:")
            print(f"Minimum compliance problem with OC; {['Sensitivity based','Density based'][ft]}")
            print(f"ndes: {nelx} x {nely}, {volfrac=}, {rmin=}, {penal=}")

            # iterate over varying load condition

            for loadpoint in test.loadpoints():
                try:
                    main(nelx, nely, volfrac, penal, rmin, ft, test.fixed, test.lp2f(loadpoint), dirname, loadpoint)
                except:
                    continue

            # plot created results neatly
            try:
                csv2fig(dirname, dirname, False)
            except:
                continue
    