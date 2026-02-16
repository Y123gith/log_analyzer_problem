import csv

def sus_hor_logs(log_file):
    with open(log_file,"r") as f:
        file = csv.reader(f)
        sus_hour_act = list(filter(lambda log: 0<=int((log[0].split(":",1)[0]).split(" ")[1])<6,file))
        return sus_hour_act