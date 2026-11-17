from random import *
import numpy as np
import os

# node 인덱스 리스트를 바탕으로 dof 인덱스를 줌.
def xdof(l): return np.array([_*2 for _ in l])
def ydof(l): return np.array([_*2+1 for _ in l])
def xydof(l): return np.array([_ for __ in l for _ in (__*2, __*2+1)])

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory @ {directory}")
    except OSError:
        print ('Error: Creating directory. ' +  directory)

def loadpoints(nelx, nely, side):
    # right, top, left, bottom
    if side == 0:
        for _ in range(nelx*(nely+1), (nelx+1)*(nely+1)): yield _
    elif side == 1:
        for _ in range(0, nelx*(nely+1)+1, nely+1): yield _
    elif side == 2:
        for _ in range(0, nely+1): yield _
    elif side == 3:
        for _ in range(nely, (nelx+1)*(nely+1), nely+1): yield _

def lp2f(f, loadpoint, theta=0):
    # load point to f vector; for vertical down load.
    # f[*ydof([loadpoint]), 0] = -1
    # then how about load point to f vector, but a load  with a theta?
    # theta would be considered as a new method of understanding the world.
    f[*ydof([loadpoint]), 0] = -np.cos(theta)
    f[*xdof([loadpoint]), 0] = -np.sin(theta)
    # then the theta represents:
    """________
          /|
         / |
        /  v
       <-theta
    """
    return f


### Mother class
class BC_mom():
    """Mother class for all structures defined by fixed dofs.
    """
    def __init__(self, nelx, nely, side):
        self.nelx = nelx
        self.nely = nely
        self.side = side
        self.ndof = 2*(nelx+1)*(nely+1)
        self.dofs = np.arange(self.ndof)
        self.f = np.zeros((self.ndof, 1))

        self.name = self.__class__.__name__
        self.dirname = f"{self.name}_{nelx}x{nely}_{side}"
        createFolder(self.dirname)

    def loadpoints(self): return loadpoints(self.nelx, self.nely, self.side)
    def lp2f(self, loadpoint, theta=0): return lp2f(self.f.copy(), loadpoint, theta)


### Beams:
class Simple(BC_mom):
    """Simply supported beam; Pinned left, Supported right, Point load on top
    """
    def __init__(self, nelx, nely, side):
        super().__init__(nelx, nely, side)
        self.fixed = np.sort(np.concatenate((xydof([nely]), ydof([(nelx+1)*(nely+1)-1]))))


class Bridge(BC_mom):
    """Bridge structure; Pinned left, Pinned right, Point load on top
    """
    def __init__(self, nelx, nely, side):
        super().__init__(nelx, nely, side)
        self.fixed = np.sort(np.concatenate((xydof([nely]), xydof([(nelx+1)*(nely+1)-1]))))


class Cantil(BC_mom):
    """Cantiliever beam; Left fixed, point load at right
    """
    def __init__(self, nelx, nely, side):
        super().__init__(nelx, nely, side)
        self.fixed = np.sort(xydof(self.dofs[0:nely+1]))


class CantilProp(BC_mom):
    """Propped Cantiliver; Fixed left, Supported right"""
    def __init__(self, nelx, nely, side):
        super().__init__(nelx, nely, side)
        self.fixed = np.sort(np.concatenate((xydof(self.dofs[0:nely+1]), ydof([(nelx+1)*(nely+1)-1]))))


class FixFix(BC_mom):
    """Fixed-Fixed Cantilever beam
    """
    def __init__(self, nelx, nely, side):
        super().__init__(nelx, nely, side)
        self.fixed = np.sort(np.concatenate((xydof(self.dofs[0:nely+1]), xydof(self.dofs[nelx*(nely+1):(nelx+1)*(nely+1)]))))


class MBB(BC_mom):
    """MBB beam; Left wall supported, right end supported, point load on top"""
    def __init__(self, nelx, nely, side):
        super().__init__(nelx, nely, side)
        self.fixed = np.sort(np.concatenate((xdof(self.dofs[0:nely+1]), ydof([(nelx+1)*(nely+1)-1]))))


### Michells: (or Pragers)

class MBeamHalf(BC_mom):
    """ Michell Beam, fixed at upper corners. Similar to Bridge... 
    """
    def __init__(self, nelx, nely, side):
        super().__init__(nelx, nely, side)
        self.fixed = np.sort(np.concatenate((xydof([0]), xydof([nelx*(nely+1)]))))


class MBeamFull(BC_mom):
    """Michell Beam, fixed at middle. Similar to Bridge
    """
    def __init__(self, nelx, nely, side):
        super().__init__(nelx, nely, side)
        self.fixed = np.sort(np.concatenate((xydof([nely//2]), xydof([nelx*(nely+1)+nely//2]))))


class MTruss(BC_mom):
    """Prager Truss; Cantilever Michell.
    """
    def __init__(self, nelx, nely, side):
        super().__init__(nelx, nely, side)
        self.fixed = np.sort(xydof([0, nely]))









"""
# 이렇게 보니까 빔 1개로만 해도 참 다양하게 나온다.
# 아예 빔들에 대한 것으로만 해봐도 의미있고 재미있을 것 같다.

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
# Michell Structures (Cantilever but corners)
# Frame/Columns

# Passive elements? (empty/filled contrains)"""