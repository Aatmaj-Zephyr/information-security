def transposition(key,string):
    length=len(key)
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


def arranger(key):
    sorted_list=sorted(key)
    answer = []
    for i in key:
       answer.append(sorted_list.index(i))
    return answer

def decrypt(key,plaintext):
    length = len(key)
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
 
   

ciphertext=transposition("hack","aatmaj")
print(ciphertext)
plaintext = decrypt("hack",ciphertext)
print(plaintext)
