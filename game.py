import random

MonsterHp = 120
PlayerHp = 100

while MonsterHp > 0 and PlayerHp > 0:
    print('스킬의 종류:')
    print('1. 일반공격(데미지:10~20)')
    print('2. 연속공격(데미지:5~10)')
    print('3. 필살기(데미지:40~60)')
    print('4. 피 채우기(힐:10~15)')
    
    skill = input()

    if skill == '1':
        MonsterHp -= random.randint(10, 20)
        print('몬스터 HP는 :', MonsterHp)
        if MonsterHp > 0:
            PlayerHp -= random.randint(10, 20)
            print('몬스터가 공격하였다. 플레이어 HP는 :', PlayerHp)
            
    elif skill == '2':
        MonsterHp -= random.randint(5, 10)
        print('몬스터 HP는 :', MonsterHp)
        MonsterHp -= random.randint(5, 10)
        print('몬스터 HP는 :', MonsterHp)
        MonsterHp -= random.randint(5, 10)
        print('몬스터 HP는 :', MonsterHp)

        if MonsterHp > 0:
            PlayerHp -= random.randint(10, 20)
            print('몬스터가 공격하였다. 플레이어 HP는 :', PlayerHp)
            
    elif skill == '3':
        MonsterHp -= random.randint(40, 60)
        print('몬스터 HP는 :', MonsterHp)
        if MonsterHp > 0:
            PlayerHp -= random.randint(20, 30)
            print('몬스터가 공격하였다. 플레이어 HP는 :', PlayerHp)

    elif skill == '4':
        PlayerHp += random.randint(10, 15)
        print('플레이어가 힐을 하였다.', PlayerHp)
        PlayerHp -= random.randint(10, 20)
        print('몬스터가 공격하였다. 플레이어 HP는 :', PlayerHp)
         
    else:
        print('다시 입력하시오.')
    
    if MonsterHp <= 0 or PlayerHp <= 0:
        break

if MonsterHp <= 0 and PlayerHp <= 0:
    print('비겼습니다.')
elif MonsterHp <= 0:
    print('승리하였습니다.')
else:
    print('패배하였습니다.')