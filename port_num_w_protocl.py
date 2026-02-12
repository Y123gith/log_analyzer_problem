import csv 

def ip_source_access_counter(log_file):
    with open(log_file,"r") as f:
        file = list(csv.reader(f))
        port_l = [log[3]for log in file]
        protocol_l = [log[4]for log in file]
        port_w_proto_dict = {port:protocl for port,protocl in zip(port_l,protocol_l)}
    return port_w_proto_dict