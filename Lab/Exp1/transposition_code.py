def transposition(key,string):
    length=len(key)
    matrix = make_matrix_from_key(string,length)
    arranged = arranger(key)
    matrix=[matrix[i] for i in arranged]
    return matrix

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

print(transposition("hack","geeks for geeks"))
