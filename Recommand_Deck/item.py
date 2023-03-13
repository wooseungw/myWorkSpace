#이벤트 핸들링 ai에게 자료제공 
#라위 무대 비파 쇼진 마공총
import sys
#"칼","곡궁","조끼","망토",지팡이,여눈,벨트,장갑,뒤집개
item_input = [0]


buff = sys.stdin.readline().split(" ")

buff_lenght = len(buff)

buff[buff_lenght-1] = buff[buff_lenght-1].strip()

for i in buff:
    if i =="칼":
        item_input[0] += 1
    elif i == "곡궁":
        item_input[1] += 1
    elif i =="쪼끼":
        item_input[2] += 1
    
print(buff)