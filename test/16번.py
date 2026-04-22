sentence = input().split()
dic = {}

for word in sentence:
  dic[word] = len(word)

max_word = max(dic, key=dic.get)
print(max_word)