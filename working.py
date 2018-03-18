import time
from Chem2D import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pickle

bound = 15
res = 20

print("Estimated time:", (1.2*res**3)/100, "seconds...")
result = hydrogen_wave_func(3,1,0,bound,res,res,res)
print("Generate data took", time.time()-start, "seconds")

pickle.dump(result, open("3.1.0."+str(bound)+"."+str(res)+"_full.p", "wb"))

result = pickle.load(open("3.1.0."+str(bound)+"."+str(res)+"_full.p", "rb"))
x,y,z,mag,mag_true = result

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')
cm_c = plt.get_cmap("plasma")
colors = mag_true*1000
start = time.time()
print("Start plotting...")
for i in range(0,len(mag)):
    for j in range (0,len(mag)):
        for k in range (0,len(mag)):
            plot_3d = ax.scatter(x[i][j][k],y[i][j][k],z[i][j][k], marker="o", c=[colors[i][j][k]],cmap=cm_c, alpha=(mag[i][j][k]/np.amax(mag)))

limit = bound*1.2
ax.set_xlim3d(-limit, limit)
ax.set_ylim3d(-limit,limit)
ax.set_zlim3d(-limit,limit)
ax.elev = 0
ax.azim = 0
print("Rendering...")
plt.show()

