hang = int(input("행 수(홀수): "))

mid = hang // 2  
for i in range(hang):
    if i <= mid:
        star = 2 * i + 1
    else:
        star = 2 * (hang - i - 1) + 1
    space = (hang - star) // 2
    print(" " * space + "*" * star)