from collections import Counter

def check_number_dict(dictionary, number: int):
    for i in range(len(dictionary)):
        if(dictionary[i][0] == number):
            return True
    return False


def add_number_dict(dictionary, number: int):
    dictionary.append([number, number_of_occurences[number]])

def remove_number_dict(dictionary, number: int):
    idx_to_erase = 0
    if check_number_dict(dictionary, number):
        for i in range(len(dictionary)):
            if dictionary[i][0] == number:
                idx_to_erase = i
    dictionary.remove(dictionary[idx_to_erase])



k = int(input())
arr = []
for _ in range(k):
    arr.append(int(input()))

number_of_occurences = Counter(arr)
digit_set = set(arr)
alternative_dictionary = []
for digit in digit_set:
    add_number_dict(alternative_dictionary, digit)


#?Running functions
print(alternative_dictionary)
print(check_number_dict(alternative_dictionary, 3))
remove_number_dict(alternative_dictionary, 3)
print(alternative_dictionary)
print(check_number_dict(alternative_dictionary, 3))