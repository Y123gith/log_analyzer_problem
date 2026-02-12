import csv

def suspicious_acts(log):
    existing_sus = []
    ip_source = log[1]
    access_hour = log[0].split(":")[0]
    access_hour = int(access_hour.split(" ")[1])
    if ip_source[:3]!="10." and ip_source[:7]!= "192.168":
        existing_sus.append("EXTERNAL_IP")
    if int(log[-1]) > 5000: # check packet
        existing_sus.append("LARGE_PACKET")
    if log[-3]=="22" or log[-3]=="23" or log[-3]=="3389": # check port
        existing_sus.append("SENSETIVE_PORT")
    if -1< access_hour < 6:
        existing_sus.append("NIGHT_ACTIVITY")
    return existing_sus

def suspicious_activ_by_ip(log_file):
    with open(log_file,"r") as f:
        file = csv.reader(f)
        for log in file:
           log_w_sus_act = {log[1]:suspicious_acts(log) for log in file}
           return log_w_sus_act
print(suspicious_activ_by_ip("text.csv"))