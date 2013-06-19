import tkinter
#from tkinter.dnd import *
from dndtester import *

#from test import *


from block import *
from conn import *
#from importall import *
from importBlocks import *
from sim import *


#global sim
S = Simulator
S.sim = S()
S.sim.lateinit()


def tickandstatus(blocks):
	print()
	print("Tick...")
	print()
	S.sim.tick()
	for block in blocks:
		print(block.name)
		for name,value in block.inputs.items():
			print(name,":",value)
		for name,value in block.outputs.items():
			print(name,":",value)
		print()

def deltoolbutton(*args): S.sim.selectedTool = "del"; print("SelectedTool: DEL")
def selecttoolbutton(*args): S.sim.selectedTool = "select"; print("SelectedTool: SELECT")
def dndtoolbutton(*args): S.sim.selectedTool = "dnd"; print("SelectedTool: Drag'n'Drop")


def tickbutton(*args):
	tickandstatus(S.sim.blocks)
	S.sim.drawConns(t1.canvas)

def saveSim(): S.sim.save()
def openSim():
	loadSim(t1.canvas)

def gui():
	root = tkinter.Tk()
	root.title("MainStuff")
	root.geometry("+5+5")
	tkinter.Button(command=root.quit, text="Quit").pack()
	tkinter.Button(command=tickbutton, text="Tick").pack()
	tkinter.Button(command=deltoolbutton, text="Tool: DEL").pack()
	tkinter.Button(command=selecttoolbutton, text="Tool: SELECT").pack()
	tkinter.Button(command=dndtoolbutton, text="Tool: DND").pack()
	tkinter.Button(command=openSim, text="Open Sim").pack()
	tkinter.Button(command=saveSim, text="Save Sim").pack()
	tkinter.Button(command=lambda : S.sim.drawConns(t1.canvas), text="Redraw").pack()
	root.bind("<space>", tickbutton)
	t1 = Tester(root)
	t1.top.geometry("+100+100")
	t1.top.bind("<space>", tickbutton)
	#S.sim.maincanvas = t1.canvas
	global t1
	#t2 = Tester(root)
	#t2.top.geometry("+120+60")
	#t3 = Tester(root)
	#t3.top.geometry("+240+60")
	
	
	placegui()
	
	lever = Lever()
	inverter = Inverter()
	lamp = Lamp()
	
	
	lever1 = Lever()
	lever2 = Lever()
	
	and1 = And()
	lamp1 = Lamp() 

	S.sim.addBlock(lever1)
	S.sim.addBlock(lever2)
	S.sim.addBlock(and1)
	S.sim.addBlock(lamp1)
	
	S.sim.connect((lever1,"Output"), (and1,"Input1"))
	S.sim.connect((lever2,"Output"), (and1,"Input2"))
	S.sim.connect((and1,"Output"), (lamp1,"Input"))
	
	S.sim.addBlock(inverter)
	S.sim.addBlock(lever)
	S.sim.addBlock(lamp)
	
	
	S.sim.connect((inverter,"Output"), (lamp,"Input"))
	S.sim.connect((lever,"Output"), (inverter,"Input"))
	
	lever.attach(t1.canvas)
	inverter.attach(t1.canvas)
	lamp.attach(t1.canvas)
	
	
	lamp1.attach(t1.canvas)
	and1.attach(t1.canvas)
	lever1.attach(t1.canvas)
	lever2.attach(t1.canvas)
	root.mainloop()



def placegui():
	# using Tkinter's Optionmenu() as a combobox
	def title():
	    sf = "%s was placed" % blockvar.get()
	    place.title(sf)
	def placeblock():
		newblock = avalibleblocksdict[blockvar.get()][0]()
		newblock.onSetting()
		S.sim.addBlock(newblock)
		print(newblock,"was placed.")
		print(newblock.inputs)
		newblock.attach(t1.canvas)
		title()


	place = tkinter.Tk()
	# use width x height + x_offset + y_offset (no spaces!)
	place.geometry("%dx%d+%d+%d" % (330, 80, 200, 150))
	place.title("Select the Block you want to Place...")

	blockvar = tkinter.StringVar(place)
	
	blockvar.set(avalibleblocknames[0])
	option = tkinter.OptionMenu(place, blockvar, *avalibleblocknames)
	option.pack(side='left', padx=10, pady=10)
	placebutton = tkinter.Button(place, text="place", command=placeblock)
	placebutton.pack(side='left', padx=20, pady=10)

	#place.mainloop()
