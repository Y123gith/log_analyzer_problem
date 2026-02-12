
def list_byte_to_kbytes(byte_list):
    kbytes_list = list(map(lambda value: int(str(value)[0]),byte_list))
    return kbytes_list