import goroda_db 
from random import choice 
count=0 #счётчик раундов
goroda_copy=goroda_db.goroda().copy()
def first_letter(word):
    first_letter=word[0]
    return first_letter
  ef end_letter(word):
    end_letter=word[len(word)-1]
    if end_letter=='ь' or end_letter=='й' or end_letter=='ы':
        end_letter=word[len(word)-2]
    return end_letter
  def first_turn_comp():
    return choice(goroda_db.goroda())
  def computer_turn(turn_player):
    first_letter_tc=end_letter(turn_player) 
    goroda_copy.remove(turn_player)        
    list=[]
    for i in goroda_copy:         
        if first_letter_tc.upper()==first_letter(i):
            list.append(i)
    choice_comp=choice(list)                 
    goroda_copy.remove(choice_comp)          
    return choice_comp
  turn_comp = print("Ход компьютера: ", first_turn_comp())
turn_player = str(input("Ход игрока, введите слово: "))
while True:
    if turn_player in goroda_copy:
        print("Ход компьютера: ", computer_turn(turn_player))
        turn_player = str(input("Ход игрока, введите слово: "))
        count+=1
    else:
        if turn_player not in goroda_db.goroda():# Проверяем существует вообще город который ввёл игрок или нет
            print("Такого города вообще не существует, раундов сыграно:", count)
            break
        else:
           print("Такой город уже был, раундов сыграно:", count)
           breaks
