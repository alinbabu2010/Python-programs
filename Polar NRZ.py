import matplotlib.pyplot as plt
import numpy as np
def my_lines(ax, pos, *args, **kwargs):
    if ax == 'x':
        for p in pos:
            if(p!=0):
                plt.axvline(p,linestyle='dashed', *args, **kwargs)
            else:
                plt.arrow(0,0,0,3.9,head_width=0.05, head_length=0.1, fc='k', ec='k')
    else:
        for p in pos:
            plt.axhline(p, *args, **kwargs)
clock = []
bits = [0,1,0,0,1,1,1,0]
for i in range(len(bits)):
    if(bits[i]==1):
        if(i!=0):
            if(clock[i-1]==0):
                clock.insert(i,1)
            else:
                clock.insert(i,0)
        else:
            clock.insert(i,0)
    else:
        if(i!=0):
            if(clock[i-1]==0):
                clock.insert(i,0)
            else:
                clock.insert(i,1)
        else:
             clock.insert(i,1)
data=np.repeat(clock,2)
data=np.insert(data,len(bits)*2,clock[i-1])
t = 0.5 * np.arange(len(data))
my_lines('x', range(len(bits)+1), color='black', linewidth=1)
plt.arrow(0, 2,len(bits)+1-0.1, 0, head_width=0.05, head_length=0.1, fc='k', ec='k')
plt.step(t, data+1.5, 'r', linewidth = 2, where='post')
plt.ylim([0,4])
plt.xlim([-0.11,len(bits)+1])
for tbit, bit in enumerate(bits):
    plt.text(tbit + 0.5, 3.5, str(bit))
plt.text(len(bits)+0.3,1.8,'Time')
plt.text(-0.2,4.1,'Amplitude')
plt.gca().axis('off')
plt.savefig("NRZ-I.png")
plt.show()


