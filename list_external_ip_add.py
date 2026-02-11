import csv

def list_external_ips(log_file):
    with open(log_file,"r") as f:
        file = csv.reader(f)
        list_source_ips = [ip[1] for ip in file]
    external_source_ips = [ip for ip in list_source_ips if ip[:3]!="10." and ip[:7]!="192.168"]
    return external_source_ips
