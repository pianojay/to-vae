from random import *
import numpy as np
import os

# node 인덱스 리스트를 바탕으로 dof 인덱스를 줌.
def xdof(l):
    return np.array([_*2 for _ in l])

def ydof(l):
    return np.array([_*2+1 for _ in l])

def xydof(l):
    return np.array([_ for __ in l for _ in (__*2, __*2+1)])

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory @ {directory}")
    except OSError:
        print ('Error: Creating directory. ' +  directory)


### Mother class for all structures defined by some fixed boundary conditions
class BC_mom():
    def __init__(self, nelx, nely):
        self.nelx = nelx
        self.nely = nely
        self.ndof = 2*(nelx+1)*(nely+1)
        self.dofs = np.arange(self.ndof)
        self.f = np.zeros((self.ndof, 1))


### cantilever beam
# Left fixed, point load at right
class Cantilever(BC_mom):
    def __init__(self, nelx, nely):
        super().__init__(nelx, nely)
        self.name = "Cantilever"
        self.dirname = f"{self.name}_{nelx}x{nely}"
        createFolder(self.dirname)
        self.fixed = np.sort(xydof(self.dofs[0:self.nely+1]))

    def loadpoints(self):
        for _ in range(self.nelx*(self.nely+1), (self.nelx+1)*(self.nely+1)): yield _

    def lp2f(self, loadpoint):
        ff = self.f.copy()
        ff[*ydof([loadpoint]), 0] = -1
        return ff


### Simply supported beam
# Two bottom end point supported (pinned left, roller support right)
# Point load on top
class SimplySupported(BC_mom):
    def __init__(self, nelx, nely):
        super().__init__(nelx, nely)
        self.name = "SimpleSupport"
        self.dirname = f"{self.name}_{nelx}x{nely}"
        createFolder(self.dirname)
        self.fixed = np.sort(np.concatenate((xydof([nely]), ydof([(nelx+1)*(nely+1)-1]))))

    def loadpoints(self):
        for _ in range(0, self.nelx*(self.nely+1)+1, self.nely+1): yield _

    def lp2f(self, loadpoint):
        ff = self.f.copy()
        ff[*ydof([loadpoint]), 0] = -1
        return ff


### Bridge structure
# Two bottom end point fixed (not supported)
# Point load on top
class Bridge(BC_mom):
    def __init__(self, nelx, nely):
        super().__init__(nelx, nely)
        self.name = "Bridge"
        self.dirname = f"{self.name}_{nelx}x{nely}"
        createFolder(self.dirname)
        self.fixed = np.sort(np.concatenate((xydof([nely]), xydof([(nelx+1)*(nely+1)-1]))))

    def loadpoints(self):
        for _ in range(0, self.nelx*(self.nely+1)+1, self.nely+1): yield _

    def lp2f(self, loadpoint):
        ff = self.f.copy()
        ff[*ydof([loadpoint]), 0] = -1
        return ff


### MBB beam (half of simply supported beam)
# Left wall supported, right end supported
# Point load on top
class MBB(BC_mom):
    def __init__(self, nelx, nely):
        super().__init__(nelx, nely)
        self.name = "MBB"
        self.dirname = f"{self.name}_{nelx}x{nely}"
        createFolder(self.dirname)
        self.fixed = np.sort(np.concatenate((xdof(self.dofs[0:nely+1]), ydof([(nelx+1)*(nely+1)-1]))))

    def loadpoints(self):
        for _ in range(0, self.nelx*(self.nely+1)+1, self.nely+1): yield _

    def lp2f(self, loadpoint):
        ff = self.f.copy()
        ff[*ydof([loadpoint]), 0] = -1
        return ff


### Michell (point-supported cantilever beam)
class Michell(BC_mom):
    def __init__(self, nelx, nely):
        super().__init__(nelx, nely)
        self.name = "Michell"
        self.dirname = f"{self.name}_{nelx}x{nely}"
        createFolder(self.dirname)
        self.fixed = np.sort(xydof([0, nely]))

    def loadpoints(self):
        for _ in range(self.nelx*(self.nely+1), (self.nelx+1)*(self.nely+1)): yield _

    def lp2f(self, loadpoint):
        ff = self.f.copy()
        ff[*ydof([loadpoint]), 0] = -1
        return ff



"""
# 이렇게 보니까 빔+로드 1개로만 해도 참 다양하게 나온다.

### L Bracket
### Plate With a hole
### Hook Shaped
### Half Wheel
### S shaped

# Discrete Loads: (as in floors of a building)

### Frame structure
# Fixed Left
# normal load at right
fixed = np.sort(xydof(dofs[0:nely+1]))
loadpoint = randrange(nelx*(nely+1), (nelx+1)*(nely+1))
f[*xdof([loadpoint]), 0]=-1


### Column with distributed load
# Fixed Left
# distributed normal load
### Pressure Vessel?
### Custom


#### 구조의 종류
# Beams (+ MBB)
# Michell Structures (only corners)
# Frame/Columns

# Passive elements? (empty/filled contrains)"""