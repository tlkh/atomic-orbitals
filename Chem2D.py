import numpy as np
import scipy.constants as c
import math, cmath
from sympy import *
from math import e
import numba
from numba import jit
import sympy as sp
r, x, a, theta = symbols('r x a theta')
init_printing(use_unicode=True)

@jit(nopython=True, cache=True, parallel=True)
def spherical_to_cartesian(r, theta, phi):
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    return x, y, z

@jit(nopython=True, cache=True, parallel=True)
def cartesian_to_spherical(x, y, z):
    r = math.sqrt(x ** 2 + y ** 2 + z ** 2)
    theta = np.arccos(z / math.sqrt(x ** 2 + y ** 2 + z ** 2)) if r != 0 else 0
    if x == 0:
        phi = 0 if (y == 0) else 1.5708
    else:
        phi = np.arctan(y / x)
    return r, theta, phi

@jit(nopython=True, cache=True, parallel=True)
def absolute(number):
    return (number.real**2 + number.imag**2)**0.5

def P_l(l):
    ans = 1 / (2 ** l * factorial(l)) * sp.diff((x ** 2 - 1) ** l, x, int(l))
    return ans

def Pm_l(m, l):
    ans = ((1 - x ** 2) ** (abs(m) / 2)) * sp.diff(P_l(l), x, abs(int(m)))
    return ans

def angular_wave_func(m, l, theta_value, phi):
    if m > 0:
        E = (-1)**m
    else:
        E = 1
    A_factor_1 = (2*l+1)/(4*math.pi)
    A_factor_2 = math.factorial(l-abs(m)) / math.factorial(l+abs(m))
    A = math.sqrt(A_factor_1*A_factor_2)
    B = cmath.exp(m*phi*1j)
    C = (Pm_l(m,l).subs(x,cos(theta)).subs(theta, theta_value)).evalf()
    long_ans = complex(E * A * B * C)
    ans = round(long_ans.real, 5) + round(long_ans.imag, 5)*1j

    return ans

def Lq(q):
    ans = e ** x * sp.diff(e ** -x * x ** q, x, int(q))
    return ans

def assoc_Lq(p, q):
    ans = (-1) ** p * sp.diff(Lq(q), x, int(p))
    return ans

bohr=c.physical_constants['Bohr radius'][0]

def radial_wave_func(n, l, radius):
    if radius == 0:
        return np.nan
    else:
        A_factor_1 = (2/(n*a))**3
        A_factor_2 = (math.factorial(n-l-1)) / (2*n*(math.factorial(n+l))**3)
        A = (A_factor_1 * A_factor_2)**0.5
        B = e**(-radius/(n*a))
        C = ((2*radius)/(n*a))**l
        p = 2*l + 1
        q = n-l-1+p
        D = assoc_Lq(p,q)
        expression = A * B * C * D / (a**(-3/2))
        subbed = expression.subs(x, 2*r/(n*a)).subs(r, radius).subs(a, bohr)
        return round(subbed.evalf(), 5)

#@jit
def linspace(start, stop, num=50):
    increment = (stop-start)/(num-1)
    current = start
    output = []
    for i in range(0,int((stop-start)/increment)+1):
        output.append(round(float(current),5))
        current+=increment
    return output

def meshgrid(x,y,z):
    output = [[],[],[]]
    output_0, output_1, output_2 = [],[],[]
    x_list, y_list, z_list = [],[],[]
    z_inner = []
    for k,z_i in enumerate(z):
        z_inner.append(z_i)
    for i,x_i in enumerate(x):
        x_list.append([x_i,x_i])
        z_list.append(z_inner)
    for j,y_i in enumerate(y):
        y_inner = [[y_i,y_i] for i in range(len(x))]
        y_list.append(y_inner)
        output_0.append(x_list)
        output_2.append(z_list)

    return output_0, y_list, output_2

cartesian_to_spherical_vector = (np.vectorize(cartesian_to_spherical))
angular_wave_vector = (np.vectorize(angular_wave_func))
radial_wave_vector = (np.vectorize(radial_wave_func))
absolute_vector = (np.vectorize(absolute))

def hydrogen_wave_func(n, l, m, roa, Nx, Ny, Nz):
    x_space = np.linspace(-roa, roa, Nx)
    y_space = np.linspace(-roa, roa, Ny)
    z_space = np.linspace(-roa, roa, Nz)
    
    xx, yy, zz = np.meshgrid(y_space, x_space, z_space)
    
    r, theta, phi = (cartesian_to_spherical_vector(yy, xx, zz))
    
    if m == 0:
        angular = angular_wave_vector(m, l, theta, phi)
    elif m < 0:
        angular = (1j / math.sqrt(2)) * (angular_wave_vector(m, l, theta, phi) - (-1) ** m * angular_wave_vector(-m, l, theta, phi))
    elif m > 0:
        angular = (1 / math.sqrt(2)) * (angular_wave_vector(-m, l, theta, phi) + (-1) ** m * angular_wave_vector(m, l, theta, phi))
    
    radial = radial_wave_vector(n, l, r * a)
    
    mag = absolute_vector(radial * angular) ** 2
    
    return np.array(yy), np.array(xx), np.array(zz), np.round(mag, 5), radial * angular

#don't use?
def hydrogen_wave_func_cross(n, l, m, roa, Nx, Ny, Nz):
    x_space = np.linspace(-roa, roa, int(Nx/2))
    y_space = np.linspace(-roa, roa, Ny)
    z_space = np.linspace(-roa, roa, Nz)
    
    xx, yy, zz = np.meshgrid(y_space, x_space, z_space)
    
    r, theta, phi = (cartesian_to_spherical_vector(yy, xx, zz))
    
    if m == 0:
        angular = angular_wave_vector(m, l, theta, phi)
    elif m < 0:
        angular = (1j / math.sqrt(2)) * (angular_wave_vector(m, l, theta, phi) - (-1) ** m * angular_wave_vector(-m, l, theta, phi))
    elif m > 0:
        angular = (1 / math.sqrt(2)) * (angular_wave_vector(-m, l, theta, phi) + (-1) ** m * angular_wave_vector(m, l, theta, phi))
    
    radial = radial_wave_vector(n, l, r * a)
    mag_true = radial * angular
    mag = absolute_vector(mag_true) ** 2
    
    return np.array(yy), np.array(xx), np.array(zz), np.round(mag, 5), mag_true