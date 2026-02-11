import csv

def list_sensitive_acces(log_file):
    with open(log_file,"r") as f:
        file = csv.reader(f)
        list_sensitve_acces_logs = [port for port in file if port[3]=="22" or port[3]=="23" or port[3]=="3389"]
    return list_sensitve_acces_logs