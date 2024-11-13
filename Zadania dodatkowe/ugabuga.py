
def main():
    arr = []
    flag = True
    while flag:
        word = input()
        arr.append(word)
        if word == "quit":
            flag = False
    
    maxl = 0
    for word in arr:
        if len(word) > maxl:
            maxl = len(word)
    
    dict = {}
    
    for i in range(maxl):
        new_data = {i+1 : []}
        dict.update(new_data)
    
    for word in arr:
        current_len = len(word)
        temp_list = dict[current_len]
        temp_list.append(word)
        dict[current_len] = temp_list


    print(dict)
    
    
    
    for key in dict.keys():
        if len(dict[key]) >0 : print(key, " --> ", sorted(dict[key]))


main()