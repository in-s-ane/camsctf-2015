import binascii
file_nums = [ 1
            , 2
            , 3
            , 4
            , 6
            , 7
            , 10
            , 11
            , 17
            , 20
            , 21
            , 22
            , 25
            , 29
            , 31
            , 33
            , 35
            , 36
            , 37
            , 38
            , 39
            , 41
            , 43
            , 44
            , 46
            , 49
            , 53
            , 55
            , 57
            , 59
            , 62
            , 66
            , 67
            , 73
            , 75
            , 76
            , 77
            , 78
            , 79
            , 82
            , 83
            , 89
            , 92
            , 93
            , 94
            , 97
            , 101
            , 103
            , 105
            , 106
            , 107
            , 108
            , 109
            , 111
            ]

bin_str = ''
for i in range(0, 112):
    if i in file_nums:
        bin_str += '1'
    else:
        bin_str += '0'

print binascii.unhexlify('%x' % int(bin_str, 2))
