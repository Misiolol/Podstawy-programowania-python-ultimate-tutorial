def main():
    number_of_rectangles = int(input())
    arr = []
    for _ in range(number_of_rectangles):
        arr.append(int(input()))

    biggest_rectangle = 0
    for height in range(1, max(arr)):
        current_size = 0
        for digit in arr:
            if digit >= height:
                current_size += height
            else:
                if current_size > biggest_rectangle:
                    biggest_rectangle = current_size
                current_size = 0
            if current_size > biggest_rectangle:
                biggest_rectangle = current_size

    print(biggest_rectangle)

main()
            
