def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])


def hex_to_str(hex_string):
    char_list = []
    for i in range(len(hex_string)//2):
        char_list.append(chr(int(hex_string[(2*i):(2*i+2)], 16)))
    return "".join(char_list)


def str_to_hex(string):
    hex_string = ""
    for i in string:
        char = str(hex(ord(i)))
        if len(char) < 4:
            hex_string += "0" + char[-1]
        else:
            hex_string += char[-2:]
    return hex_string
