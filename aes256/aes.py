from xor import hex_to_str, str_to_hex
from blocks import StateBlock, KeyBlock


def gen_keys(cipher_key):
    key_array = [cipher_key]
    key_state_array = []
    for i in range(10):
        key_array.append(key_array[i].NextKey())
    for i in range(11):
        key_state_array.append("".join(key_array[i].state))
    return key_state_array


def aes(key, block):
    state = StateBlock(hex_to_str(block))
    cipher_key = KeyBlock(hex_to_str(key), 0)
    key_array = gen_keys(cipher_key)
    state.AddRoundKey(key_array[0])
    for i in range(1, 10):
        state.SubBytes().ShiftRows().MixColumns().AddRoundKey(key_array[i])
    state.SubBytes().ShiftRows().AddRoundKey(key_array[10])
    return str_to_hex("".join(state.state))


def inv_aes(key, block):
    state = StateBlock(hex_to_str(block))
    cipher_key = KeyBlock(hex_to_str(key), 0)
    key_array = gen_keys(cipher_key)
    state.AddRoundKey(key_array[10])
    state.InverseSubBytes().InverseShiftRows()
    for i in range(9, 0, -1):
        state.AddRoundKey(key_array[i])
        state.InverseMixColumns().InverseSubBytes().InverseShiftRows()
    state.AddRoundKey(key_array[0])
    return str_to_hex("".join(state.state))
