def solution(sentence):
    vowels = set('aeiouyAEIOUY')
    sol = ""
    for word in sentence:
        for char in word:
            if char not in vowels:
                sol+=char
            else:
                continue
        sol+=" "
    return sol
    
sentence = list(input().split())
print(solution(sentence))