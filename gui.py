import tkinter
#from tkinter.dnd import *
from dndtester import *

#from test import *


from block import *
from conn import *
#from importall import *
from Blocks import *
from sim import *

sim = Simulator()


def tickandstatus(blocks):
	print()
	print("Tick...")
	print()
	sim.tick()
	for block in blocks:
		print(block.name)
		for name,value in block.inputs.items():
			print(name,":",value)
		for name,value in block.outputs.items():
			print(name,":",value)
		print()

def tickbutton(*args):
	tickandstatus(sim.blocks)

def gui():
	root = tkinter.Tk()
	root.geometry("+1+1")
	tkinter.Button(command=root.quit, text="Quit").pack()
	tkinter.Button(command=tickbutton, text="Tick").pack()
	root.bind("<space>", tickbutton)
	t1 = Tester(root)
	t1.top.geometry("+1+60")
	t1.top.bind("<space>", tickbutton)
	#t2 = Tester(root)
	#t2.top.geometry("+120+60")
	#t3 = Tester(root)
	#t3.top.geometry("+240+60")
	
	
	
	
	lever = Lever()
	inverter = Inverter()
	lamp = Lamp()
	
	sim.addBlock(inverter)
	sim.addBlock(lever)
	sim.addBlock(lamp)
	
	sim.connect((inverter,"Output"), (lamp,"Input"))
	sim.connect((lever,"Output"), (inverter,"Input"))
	
	lever.attach(t1.canvas)
	inverter.attach(t1.canvas)
	lamp.attach(t1.canvas)
	root.mainloop()
gui()