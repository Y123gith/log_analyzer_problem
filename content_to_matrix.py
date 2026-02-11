def csv_into_list(file_name):
    list_w_str,list_w_lists = [],[]
    with open(file_name,"r") as f:
        file_content = f.readlines()
        for content in file_content:
            if "\n" in content:
                content = content.replace("\n","")
            list_w_str.append(content)
            list_w_lists.append(list_w_str.copy())
            list_w_str.clear()
    return list_w_lists