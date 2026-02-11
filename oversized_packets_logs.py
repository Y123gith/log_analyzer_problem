import csv

def list_oversized_acces(log_file):
    with open(log_file,"r") as f:
        file = csv.reader(f)
        oversized_packets_logs = [packet for packet in file if int(packet[-1])>5000]
    return oversized_packets_logs