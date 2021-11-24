n=int(input())
teams_score=[input().split(';') for t in range(n)]

score={} # словарь для всех баллов

for elem in teams_score:
    for i in elem:
        if not i.isdigit():
            score[i]=[0, 0, 0, 0, 0] # этим обходом мы получаем требуемый словарь с неповторяющимися командами
                     # [Всего_игр, Побед, Ничьих, Поражений, Всего_очков]
for T in teams_score:
    if int(T[1])>int(T[3]):
            score[T[0]][1]+=1 # +победа
            score[T[2]][3]+=1 # +поражение
            score[T[0]][0]+=1 # +игра
            score[T[2]][0]+=1 # +игра
            score[T[0]][4]+=3 # +3 балла
    elif int(T[1])<int(T[3]):
            score[T[2]][1]+=1 # +победа
            score[T[0]][3]+=1 # +поражение
            score[T[0]][0]+=1 # +игра
            score[T[2]][0]+=1 # +игра
            score[T[2]][4]+=3 # +3 балла
    elif int(T[1])==int(T[3]):
            score[T[0]][2]+=1 # +ничья
            score[T[2]][2]+=1 # +ничья
            score[T[0]][0]+=1 # +игра
            score[T[2]][0]+=1 # +игра
            score[T[0]][4]+=1 # +балл
            score[T[2]][4]+=1 # +балл
            
for el in score:
    print(el+':', end='')
    print(*score[el])

    #3
#Спартак;9;Зенит;10
#Локомотив;12;Зенит;3
#Спартак;8;Локомотив;15