# написать простейшую игру дурак
import random
from operator import itemgetter, attrgetter, methodcaller

#-------Колода------------------------------------------------------------------------
bubna = [('6_b', 1), ('7_b', 2), ('8_b', 3), ('9_b', 4), ('10_b', 5), ('V_b', 6), ('D_b', 7), ('K_b', 8), ('T_b', 9)]
cherva = [('6_ch', 1), ('7_ch', 2), ('8_ch', 3), ('9_ch', 4), ('10_ch', 5), ('V_ch', 6), ('D_ch', 7), ('K_ch', 8), ('T_ch', 9)]
pika = [('6_p', 1), ('7_p', 2), ('8_p', 3), ('9_p', 4), ('10_p', 5), ('V_p', 6), ('D_p', 7), ('K_p', 8), ('T_p', 9)]
kresti = [('6_k', 1), ('7_k', 2), ('8_k', 3), ('9_k', 4), ('10_k', 5), ('V_k', 6), ('D_k', 7), ('K_k', 8), ('T_k', 9)]
koloda = [bubna,  cherva, pika, kresti]

#-----Автоматизировать выбор козыря----------------------------------------------------------------------

mast_kosir = random.choice(koloda) # нужно сделать на вывод название одного из листа(масти)???
#print(mast_kosir)

#Перемешать колоду----------------------------------------------------------------------------------
#-------- способ от Марата--------------------
vse_karty = []

for sh_koloda in koloda:
    random.shuffle(sh_koloda)
    vse_karty.extend(sh_koloda)
    #здесь используем не append, с которым во vse_karty окажется 4 списка со вложенными элементами, а extend,
    # который просто расширяет изначальный список элементами очередного списка, разницу можете увидеть, выведя
    # на принт и так и так
#print(vse_karty)


#------------------Раздача карт игрокам и удаление их с колоды--------------------------------------------
#раздача карт игроку 1-----------------------------------------------
player_1 = []
player_1 = random.sample(vse_karty, k=6)
#print(f'Карты игрока 1: {player_1}')
for kards_player in player_1:
    vse_karty.remove(kards_player)
#print(f'Удаление карт первого ирока из колоды {vse_karty}')

#----------Раздача карт игроку КОМП после удаления карт 1-го игрока из колоды(vse_karty)
player_comp = []
player_comp = random.sample(vse_karty,k=6)
print(len(vse_karty), len(player_1))
print(f'Карты КОМП игрока {player_comp}')
for kards_comp in player_comp:
    vse_karty.remove(kards_comp)
#print(f'Удаление карт игрока из колоды: {vse_karty}')
print(len(vse_karty), len(player_comp))

#-----------Проверка на совпадение карт игроков
for card_player in player_1:
    for card_comp in player_comp:
        if card_comp == card_player:
            print('Совпадение карт игроков')
            break

#--------------------------------------------------------------------------------------------------------
#--------------Сделать ходы игроков и уменьшение карт игроков--------------------------------------------
print(f'Ваши карты: {player_1}')
print(f'Козырь: {mast_kosir}')
print(f'Так как начало игры ходит игрок у которого наименьший козырь.')
#-----------Сравниваю с козырной мастью и козырем игроков

#---------блок кто первый ходит---------------------------------------------------------------------------------------
kozir_player = []
kozir_komp = []
card_kozir_sort = []
player_1.sort()
mast_kosir.sort()
# card_kozir_sort = sorted(mast_kosir, key=itemgetter(1))
# card_player_sort = sorted(player_1, key=itemgetter(1))
# card_comp_sort = sorted(player_comp, key=itemgetter(1))
#--------------------Не получается козырь найти минимальный у игроков
for kozir in mast_kosir:
    for player in player_1:
        if player == kozir:
            kozir_player.append(player)
            kozir_player.sort()
        else:                          # Если козыря не то пишет что выходит за пределы списка
            print('У вас козыря нет') # Много повторяется
print(f'Младший козырь у игрока: {kozir_player[0]}')  # Здесь пишет Иногда что выходит за
                                                                    # пределы списка - list index out of range?

#-------------------Младший козырь компа
player_comp.sort()
# #card_comp_sort = sorted(player_comp, key=itemgetter(1))
for kozir_c in mast_kosir:
    for player_c in player_comp:
        if player_c == kozir_c:
            kozir_komp.append(player_c)
            kozir_komp.sort()

        else:                               #Если козыря не то пишет что выходит за пределы списка
            print('У компа козыря нет')  # Много повторяется
print(f'Младший козырь у КОМП: {kozir_komp[0]}')#Здесь пишет Иногда что выходит за  пределы списка - list index out of range?

komp_step = []
if kozir_player[0] < kozir_komp[0]:
    print(f'Вы ходите первым ')
    #p_1 = input('Введите номер карты по порядку какую Вы считаете нужной ходить: ')
else:
    print('Компьютер ходит первым')
    komp_step = sorted(player_comp, key=itemgetter(1))

    print(f'Компьютер ходит такой картой:{komp_step[0]}')# Не выдает минимальную карту
#-------------------------------------------------------------------------------

#---------------Блок сделать ход--------------------------------------
komp_step = []
#komp_step.append(sorted(player_comp))
#print(min(komp_step)) # Не выдает минимальную карту сортировкой
# komp_step = sorted(player_comp, key=itemgetter(1))
# print(komp_step[0])