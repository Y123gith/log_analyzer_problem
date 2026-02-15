import csv
# returns a matrix with lists of the logs which accessed sensitive ports
def sus_port_act(log_file):
    with open(log_file,"r") as f:
        file = csv.reader(f)
        return list(filter(lambda log:log[-3]=="22"or log[-3]=="23" or log[-3]=="3389",file))
    
print(sus_port_act("text.csv"))