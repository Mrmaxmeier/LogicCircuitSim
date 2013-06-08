from block import *
from conn import *
from importall import *
from sim import *

sim = Simulator()
sim.addBlock(Inverter())
sim.addBlock(Lever())
sim.addBlock(Lamp())
inverter = sim.blocks[0]
lever = sim.blocks[1]
lamp = sim.blocks[2]

print(sim)
print(sim.blocks)
print(sim.blocks[0].outputs["Output"])
sim.connect((inverter,"Output"), (lamp,"Input"))
sim.connect((lever,"Output"), (inverter,"Input"))

def tickandstatus():
	print("Tick...")
	sim.tick()
	print("Lever-O:",lever.outputs["Output"],"\nInverter-I:",inverter.inputs["Input"],"\nInverter-O:",inverter.outputs["Output"],"\nLamp-I:",lamp.inputs["Input"])
#tickandstatus()
#lever.onClick()
#tickandstatus()
#lever.onClick()
#tickandstatus()
##sim.blocks[1].onClick()
#tickandstatus()
##sim.blocks[1].onClick()
#tickandstatus()
##not1 = Not()
##lever1 = Lever()
##lamp1 = Lamp()
