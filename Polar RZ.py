#Implementation of RZ Encoding Scheme
import matplotlib.pyplot as plt
import numpy as np
#Function for drwaing vertical dashed lines and Y-axis
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
bits = [0,1,0,0,1]
j=0
#Encoding of signal bits to RZ scheme signal bits
for i in range(len(bits)):
    if(bits[i]==1):
        clock.insert(j,1)
        clock.insert(j+1,0)
    elif(bits[i]==0):
            clock.insert(j,-1)
            clock.insert(j+1,0)
    j=j+2
clock.insert(j+1,0)
data=np.repeat(clock,1)
t = 0.5 * np.arange(len(data))
my_lines('x', range(len(bits)+1), color='black', linewidth=1)
plt.arrow(0, 2,len(bits)+1-0.1, 0, head_width=0.05, head_length=0.1, fc='k', ec='k')
plt.step(t, data+2, 'r', linewidth = 2.5, where='post')
plt.ylim([0,4])
plt.xlim([-0.1,len(bits)+1])
for tbit, bit in enumerate(bits):
    plt.text(tbit + 0.5, 3.5, str(bit))
plt.text(-0.2,4.1,'Amplitude');
plt.text(len(bits)+0.3,1.8,'Time');
plt.gca().axis('off')
plt.savefig("RZ.png")
plt.show()



