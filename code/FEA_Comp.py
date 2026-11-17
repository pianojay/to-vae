# A 200 LINE TOPOLOGY OPTIMIZATION CODE BY NIELS AAGE AND VILLADS EGEDE JOHANSEN, JANUARY 2013
# Updated by Niels Aage February 2016

from __future__ import division

from time import time

import numpy as np
from scipy.sparse import coo_matrix
import cvxopt ;import cvxopt.cholmod

import pandas as pd
from matplotlib import colors
import matplotlib.pyplot as plt

def main(nelx, nely, volfrac, penal, rmin, ft, fixed, f, x):
    x = x.ravel()
    # fixed dofs and force matrix comes as an input.
    Emin, Emax = 1e-9, 1.0		# Max and min stiffness
    ndof = 2*(nelx+1)*(nely+1)	# dofs

    # Allocate design variables (as array), initialize and allocate sens.
    # x = volfrac * np.ones(nely*nelx,dtype=float)
    xPhys = x.copy()

    # FE: Build the index vectors for the for coo matrix format.
    KE=lk()
    edofMat=np.zeros((nelx*nely,8),dtype=int)
    for elx in range(nelx):
        for ely in range(nely):
            el = ely+elx*nely
            n1=(nely+1)*elx+ely
            n2=(nely+1)*(elx+1)+ely
            edofMat[el,:]=np.array([2*n1+2, 2*n1+3, 2*n2+2, 2*n2+3, 2*n2, 2*n2+1, 2*n1, 2*n1+1])
    # Construct the index pointers for the coo format
    iK = np.kron(edofMat,np.ones((8,1))).flatten()
    jK = np.kron(edofMat,np.ones((1,8))).flatten()    

    # Filter: Build (and assemble) the index+data vectors for the coo matrix format
    nfilter=int(nelx*nely*((2*(np.ceil(rmin)-1)+1)**2))
    iH = np.zeros(nfilter)
    jH = np.zeros(nfilter)
    sH = np.zeros(nfilter)
    cc=0
    for i in range(nelx):
        for j in range(nely):
            row=i*nely+j
            kk1, kk2 = max(i - (np.ceil(rmin) - 1), 0), min(i + np.ceil(rmin), nelx)
            ll1, ll2 = max(j - (np.ceil(rmin) - 1), 0), min(j + np.ceil(rmin), nely)
            for k in range(int(kk1), int(kk2)):
                for l in range(int(ll1), int(ll2)):
                    col=k*nely+l
                    fac=rmin-np.sqrt(((i-k)*(i-k)+(j-l)*(j-l)))
                    iH[cc]=row
                    jH[cc]=col
                    sH[cc]=np.maximum(0.0,fac)
                    cc += 1

    # BC's and support
    dofs=np.arange(2*(nelx+1)*(nely+1))
    free=np.setdiff1d(dofs,fixed) # fixed is given as parameter

    # Solution and RHS vectors
    # f is given as parameter
    u=np.zeros((ndof,1))
    
    ce = np.ones(nely*nelx)

    # Setup and solve FE problem
    sK=((KE.flatten()[np.newaxis]).T*(Emin+(xPhys)**penal*(Emax-Emin))).flatten(order='F')
    K = coo_matrix((sK,(iK,jK)),shape=(ndof,ndof)).tocsc()
    # Remove constrained dofs from matrix and convert to coo
    K = deleterowcol(K,fixed,fixed).tocoo() # *removed intermediate step
    # Solve system
    K = cvxopt.spmatrix(K.data,K.row.astype(int),K.col.astype(int))
    B = cvxopt.matrix(f[free,0])
    cvxopt.cholmod.linsolve(K,B)
    u[free,0]=np.array(B)[:,0]

    # TODO: from cvxopt to cupy for GPU? -> Bad idea. (CPU->GPU->CPU bottle-neck)

    # Objective and sensitivity
    ce[:] = (np.dot(u[edofMat].reshape(nelx*nely,8),KE) * u[edofMat].reshape(nelx*nely,8) ).sum(1)
    obj=( (Emin+xPhys**penal*(Emax-Emin))*ce ).sum()

    if False:
        _,ax = plt.subplots()
        ax.imshow(-xPhys.reshape((nelx,nely)).T, cmap='gray', interpolation='none', norm=colors.Normalize(vmin=-1,vmax=0))
        plt.show()
        input("Press any key...")

    return obj


#element stiffness matrix   
def lk():
    E, nu = 1, 0.3
    k=np.array([1/2-nu/6,1/8+nu/8,-1/4-nu/12,-1/8+3*nu/8,-1/4+nu/12,-1/8-nu/8,nu/6,1/8-3*nu/8])
    KE = E/(1-nu**2)*np.array([
        [k[0], k[1], k[2], k[3], k[4], k[5], k[6], k[7]],
        [k[1], k[0], k[7], k[6], k[5], k[4], k[3], k[2]],
        [k[2], k[7], k[0], k[5], k[6], k[3], k[4], k[1]],
        [k[3], k[6], k[5], k[0], k[7], k[2], k[1], k[4]],
        [k[4], k[5], k[6], k[7], k[0], k[1], k[2], k[3]],
        [k[5], k[4], k[3], k[2], k[1], k[0], k[7], k[6]],
        [k[6], k[3], k[4], k[1], k[2], k[7], k[0], k[5]],
        [k[7], k[2], k[1], k[4], k[3], k[6], k[5], k[0]]
    ])
    return (KE)

def deleterowcol(A, delrow, delcol):
    # Assumes that matrix is in symmetric csc form !
    m = A.shape[0]
    A = A[np.delete(np.arange(0, m), delrow), :]
    A = A[:, np.delete(np.arange(0, m), delcol)]
    return A


from bc_options import *
def fea_c(nelx, nely, volfrac, penal, rmin, ft, fixed, f, x): # XXX no backward compatibility. sorry
    return main(nelx, nely, volfrac, penal, rmin, ft, fixed, f, x)