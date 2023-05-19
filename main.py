import array
import random

def PossibleCreateMap(size : int):
    if (abs(size) in [0,1]) :
        return  False;

    return abs(size) % 2  == 1;

def CreateMap(size : int):
    map = [];

    for column in range(size):
        subMap = [];
        for row in range(size):
            subMap.append("#");

        map.append(subMap);

    return map;

def DrawMap(map : array):
    str = "";

    for column in range(len(map)):
        for row in range(len(map[column])):
            str = str + map[column][row];

        print(str);
        str = "";

def SettingMap():
    done = False;

    print("Пример, ввод 3 создаст карту 3 х 3.");
    print("минимальный размер игровой карты 3 x 3. Размеры 0 x 0, 1 x 1  учитываться не будут.")
    while done == False:
        size = input("Ввидите нечётное число = ");

        if (size.isdigit() == False):
            print("Введите число!");
            continue;

        size = int(size);
        done = PossibleCreateMap(size);

    return  size;

def InputUser(title : str, inputText : str):
    if (title != None):
        print(title);

    data = "";

    while True:
        data = input(inputText + "\n");

        if (data.isdigit()):
            break;

        print("Не правильный ввод.");

    return int(data);

def UpdateMap(map: array, user : array, isUser : bool):
    user[1] -= 1;
    user[2] -= 1;

    if (user[1] > len(map) or user[1] < 0):
        if (isUser):
            print("линия выбрана не правильно.");

        return False;

    if (user[2] > len(map[0]) or user[2] < 0):
        if (isUser):
            print("ячейка выбрана не правильно.");

        return False;

    if (map[user[1]][user[2]] != "#"):
        if (isUser):
            print("Эта ячейка уже занята, попробуйте снова.");

        return  False;

    map[user[1]][user[2]] = user[0];
    return  True;

def FindWinner(map : array, symbol : str):
    numberMatches = 0;

    for column in range(len(map)):
        for row in range(len(map[column])):
            if (map[column][row] == symbol):
                numberMatches += 1;

        if (numberMatches == len(map[column])):
            return  True;
        numberMatches = 0;

    numberMatches = 0;

    for column in range(len(map)):
        for row in range(len(map[column])):
            if (map[row][column] == symbol):
                numberMatches += 1;

        if (numberMatches == len(map[column])):
            return True;
        numberMatches = 0;

    numberMatches = 0;

    #\
    for cell in range(len(map)):
        if (map[cell][cell] == symbol):
            numberMatches += 1;

    if (numberMatches == len(map)):
        return True;

    numberMatches = 0;

    #/
    for cell in range(len(map)):
        if (map[cell][(len(map[0]) - 1) - cell] == symbol):
            numberMatches += 1;

    if (numberMatches == len(map)):
        return True;

    return False;

def PossibleToTakeStep(map : array):

    for column in range(len(map)):
        for row in range(len(map[column])):
            if (map[column][row] == "#"):
                return  True;

    return  False;

def BotStep(map : array,bot : array):

    while(True):
        bot[1] = random.randint(0,len(map));
        bot[2] = random.randint(0,len(map));

        if (UpdateMap(map,bot,False)):
            break;

def Game():
    size = SettingMap();
    map = CreateMap(size);

    player = ["x",1,1];
    bot = ["o",1,1];

    while True:
        DrawMap(map);

        if (PossibleToTakeStep(map) == False):
            print("Удивительно, но у нас ничья! Все молодцы!");
            break;

        if (FindWinner(map, player[0])):
            print("You win!");
            break;

        if (FindWinner(map, bot[0])):
            print("You lose!");
            break;

        player[1] = InputUser(None,"введите число которое"
                                   " означает номер линии"
                                   " который вы выбрали.");
        player[2] = InputUser(None, "введите число которое"
                                   " означает номер ячейки"
                                   " которой вы выбрали.");

        if (UpdateMap(map,player,True) == False):
            continue;

        if (PossibleToTakeStep(map) == False):
            continue;

        BotStep(map,bot);





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Game();

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
