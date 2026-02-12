import csv

def hour_logs(log_file):
    with open(log_file,"r") as f:
        file = csv.reader(f)
        hours = list(map(lambda row:int(row[0].split(" ")[1].split(":")[0]) ,file))
    return hours