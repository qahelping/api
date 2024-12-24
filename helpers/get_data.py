import csv


def get_data_from_csv(file: str):
    with open(file, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for el in reader:
            yield el
