def transposition(key,string):
    length=key
    matrix = make_matrix_from_key(string,length)
    arranged = arranger(key)
    matrix= list(zip(*matrix))
    matrix_cpy = list(matrix) # shallow copy
    for ctr in range(len(arranged)):
        matrix_cpy[arranged[ctr]] = matrix[ctr]
    ans=""
    for i in matrix_cpy:
        for j in i:
          ans+=j
    return ans

def make_matrix_from_key(string,length):
    answer = []
    if(len(string)!=length**2):
        for i in range(length**2-len(string)):
            string+=" "
    for i in range(length):
        answer.append([])
        for j in range(length):
            answer[i].append(string[length*i+j])
    return answer


def arranger(keylen):
   
    return range(keylen)

def decrypt(key,plaintext):
    length = key
    matrix = make_matrix_from_key(plaintext,length,)
    arranged = arranger(key)
   
    matrix_cpy = list(matrix) # shallow copy
    for ctr in range(len(arranged)):
        matrix_cpy[ctr] = matrix[arranged[ctr]]
    matrix_cpy= list(zip(*matrix_cpy))
    ans=""
    for i in matrix_cpy:
        for j in i:
          ans+=j
    return ans
 
keylen=3
ciphertext=transposition(keylen,"aatmaj")
print(ciphertext)
plaintext = decrypt(keylen,ciphertext)
print(plaintext)
