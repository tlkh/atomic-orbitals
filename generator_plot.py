import time
from Chem2D import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pickle
import seaborn

bound = 15
res = 20

for l in range(0,3):
    for m in range(-l,l+1):
        print("Doing:", l,float(m))
        result = pickle.load(open("3."+str(l)+"."+str(m)+".0."+str(bound)+"."+str(res)+"_full.p", "rb"))
        x,y,z,mag,mag_true = result
        fig = plt.figure(figsize=(10,10))
        ax = fig.add_subplot(111, projection='3d')
        cm_c = plt.get_cmap("plasma")
        colors = mag_true*1000
        print("Start plotting...")
        for i in range(0,len(mag)):
            for j in range (0,len(mag)):
                for k in range (0,len(mag)):
                    if colors[i][j][k] > 0:
                        colour = 'r'
                    else:
                        colour = 'b'
                    plot_3d = ax.scatter(x[i][j][k],y[i][j][k],z[i][j][k], marker="o", c=colour,cmap=cm_c, alpha=(mag[i][j][k]/np.amax(mag)))
        limit = bound*1.4
        ax.set_title(r"$n$=3, $l$="+str(int(l))+r", $m$="+str(int(m)))
        ax.set_xlim3d(-limit, limit)
        ax.set_ylim3d(-limit,limit)
        ax.set_zlim3d(-limit,limit)
        ax.set_xlabel(r'$x$')
        ax.set_ylabel(r'$y$')
        ax.set_zlabel(r'$z$')
        plt.savefig("plot_3_" + str(l) + "_" + str(m) + ".jpg", bbox_inches='tight')