
user_input = input()


jumin, gender_num = user_input.split(',')


age = 2025 - (1900 + int(jumin[:2])) + 1


gender = "남성" if gender_num.strip() == "1" else "여성"


print(f"현재나이 {age}살 {gender}입니다")