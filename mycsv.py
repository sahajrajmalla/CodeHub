import csv


with open("csvfile.csv", "w", newline="") as file_write:
    writer = csv.writer(file_write)
    writer.writerow(["full name", "city", "country"])


def appendtable(name, city, country):
    with open("csvfile.csv", "a", newline="") as file_append:
        appender = csv.writer(file_append)
        appender.writerow([name, city, country])


appendtable("sahaj raj malla", "banepa", "nepal")
appendtable("steve jobs", "silicon valley", "USA")
appendtable("albert einstein", "berlin", "germany")
appendtable("elon musk", "california", "USA")
