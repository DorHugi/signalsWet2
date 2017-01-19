import numpy as np
import matplotlib.pyplot as plt

#CONSTS:
PI = np.pi
#TODO:
#1) Add names to axes and title.

# part A
def transFourier(x,t,w):
    # dt is the interval between two samples

    dt= t[1]-t[0]

    # Prepare matrices:

    wMatrix, _dontCare = np.meshgrid(w, t)
    timeMatrix, _dontCare = np.meshgrid(t, w)

    # Prepare for matrix multiplication, and calculating the series correctly:

    wMatrix = wMatrix.transpose()
    wMatrix = wMatrix*timeMatrix

    wMatrix = wMatrix*(1j)

    outerMatrix = np.exp(wMatrix)


    #Now when we have the matrix the we were looking for, all that remains is to calc the dot product and normalize by dt.

    ft = dt*np.dot(outerMatrix,x)

    return ft

# part B


def invTransFourier(X,w,t):
    # Return inverse transform, using the properties we learned in class.
    #TODO: fix this minus
    return transFourier(X,-w,t)*(-1/(2*PI))


def windowFunc(t,wind):
    return np.asarray([1*(i > -wind and i < wind) for i in t])


#MAIN:



def main():

    # part d
    dt = 0.02
    t = np.arange(-3,3,dt)

    # part d function:
    x = np.sin(2*PI*t) +2*np.cos(2*PI*2*t)
    firstFunc = x


    fs = 1/dt

    w = 2*PI*np.linspace(-fs/2,fs/2,len(t)+1)

    ft = transFourier(x,t,w)
    firstFourier = ft
    ift =invTransFourier(ft,w,t)
    # As we were asked - plot abs value

    ft = np.absolute(ft)

    #Plot
    # fig = plt.figure()
    # ax1 = plt.subplot(211)
    # ax1.plot(t,x,label='original function')
    # ax1.set_title('Original graph - time domain')
    # ax1.set_xlim([t.min(),t.max()])
    # ax1.set_xlabel('time')
    # ax1.plot(t,ift,label='inverse fourier transform')
    # plt.legend()
    #
    # ax2 = plt.subplot(212)
    # ax2.plot(w,ft)
    # ax2.set_xlim([-10*PI,10*PI])
    # ax2.set_title('Fourier transform - frequency domain')
    # ax2.set_xlabel('frequency')
    #
    # plt.subplots_adjust(top=0.90)
    # fig.tight_layout()


    # part E
    dt = 0.02
    t = np.arange(-3,3,dt)


    #part e function:
    W = 4*PI
    x = (W/PI)*np.sinc((W/PI)*t)


    fs = 1/dt

    w = 2*PI*np.linspace(-fs/2,fs/2,len(t)+1)

    ft = transFourier(x,t,w)
    secondFourier = ft
    ift =invTransFourier(ft,w,t)
    analyticCalc = windowFunc(w,W)

    # As we were asked - plot abs value

    ft = np.absolute(ft)

    #Plot
    # fig = plt.figure()
    # ax1 = plt.subplot(211)
    # ax1.plot(t,x,label='original function')
    # ax1.set_title('Original graph - time domain')
    # ax1.set_xlim([t.min(),t.max()])
    # ax1.set_xlabel('time')
    # ax1.plot(t,ift,label='inverse fourier transform')
    #
    # plt.legend()
    #
    # ax2 = plt.subplot(212)
    # ax2.plot(w,ft,label = 'Numeric calculation')
    # ax2.set_xlim([-10*PI,10*PI])
    # ax2.set_title('Fourier transform - frequency domain')
    # ax2.set_xlabel('frequency')
    # ax2.plot(w,analyticCalc,label='Analytic calculation')
    # plt.legend()
    # plt.subplots_adjust(top=0.90)
    # fig.tight_layout()


    #Part G:

    # Convolution in time domain is multiplication in Frequency domain
    fourierZ = firstFourier*secondFourier
    actualZ = invTransFourier(fourierZ,w,t)


    #Plot
    fig = plt.figure()
    ax1 = plt.subplot(221)
    ax1.plot(t,firstFunc,label='harmonic sum')
    plt.legend()

    ax2 = plt.subplot(222)
    ax2.plot(w,np.abs(firstFourier),label='harmonic sum fourier')
    ax2.plot(w,secondFourier,label='sinc fourier')
    ax2.set_xlim([-10*PI,10*PI])
    plt.legend()

    ax3 = plt.subplot(223)
    ax3.plot(t,actualZ,label='z function')
    ax3.set_xlim([-3,3])
    plt.legend()

    ax4 = plt.subplot(224)
    ax4.plot(w,np.abs(fourierZ),label='z fourier')
    ax4.set_xlim([-10*PI,10*PI])
    plt.legend()

    plt.tight_layout()
    plt.show()




if __name__ ==  "__main__":
    main()
