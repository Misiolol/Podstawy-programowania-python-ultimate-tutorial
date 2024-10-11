def check_palindrome(text):
    return text == text[::-1]

def validate_palindrome(text, start, end, remove_count):
    while start < end:
        if text[start] != text[end]:
            if remove_count == 0:
                return False
            return validate_palindrome(text, start + 1, end, remove_count - 1) or validate_palindrome(text, start, end - 1, remove_count - 1)
        start += 1
        end -= 1
    return True

input_text = input()
input_text = input_text.lower()

if validate_palindrome(input_text, 0, len(input_text) - 1, 2):
    print("YES")
else:
    print("NO")