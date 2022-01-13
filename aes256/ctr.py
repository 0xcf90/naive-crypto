from xor import strxor, hex_to_str, str_to_hex
from aes import aes

BLOCK_SIZE = 32


def gen_keys(key, init_vector, length):
    key_array = []
    for i in range(length):
        counter = hex(int(init_vector, 16) + i)[2:]
        key_array.append(aes(key, counter))
    return key_array


def ctr(key, message, init_vector):
    cipher = ""
    message = str_to_hex(message)
    if len(message) % BLOCK_SIZE == 0:
        length = len(message) / BLOCK_SIZE
    else:
        length = (len(message) // BLOCK_SIZE) + 1
    key_array = gen_keys(key, init_vector, length)
    for i in range(length):
        cipher += strxor(hex_to_str(key_array[i]),
                         hex_to_str(message[BLOCK_SIZE*i:BLOCK_SIZE*(i+1)]))
    return str_to_hex(cipher)


def inv_ctr(key, cipher):
    init_vector = cipher[:BLOCK_SIZE]
    cipher = cipher[BLOCK_SIZE:]
    if len(cipher) % BLOCK_SIZE == 0:
        length = len(cipher) / BLOCK_SIZE
    else:
        length = (len(cipher) // BLOCK_SIZE) + 1
    key_array = gen_keys(key, init_vector, length)
    message = ""
    for i in range(length):
        message += strxor(hex_to_str(key_array[i]),
                          hex_to_str(cipher[BLOCK_SIZE*i:BLOCK_SIZE*(i+1)]))
    return message
