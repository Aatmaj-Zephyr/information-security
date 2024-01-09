def playfair(key, plaintext):
    plaintext = plaintext.replace("i", "j")
    matrix = make_matrix_from_key(key)
    pairs = make_pairs(plaintext)
    answer = crypt(pairs, matrix)
    print(answer)
    # print(matrix)


def crypt(pairs, matrix):
    answer = []
    for pair in pairs:
        answer.append(crypt_pair(pair, matrix))

    return answer


def crypt_pair(pair, matrix):
    # print(matrix)
    first = matrix.index(pair[0])
    second = matrix.index(pair[1])
    div_1, mod_1 = divmod(first, 5)
    div_2, mod_2 = divmod(second, 5)

    # check if both are in the same row
    if div_1 == div_2:
        mod_1 = (mod_1 + 1) % 5
        mod_2 = (mod_2 + 1) % 5

    elif mod_1 == mod_2:  # column same
        div_1 = (div_1 + 1) % 5
        div_2 = (div_2 + 1) % 5

    else:
        mod_1,mod_2 = mod_2,mod_1
    first = div_1*5+mod_1
    second = div_2*5+mod_2
    return (matrix[first], matrix[second])


def make_pairs(plaintext):
    # plaintext+='z'
    pairs = []
    i = 0
    while i <= len(plaintext) - 1:
        if i == len(plaintext) - 1:
            pairs.append((plaintext[i], "z"))
            break

        if plaintext[i] != plaintext[i + 1]:
            pairs.append((plaintext[i], plaintext[i + 1]))
            i += 1
        else:
            pairs.append((plaintext[i], "x"))
        i += 1

    return pairs


def make_matrix_from_key(key):
    length = 5
    alphabets = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    for i in alphabets:
        if i not in key:
            key += i
    answer = []
    if len(key) != length**2:
        for i in range(length**2 - len(key)):
            key += " "
    for i in range(length):
        # answer.append([])
        for j in range(length):
            answer.append(key[length * i + j])
    return answer


print(playfair("monarchy", "aatmaj"))
