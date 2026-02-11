import csv

def csv_into_list(file_name):
    with open(file_name,"r") as f:
        file_content = csv.reader(f)
        list_w_lists = [line for line in file_content]
        return list_w_lists
print(csv_into_list("text.csv"))
