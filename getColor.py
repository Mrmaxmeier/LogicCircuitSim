def standardCols(val):
	if val == -1:
		return "red"
	elif val == 1:
		return "green"
	elif val == str(val):
		return "blue"
	elif val > 1:
		return "yellow"
	else:
		return "black"