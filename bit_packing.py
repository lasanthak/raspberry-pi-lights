def pack_bits(int_array):
    """ Returns an int that represents the given 8 bits (int array). """
    assert len(int_array) == 8
    for bit_val in int_array:
        assert bit_val == 0 or bit_val == 1
    return 128 * int_array[7] + \
           64 * int_array[6] + \
           32 * int_array[5] + \
           16 * int_array[4] + \
           8 * int_array[3] + \
           4 * int_array[2] + \
           2 * int_array[1] + \
           int_array[0]


def unpack_bits(int_value):
    """ Unpack the 8 bits represented by the given int and return an array of ints. """
    return [
        positional_bit_int(int_value, 1),
        positional_bit_int(int_value, 2),
        positional_bit_int(int_value, 4),
        positional_bit_int(int_value, 8),
        positional_bit_int(int_value, 16),
        positional_bit_int(int_value, 32),
        positional_bit_int(int_value, 64),
        positional_bit_int(int_value, 128)
    ]


def positional_bit_int(int_value, position_mask):
    if int_value & position_mask > 0:
        return 1
    else:
        return 0


if __name__ == '__main__':
    for i in range(256):
        assert i == pack_bits(unpack_bits(i))
    print "Bit Packing Test Passed."
