def sus_checks(func_call_reason):

    suspicion_checks ={"EXTERNAL_IP": lambda row: str(row[1])[:7]!="192.168" or str(row[1])[:3]!="10.",
        "SENSITIVE_PORT": lambda row: row[3]=="22" or row[3]=="23" or row[3]=="3389", "LARGE_PACKET":
        lambda row: int(row[-1])>5000, "NIGHT_ACTIVITY": lambda row: 0<=int((row[0].split(":",1)[0]).split(" ")[1])<6}
    
    return sus_checks