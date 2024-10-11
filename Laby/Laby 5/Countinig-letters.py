from collections import Counter

def most_frequent_letter(sentence):
    plain_text = ""
    for i in range(len(sentence)):
        for char in sentence[i]:
            #print(char)
            if char.isalpha():
                plain_text+=char.lower()
            else:
                continue
    #print(plain_text)
    letter_counts = Counter(plain_text)
    max_count = max(letter_counts.values())
    solution = [letter for letter, count in letter_counts.items() if count == max_count]
    return min(solution)


sentence = list(input().split())
print(most_frequent_letter(sentence))
