from ip_w_suspicious_activ import suspicious_acts,suspicious_activ_by_ip

def sevral_sus_act(log_file)
    dict_with_sus_act = suspicious_activ_by_ip(log_file)
    over_two_sus_activity = {key:dict_with_sus_act[key] for key in dict_with_sus_act if len(dict_with_sus_act[key])>1}