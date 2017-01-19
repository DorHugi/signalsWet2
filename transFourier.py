import numpy as np
import matplotlib.pyplot as plt

#CONSTS:
PI = np.pi



def transFourier(x,t,w):

    # dt is the interval between two samples
    dt= t[1]-t[0]


    # Prepare matrices:

    wMatrix, _dontCare = np.meshgrid(w, t)
    timeMatrix, _dontCare = np.meshgrid(t, w)

    # Prepare for matrix multiplication, and calculating the series correctly:

    wMatrix = wMatrix.transpose()
    outerMatrix = np.exp((wMatrix* timeMatrix) * 1j)


    #Now when we have the matrix the we were looking for, all that remains is to calc the dot product and normalize by dt.

    ft = dt*np.dot(outerMatrix,x)

    return ft




#MAIN:


#Question 1


# part d
dt = 0.02
t = np.arange(-3,3,dt)
x = np.sin(2*PI*t) +2*np.cos(2*PI*2*t)

# part E
fs = 1/dt

w = 2*PI*np.linspace(-fs/2,fs/2,len(t)+1)

ft = transFourier(x,t,w)
ft = np.absolute(ft)

#Plot
ax1 = plt.subplot(211)
ax1.plot(t,x)
ax1.set_title('First graph')
ax1.set_xlim([t.min(),t.max()])


ax2 = plt.subplot(212)
ax2.plot(w,ft)
ax2.set_xlim([-10*PI,10*PI])

ax2.set_title('Fourier transform')

plt.show()


