from bitstring import BitArray

CP_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

SHIFT = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

CP_2 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]


PI = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

S_BOX = [
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
    ],

    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
    [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
    ],

    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
    [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
    [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
    [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
    ],

    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
    ],  

    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
    [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
    [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
    [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
    ], 

    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
    [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
    [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
    [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
    ], 

    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
    [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
    [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
    [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
    ],
    
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
    [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
    [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
    [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
    ]
]


P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]


PI_1 = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]

def permute(num, index):
    s = ''
    for i in index:
        s += num.bin[i-1]
    s = BitArray(bin='0b'+s)
    return s


def split_half(num):
    l = len(num.bin) // 2
    c = num.bin[:l]
    d = num.bin[l:]
    c = BitArray(bin='0b'+c)
    d = BitArray(bin='0b'+d)
    return c,d

def split_eighth(num):
    assert len(num.bin) == 48
    res = []
    for i in range(8):
        s = num.bin[i*6 : (i+1)*6]
        s = BitArray(bin='0b'+s)
        res += [s]
    return res

def reduce_sbox(num, box):
    assert len(num.bin) == 6
    row = int(num.bin[0]+num.bin[-1], 2)
    col = int(num.bin[1:5], 2)
    t = box[row][col]
    res = BitArray(uint=t, length=4)
    return res


def gen_subkey_from_cd(c,d):
    t = BitArray(bin='0b'+c.bin+d.bin)
    subkey = permute(t, CP_2)
    return subkey

def f(r, k):
    r_expand = permute(r, E)
    rk = r_expand ^ k
    rk8 = split_eighth(rk)
    res = ''
    for i, s in enumerate(rk8):
        t = reduce_sbox(s, S_BOX[i])
        res += t.bin
    res = BitArray(bin='0b'+res)
    res = permute(res, P)
    return res

def encodeLR(l, r, k):
    new_L = r
    new_R = l ^ f(r, k)
    return new_L, new_R


def fnum(num):
    s = ''
    l = len(num.bin) // 4
    for i in range(l):
        s += num.bin[i*4 : (i+1)*4] + ' '
    return s

# Step 1: create 16 subkeys, 48 bits long

def gen_keys(K):
    # permute K, 64 bit -> 58 bit
    K_plus = permute(K, CP_1)

    # Split K+ to C0, D0
    C0, D0 = split_half(K_plus)

    C = [C0]
    D = [D0]

    # Rotate C0,D0 to generate 16 Cs, Ds
    for i in range(1,17,1):
        bit_shift = SHIFT[i-1]
        ci = C[-1].copy()
        di = D[-1].copy()
        ci.rol(bit_shift)
        di.rol(bit_shift)
        C += [ci]
        D += [di]   

    SUBKEY = []

    # Generate 16 subkeys from 16 Cs, Ds
    for i in range(1,17,1):
        sk = gen_subkey_from_cd(C[i], D[i])
        SUBKEY += [sk]

    return SUBKEY 

# Step 2: encode
def encrypt(M, K):
    SUBKEY = gen_keys(K)

    # Permute message M with PI
    M_permute = permute(M, PI)
    
    # Split M_permute to L, R 64 bits -> 32 bits, 32 bits
    L, R = split_half(M_permute)

    # Encode L, R 16 times with subkey
    for i in range(16):
        L, R = encodeLR(L, R, SUBKEY[i])

    # Concat L,R
    CIPHER = BitArray(bin='0b'+R.bin+L.bin)

    # Reverse 
    CIPHER = permute(CIPHER, PI_1)

    return CIPHER

def decrypt(M, K):
    # Reverse Subkey
    SUBKEY = gen_keys(K)[::-1]

    # Permute message M with PI
    M_permute = permute(M, PI)
    
    # Split M_permute to L, R 64 bits -> 32 bits, 32 bits
    L, R = split_half(M_permute)

    # Encode L, R 16 times with subkey
    for i in range(16):
        L, R = encodeLR(L, R, SUBKEY[i])

    # Concat L,R
    Mess = BitArray(bin='0b'+R.bin+L.bin)

    # Reverse 
    Mess = permute(Mess, PI_1)

    return Mess

M = BitArray(hex='0x56cc09e7cfdc4cef')
K = BitArray(hex='0x0123456789ABCDEF')

c = decrypt(M, K)

print(c.hex)