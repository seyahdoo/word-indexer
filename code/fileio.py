def parse_file(file_path):
	file = open(file_path, "r")
	context = []
	for line in file:
		context.add({line.split(";")[0]: line.split(";")[1]})
	file.close()