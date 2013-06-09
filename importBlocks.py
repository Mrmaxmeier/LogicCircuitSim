import os

with open("blocks_generated.py", "w") as blocks:
	blocks.write("#WARNING: do not edit!\navalibleblocks = []#[['Name',Class,Ranking]]\n")
	for filename in os.listdir("Blocks"):
		if filename.endswith(".py"):
			print("writing "+filename)
			with open(os.path.join("Blocks", filename), "r") as f:
				for line in f:
					blocks.write(line)
	blocks.write("""print('Imported:',avalibleblocks)
print('Imported',len(avalibleblocks),' in Total.')
avalibleblocksdict = {}
avalibleblocknames = []
for block in avalibleblocks:
	avalibleblocksdict[block[0]] = [block[1],block[2]]
	avalibleblocknames.append(block[0])""")

from blocks_generated import *
