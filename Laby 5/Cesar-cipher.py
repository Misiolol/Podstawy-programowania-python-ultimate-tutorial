def encrypt(text, n):
    encrypted = ""
    for char in text:
        if (char.isupper()):
            encrypted += chr((ord(char)-n-65) % 26 + 65)
        else:
            encrypted += chr((ord(char)-n-97) % 26 + 97)
    return encrypted


n = int(input())
message = list(input())

print(encrypt(message, n))