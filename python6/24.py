import random
user = list(map(int, input("세 수를 입력하세요:").split()))

random.shuffle(user)

print(f"두 번째 수는 {user[1]} 입니다.")