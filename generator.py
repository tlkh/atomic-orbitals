import time
from Chem2D import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pickle

bound = 15
res = 20

print("full orbitals")

l, m = 0, 0
print("3",l,m)
print("Estimated time:", (1.2*res**3)/100, "seconds...")
start = time.time()
result = hydrogen_wave_func(3,l,m,bound,res,res,res)
print("Generate data took", time.time()-start, "seconds")
pickle.dump(result, open("3."+str(l)+"."+str(m)+".0."+str(bound)+"."+str(res)+"_full.p", "wb"))

l, m = 1, 0
print("3",l,m)
print("Estimated time:", (1.2*res**3)/100, "seconds...")
start = time.time()
result = hydrogen_wave_func(3,l,m,bound,res,res,res)
print("Generate data took", time.time()-start, "seconds")
pickle.dump(result, open("3."+str(l)+"."+str(m)+".0."+str(bound)+"."+str(res)+"_full.p", "wb"))

l, m = 1, -1
print("3",l,m)
print("Estimated time:", (1.2*res**3)/100, "seconds...")
start = time.time()
result = hydrogen_wave_func(3,l,m,bound,res,res,res)
print("Generate data took", time.time()-start, "seconds")
pickle.dump(result, open("3."+str(l)+"."+str(m)+".0."+str(bound)+"."+str(res)+"_full.p", "wb"))

l, m = 1, 1
print("3",l,m)
print("Estimated time:", (1.2*res**3)/100, "seconds...")
start = time.time()
result = hydrogen_wave_func(3,l,m,bound,res,res,res)
print("Generate data took", time.time()-start, "seconds")
pickle.dump(result, open("3."+str(l)+"."+str(m)+".0."+str(bound)+"."+str(res)+"_full.p", "wb"))

l, m = 2, 0
print("3",l,m)
print("Estimated time:", (1.2*res**3)/100, "seconds...")
start = time.time()
result = hydrogen_wave_func(3,l,m,bound,res,res,res)
print("Generate data took", time.time()-start, "seconds")
pickle.dump(result, open("3."+str(l)+"."+str(m)+".0."+str(bound)+"."+str(res)+"_full.p", "wb"))

l, m = 2, -2
print("3",l,m)
print("Estimated time:", (1.2*res**3)/100, "seconds...")
start = time.time()
result = hydrogen_wave_func(3,l,m,bound,res,res,res)
print("Generate data took", time.time()-start, "seconds")
pickle.dump(result, open("3."+str(l)+"."+str(m)+".0."+str(bound)+"."+str(res)+"_full.p", "wb"))

l, m = 2, -1
print("3",l,m)
print("Estimated time:", (1.2*res**3)/100, "seconds...")
start = time.time()
result = hydrogen_wave_func(3,l,m,bound,res,res,res)
print("Generate data took", time.time()-start, "seconds")
pickle.dump(result, open("3."+str(l)+"."+str(m)+".0."+str(bound)+"."+str(res)+"_full.p", "wb"))

l, m = 2, 2
print("3",l,m)
print("Estimated time:", (1.2*res**3)/100, "seconds...")
start = time.time()
result = hydrogen_wave_func(3,l,m,bound,res,res,res)
print("Generate data took", time.time()-start, "seconds")
pickle.dump(result, open("3."+str(l)+"."+str(m)+".0."+str(bound)+"."+str(res)+"_full.p", "wb"))

l, m = 2, 1
print("3",l,m)
print("Estimated time:", (1.2*res**3)/100, "seconds...")
start = time.time()
result = hydrogen_wave_func(3,l,m,bound,res,res,res)
print("Generate data took", time.time()-start, "seconds")
pickle.dump(result, open("3."+str(l)+"."+str(m)+".0."+str(bound)+"."+str(res)+"_full.p", "wb"))

print("cross sections")

l, m = 0, 0
print("3",l,m)
print("Estimated time:", (1.2*res**3)/100, "seconds...")
start = time.time()
result = hydrogen_wave_func_cross(3,l,m,bound,res,res,res)
print("Generate data took", time.time()-start, "seconds")
pickle.dump(result, open("3."+str(l)+"."+str(m)+".0."+str(bound)+"."+str(res)+"_cross.p", "wb"))

l, m = 1, 0
print("3",l,m)
print("Estimated time:", (1.2*res**3)/100, "seconds...")
start = time.time()
result = hydrogen_wave_func_cross(3,l,m,bound,res,res,res)
print("Generate data took", time.time()-start, "seconds")
pickle.dump(result, open("3."+str(l)+"."+str(m)+".0."+str(bound)+"."+str(res)+"_cross.p", "wb"))

l, m = 1, -1
print("3",l,m)
print("Estimated time:", (1.2*res**3)/100, "seconds...")
start = time.time()
result = hydrogen_wave_func_cross(3,l,m,bound,res,res,res)
print("Generate data took", time.time()-start, "seconds")
pickle.dump(result, open("3."+str(l)+"."+str(m)+".0."+str(bound)+"."+str(res)+"_cross.p", "wb"))

l, m = 1, 1
print("3",l,m)
print("Estimated time:", (1.2*res**3)/100, "seconds...")
start = time.time()
result = hydrogen_wave_func_cross(3,l,m,bound,res,res,res)
print("Generate data took", time.time()-start, "seconds")
pickle.dump(result, open("3."+str(l)+"."+str(m)+".0."+str(bound)+"."+str(res)+"_cross.p", "wb"))

l, m = 2, 0
print("3",l,m)
print("Estimated time:", (1.2*res**3)/100, "seconds...")
start = time.time()
result = hydrogen_wave_func_cross(3,l,m,bound,res,res,res)
print("Generate data took", time.time()-start, "seconds")
pickle.dump(result, open("3."+str(l)+"."+str(m)+".0."+str(bound)+"."+str(res)+"_cross.p", "wb"))

l, m = 2, -2
print("3",l,m)
print("Estimated time:", (1.2*res**3)/100, "seconds...")
start = time.time()
result = hydrogen_wave_func_cross(3,l,m,bound,res,res,res)
print("Generate data took", time.time()-start, "seconds")
pickle.dump(result, open("3."+str(l)+"."+str(m)+".0."+str(bound)+"."+str(res)+"_cross.p", "wb"))

l, m = 2, -1
print("3",l,m)
print("Estimated time:", (1.2*res**3)/100, "seconds...")
start = time.time()
result = hydrogen_wave_func_cross(3,l,m,bound,res,res,res)
print("Generate data took", time.time()-start, "seconds")
pickle.dump(result, open("3."+str(l)+"."+str(m)+".0."+str(bound)+"."+str(res)+"_cross.p", "wb"))

l, m = 2, 2
print("3",l,m)
print("Estimated time:", (1.2*res**3)/100, "seconds...")
start = time.time()
result = hydrogen_wave_func_cross(3,l,m,bound,res,res,res)
print("Generate data took", time.time()-start, "seconds")
pickle.dump(result, open("3."+str(l)+"."+str(m)+".0."+str(bound)+"."+str(res)+"_cross.p", "wb"))

l, m = 2, 1
print("3",l,m)
print("Estimated time:", (1.2*res**3)/100, "seconds...")
start = time.time()
result = hydrogen_wave_func_cross(3,l,m,bound,res,res,res)
print("Generate data took", time.time()-start, "seconds")
pickle.dump(result, open("3."+str(l)+"."+str(m)+".0."+str(bound)+"."+str(res)+"_cross.p", "wb"))