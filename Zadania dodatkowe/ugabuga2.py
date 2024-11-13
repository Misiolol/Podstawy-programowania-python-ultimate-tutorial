
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
    
    
    extra_list = []
    for key in dict.keys():
        if len(dict[key]) >0:
            new_row = [key, dict[key]]
            extra_list.append(new_row)

    

    print(extra_list)
    extra_list.sort(key=lambda x:len(set(x[1])), reverse=True)
    print(extra_list)

main()