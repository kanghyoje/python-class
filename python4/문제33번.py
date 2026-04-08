apabet = ['a', 'b', 'c', 'd', 'e']

word = input('문자를 입력하세요:')
for i in range(-1, -1 - len(word), -1): # i는 -1 부터 -5까지 -1씩 줄어든다.
    print(word[i], end = '')
    