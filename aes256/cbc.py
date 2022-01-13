from xor import strxor, hex_to_str, str_to_hex
from aes import aes, inv_aes

BLOCK_SIZE = 32


def cbc(key, message, init_vector):
    global BLOCK_SIZE
    pad_length = 16 - (len(message) % 16)
    message += pad_length * chr(pad_length)
    message = str_to_hex(message)
    cipher = init_vector
    block1 = strxor(hex_to_str(init_vector), hex_to_str(message[:BLOCK_SIZE]))
    cipher += aes(key, str_to_hex(block1))
    for i in range(BLOCK_SIZE, len(message), BLOCK_SIZE):
        block = strxor(hex_to_str(cipher[i:i+BLOCK_SIZE]),
                       hex_to_str(message[i:i+BLOCK_SIZE]))
        cipher += aes(key, str_to_hex(block))
    return cipher


def inv_cbc(key, cipher):
    global BLOCK_SIZE
    init_vector = cipher[:BLOCK_SIZE]
    cipher = cipher[BLOCK_SIZE:]
    message = ""
    new_block = inv_aes(key, cipher[:BLOCK_SIZE])
    message += strxor(hex_to_str(new_block), hex_to_str(init_vector))
    for i in range(BLOCK_SIZE, len(cipher), BLOCK_SIZE):
        new_block = inv_aes(key, cipher[i:i+BLOCK_SIZE])
        message += strxor(hex_to_str(cipher[i-BLOCK_SIZE:i]),
                          hex_to_str(new_block))
    message = message[:len(message)-ord(message[-1])]
    return message
