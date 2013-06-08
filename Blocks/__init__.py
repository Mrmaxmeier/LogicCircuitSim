import posix

blocklist = posix.listdir("Blocks")
blocklist.remove("__init__.py")
#blocklist.remove(".DS_Store")


blocklist2 = []

for block in blocklist:
	if block.endswith(".py"):
		blocklist2.append(block)
print("Importing",blocklist2)


for i in blocklist2:
	exec("from "+"Blocks."+i.split(".")[0]+" import *")
	print("imported",i)

#print(posix.listdir("...."))