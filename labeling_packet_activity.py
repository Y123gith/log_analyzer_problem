import csv

def list_oversized_acces(log_file):
    with open(log_file,"r") as f:
        file = csv.reader(f)
        all_logs = [packet for packet in file ]
        for log in all_logs:
            if int(log[-1]) > 5000:
                log.append("Large")
            else:
                log.append("NORMAL")
    return all_logs