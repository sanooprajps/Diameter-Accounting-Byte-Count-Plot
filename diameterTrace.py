#!/usr/bin/python

######################################################################
## Script will count Client & server side Accounting input/ouput octets
## Script accepts Client, server side pcaps and server port as the input
## Output will be sum of Client/Server, Accounting input/output bytes
######################################################################

import re
import time
import os
import sys
import subprocess
import numpy as np	## Make sure numpy package is installed before running the script
import matplotlib.pyplot as plt	## Make sure matplotlib package is installed before running the script
import  Tkinter ## Make sure Tkinter package is installed before running the script

from Tkinter import *
from matplotlib.widgets import Button
###################################################################
## Calling messagesort.sh script (This will be deleted at the end)
###################################################################

def PlotGraph():
	x=[]
	y=[]
	a=[]
	b=[]


	readfile = open('graph-mdn-sessionCount.txt', 'r')
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

	global k
	global MDN
	k=0
	
	MDN = split(x,10)
	Session = split(y,10)
	ValFlow = split(a,10)
	FFLOW = split(b,10)


	M = MDN[k]
	S = Session[k]
	V = ValFlow[k]
	T = FFLOW[k]
	fig = plt.figure(figsize=(11,4)) #sets a different size (inches wide, inches tall)
	ax = plt.subplot(111)
	plt.subplots_adjust(bottom=0.2)

	width = 0.25       # the width of the bars: can also be len(x) sequence

	ind = np.arange(0,len(M) - width)    # the x locations for the groups

	p1 = plt.bar(ind, S,   width, color='g')
	p2 = plt.bar(ind+width, V, width, color='c')
	p3 = plt.bar(ind+width+width, T, width, color='y')

	plt.ylabel('Sessions')
	plt.xlabel('MDNs')
	plt.title('MDN vs Sessions')
	plt.xticks(ind+width/2.,(M), rotation=90, fontsize=12)
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

			p1 = plt.bar(ind, S,   width, color='g')
			p2 = plt.bar(ind+width, V, width, color='c')
			p3 = plt.bar(ind+width+width, T, width, color='y')

			plt.ylabel('Sessions')
			plt.xlabel('MDNs')
			plt.title('MDN vs Sessions')
			plt.xticks(ind+width/2.,(M), rotation=90, fontsize=10)
			plt.legend( (p1[0], p2[0],p3[0]), ('Total Sessions', 'ValidationFlows','FFLOW Flows') )
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

        		p1 = plt.bar(ind, S,   width, color='g')
        		p2 = plt.bar(ind+width, V, width, color='c')
        		p3 = plt.bar(ind+width+width, T, width, color='y')

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
	dbprev = Button(axprev, 'Previous')
	dbprev.on_clicked(callback.prev)
	ax.grid(True)
	plt.show()

def Execute_Filter ():
	os.system("clear")
	os.system("chmod 755 diameterFiler.sh")
	
	subprocess.call(['./diameterFiler.sh', str(cpcap), str(spcap), str(sport), str(cport)])	
	print ('Done running filter script')	
## ####################################################################
##      Plotting the graph - Reading values from *.txt file
#######################################################################

	PlotGraph ()
## ####################################################################
##	GUI create function
#######################################################################

def creategui ():
	#create a new window
	window = Tkinter.Tk()
	#set the window background to hex code #999E98
	#window.configure(background="#999E98")
	#set the window title
	window.title("diametertrace")
	window.geometry('{}x{}'.format(500, 250))
	
	#create a label for the instructions
	lblInst = Tkinter.Label(window, text="diameter tracer", fg="#383a39", font=("Courier New", 19, "bold"))
	#and pack it into the window
	lblInst.pack()
	
	#create the widgets for entering a Client pcap
	lblClientPcap = Tkinter.Label(window, text="Client pcap:", fg="#383a39", borderwidth=2, highlightthickness=2, highlightcolor="#383a39")
	entClientPcap = Tkinter.Entry(window)
	#and pack them into the window
	lblClientPcap.pack()
	entClientPcap.pack()

	#create the widgets for entering a server pcap
	lblSereverPcap = Tkinter.Label(window, text="Server pcap:", fg="#383a39")
	entServerPcap = Tkinter.Entry(window)
	#and pack them into to the window
	lblSereverPcap.pack()
	entServerPcap.pack()

	#create the widgets for entering a server port	
	lblSereverPort = Tkinter.Label(window, text="Server port:", fg="#383a39")
	entServerPort = Tkinter.Entry(window)
	#and pack them into to the window
	lblSereverPort.pack()
	entServerPort.pack()
	
	## Handling close event
	def on_closing():
		print ('Closing the window... bye bye... !!!')
		sys.exit()
	window.protocol("WM_DELETE_WINDOW", on_closing)
	#Creating selection button for vsep/pgw traffic

	def sel():
		global radioSelection
		global port
		radioSelection = int(str(var.get()))
		if radioSelection == 1:
			selection = "You selected Client traffic as CLIENT Rf "
			port = int(3998)
		elif radioSelection == 2:
			selection = "You selected Client traffic as PGW Rf "
			port = int(3999)
		else:
			selection = "Invalid input received "
		#label.config(fg="#383a39", bg="#F5900C",text = selection)
		label.config(text = selection, fg="#383a39")
		
	def callback():
		global port
		#print 'Client pcap entered:' + entClientPcap.get()
		#print 'Server pcap entered:' + entServerPcap.get()
		#print 'Server port entered:' + entServerPort.get()
		#print  port
		
		global cpcap
                global spcap
                global sport
                global cport

		cpcap = entClientPcap.get()
		spcap = entServerPcap.get()
		sport = entServerPort.get()
		cport = int(port)

		Execute_Filter()
		
	var = IntVar()
	R1 = Radiobutton(window, text="VSEP Rf", variable=var, value=1,
					  fg="#383a39", bg="#53EB21", command=sel, height = 1, width = 13, relief=RAISED)
	R1.pack( anchor = W )

	R2 = Radiobutton(window, text="PGW Rf", variable=var, value=2,
					  fg="#383a39", bg="#53EB21", command=sel, height = 1, width = 13, relief=RAISED)
	R2.pack( anchor = W )

	label = Label(window)
	label.pack()
	
	#create a button widget called btn	
	btn = Tkinter.Button(window, text="Submit", fg="#000000", bg="#53EB21",command=callback, height = 4, width = 10, relief=RAISED)
	quitbtn = Tkinter.Button(window, text="Quit", fg="#000000", bg="#FF0000",command=on_closing, height = 4, width = 10, relief=RAISED)
	#pack the widget into the window	
	btn.pack(side=LEFT, fill=BOTH, expand=1)
	quitbtn.pack(side=LEFT, fill=BOTH, expand=1)

	#draw the window, and start the application
	window.mainloop()
	
def main ():
## Calling create GUI function
	creategui()
## Calling execute filter function - This will call shell script to run tshark command
	Execute_Filter()

if __name__ == '__main__':
        main()