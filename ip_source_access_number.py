import csv 

def ip_source_access_counter(log_file):
    with open(log_file,"r") as f:
        file = list(csv.reader(f))
        ip_sources = [ip[1] for ip in file]
        count_access_by_ip = {ip:ip_sources.count(ip) for ip in ip_sources}
    return count_access_by_ip
print(ip_source_access_counter("text.csv"))