place = [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"]
                        ]

# UI

def plaing_place(place):
    print(f"  0 1 2")
    for i in range(3):
        print(f"{i} {place[i][0]} {place[i][1]} {place[i][2]}")

# победитель
def victory():
    x = "X"
    y = "0"

    # горизонталь
    for i in place:
        if i == [y, y, y]:
            print(i)
            print("Игрок 2 победил")
            return True
        if i == [x, x, x]:
            print(i)
            print("Игрок 1 победил")
            return True

    # вертикаль
    res = ["-", "-", "-"]
    for i in range(3):
        for k in range(3):
            res[k] = place[k][i]

        if res == [x,x,x]:
            print("Игрок 1 выиграйл")
            return True
        if res == [y,y,y]:
            print("Игрок 2 выйграл")
            return True

    # диагональ
    p1 = place[0][0]
    p2 = place[1][1]
    p3 = place[2][2]
    p4 = place[0][2]
    p5 = place[2][0]

    one = ((p1 == x and p2 == x and p3 == x) or (p4 == x and p2 == x and p5 == x))
    two = ((p1 == y and p2 == y and p3 == y) or (p4 == y and p2 == y and p5 == y))

    if one:
        print("Игрок 1 выйграл")
        return True
    if two:
        print("Игрок 2 выйграл")
        return True
    else:
        return False

# кондишонс

def conditions():
    while True:
        coordinates = input("Введите координаты: ").replace(",", " ").split()

        if len(coordinates) != 2:
            print("Введите обе координаты")
            continue

        x, y = coordinates
        if not(x.isdigit()) or not(y.isdigit()):
            print("Одна или обе координаты не являются числами")
            continue

        x, y = int(x), int(y)
        if x < 0 or x > 2 or y < 0 or y > 2:
            print("Координаты введены не верно")
            continue
        if place[x][y] != '-':
            print("Клетка занята")
            continue

        else:
            return x, y

# цикл

mov = 0
while True:
    mov += 1
    plaing_place(place)
    if mov % 2 == 1:
        print(f"Ход первого игрока:")
    else:
        print(f"Ход второго игрока:")

    x,y = conditions()
    if mov % 2 == 1:
        place[x][y] = "X"
    # else:
    if mov % 2 == 0:
        place[x][y] = "0"
    if victory():
        plaing_place(place)
        break
    if mov == 9:
        print(f"Ничья")
        break

