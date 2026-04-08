import random
start = random.randint(1, 9)          
end = random.randint(start, 10)
hap = 0
for i in range(start, end + 1):
    hap += i
print(f"{start} ~ {end} => {hap}")