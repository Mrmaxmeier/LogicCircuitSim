import os

with open("blocks_generated.py", "w") as blocks:
	blocks.write("#WARNING: do not edit!\n")
	for filename in os.listdir("Blocks"):
		if filename.endswith(".py"):
			print("writing "+filename)
			with open(os.path.join("Blocks", filename), "r") as f:
				for line in f:
					blocks.write(line)

from blocks_generated import *
