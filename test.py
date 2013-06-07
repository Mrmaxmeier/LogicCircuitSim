from block import *
from conn import *
from importall import *
from sim import *

sim = Simulator()
sim.addBlock(Inverter())
sim.addBlock(Lever())
sim.addBlock(Lamp())
print(sim)
print(sim.blocks)
print(sim.blocks[0].outputs["Output"])
sim.connect((sim.blocks[0],sim.blocks[0].outputs["Output"]), (sim.blocks[2],sim.blocks[2].inputs["Input"]))
sim.connect((sim.blocks[1],sim.blocks[1].outputs["Output"]), (sim.blocks[0],sim.blocks[0].inputs["Input"]))
#not1 = Not()
#lever1 = Lever()
#lamp1 = Lamp()
