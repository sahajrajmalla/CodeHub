import csv

# with open("hamrocsv.csv", "w") as file:
# 	writer = csv.writer(file)
# 	writer.writerow(["name", "age"])
# 	writer.writerow(["sahaj", 17])
# 	writer.writerow(["elon", 49])
# 	writer.writerow(["steve", 67])


with open("hamrocsv.csv", "r") as file:
	reader = csv.Dictreader(file)
	for x in reader:
		print(x) 	

