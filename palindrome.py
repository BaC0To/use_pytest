def is_palindrome(some_data:str):
    some_data = some_data.replace(' ', '').lower()
    split = len(some_data) // 2

    if len(some_data) % 2 == 0:
        left = some_data[:split]
        right = some_data[split:]
    else:
        left = some_data[:split]
        right = some_data[split+1:]

    return left == right[::-1]


#result = is_palindrome('BOOB')
#print(f'Word result is palindrome? --> {result}')