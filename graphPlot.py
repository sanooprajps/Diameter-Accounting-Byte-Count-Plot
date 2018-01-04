#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

readfile = open('test.txt', 'r')
sepFile = readfile.read().split('\n')
readfile.close

for plotPair in sepFile:
            XAndY = plotPair.split(',')
            if len(XAndY) > 1:
                        x.append(int(XAndY[0]))
                        y.append(int(XAndY[1]))
			a.append(int(XAndY[2]))
			b.append(int(XAndY[3]))


def split(arr, size):
     arrs = []
     while len(arr) > size:
         pice = arr[:size]
         arrs.append(pice)
         arr   = arr[size:]
     arrs.append(arr)
     return arrs

MDN = split(x,10)
Session = split(y,10)
ValFlow = split(a,10)
FFLOW = split(b,10)

k=0

M = MDN[k]
S = Session[k]
V = ValFlow[k]
T = FFLOW[k]
fig = plt.figure(figsize=(11,4)) #sets a different size (inches wide, inches tall)
ax = plt.subplot(111)
plt.subplots_adjust(bottom=0.2)

width = 0.25       # the width of the bars: can also be len(x) sequence

ind = np.arange(0,len(M) - width)    # the x locations for the groups

p1 = plt.bar(ind, S,   width, color='r')
p2 = plt.bar(ind+width, V, width, color='y')
p3 = plt.bar(ind+width+width, T, width, color='b')

plt.ylabel('Sessions')
plt.xlabel('MDNs')
plt.title('MDN vs Sessions')
plt.xticks(ind+width/2.,(M), rotation=90, fontsize=10)
plt.legend( (p1[0], p2[0],p3[0]), ('Sessions', 'ValidationFlows','FFLOW Flows') )
ax.set_xticklabels(M)

class Index():
    def next(self,event):
	plt.close()	
	global k	
	global MDN
	if k == len(MDN) - 1:
		k=0
	else:
		k=k+1
	M = MDN[k]
	S = Session[k]
	V = ValFlow[k]
	T = FFLOW[k]
	
	fig = plt.figure(figsize=(11,4)) #sets a different size (inches wide, inches tall)
	ax = plt.subplot(111)
	plt.subplots_adjust(bottom=0.2)

	width = 0.25       # the width of the bars: can also be len(x) sequence

	ind = np.arange(0,len(M) - width)    # the x locations for the groups

	p1 = plt.bar(ind, S,   width, color='r')
	p2 = plt.bar(ind+width, V, width, color='y')
	p3 = plt.bar(ind+width+width, T, width, color='b')

	plt.ylabel('Sessions')
	plt.xlabel('MDNs')
	plt.title('MDN vs Sessions')
	plt.xticks(ind+width/2.,(M), rotation=90, fontsize=10)
	plt.legend( (p1[0], p2[0],p3[0]), ('Sessions', 'ValidationFlows','FFLOW Flows') )
	ax.set_xticklabels(M)
	
	callback = Index()
	axprev = plt.axes([0.7, 0.01, 0.1, 0.075])
	axnext = plt.axes([0.81, 0.01, 0.1, 0.075])
	bnext = Button(axnext, 'Next')
	bnext.on_clicked(callback.next)
	bprev = Button(axprev, 'Previous')
	bprev.on_clicked(callback.prev)
	ax.grid(True)
	plt.show()


    def prev(self, event):
        plt.close() 
        global k
        global MDN
        if k == 0:
                k=len(MDN) - 1
        else:
                k=k-1
        M = MDN[k]
        S = Session[k]
        V = ValFlow[k]
        T = FFLOW[k]
        fig = plt.figure(figsize=(11,4)) #sets a different size (inches wide, inches tall)
        ax = plt.subplot(111)
        plt.subplots_adjust(bottom=0.2)

        width = 0.25       # the width of the bars: can also be len(x) sequence

        ind = np.arange(0,len(M) - width)    # the x locations for the groups

        p1 = plt.bar(ind, S,   width, color='r')
        p2 = plt.bar(ind+width, V, width, color='y')
        p3 = plt.bar(ind+width+width, T, width, color='b')

        plt.ylabel('Sessions')
        plt.xlabel('MDNs')
        plt.title('MDN vs Sessions')
        plt.xticks(ind+width/2.,(M), rotation=90, fontsize=10)
        plt.legend( (p1[0], p2[0],p3[0]), ('Sessions', 'ValidationFlows','FFLOW Flows') )
        ax.set_xticklabels(M)

        callback = Index()
        axprev = plt.axes([0.7, 0.01, 0.1, 0.075])
        axnext = plt.axes([0.81, 0.01, 0.1, 0.075])
        bnext = Button(axnext, 'Next')
        bnext.on_clicked(callback.next)
        bprev = Button(axprev, 'Previous')
        bprev.on_clicked(callback.prev)
	ax.grid(True)
        plt.show()


callback = Index()
axprev = plt.axes([0.7, 0.01, 0.1, 0.075])
axnext = plt.axes([0.81, 0.01, 0.1, 0.075])
bnext = Button(axnext, 'Next')
bnext.on_clicked(callback.next)
bprev = Button(axprev, 'Previous')
bprev.on_clicked(callback.prev)
ax.grid(True)
plt.show()