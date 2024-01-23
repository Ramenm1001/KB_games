'''''
import random
input("enter - бросить кубик")
pc1 = random.randint(1, 6)
bc1 = random.randint(1, 6)
print(f"У вас выпало {pc1}, а у противника {bc1}")

input("Второй раунд")
pc2 = random.randint(1, 6)
bc2 = random.randint(1, 6)
print(f"У вас выпало {pc2}, а у противника {bc2}")
cube1 = pc1 + pc2
cube2 = pc2 + bc2
print(f"Итог: у вас {cube1}, у соперника {cube2}")
if cube1 > cube2:
    print("Победа!")
if cube1 < cube2:
    print("Повезёт в следущий раз...")
else:
    print("Ничья")

'''''
'''''
import random

enemy_names = ["Arab with awm", "Pudge", "Gattsu", "Bear", "Visp", "Jason", "Mega knight", "Joker", "Girl with surprise" , "Sl1vko", "Kricup"]

hp = 100
max_hp = 100
attack = 20
exp = 0
max_exp = 10
fox_hp = 50
fox_hp_max = 50
fox_attack = 5
fox_attack_max = 25
print("Вы - элитный боец короля. Он дал вам задание уничтожить всю нечесть, которая обитает в лесу. Вы шли на задание по лесу и увидели лиса. У вас с собой было мясо, поэтому вам удалось приручить его. "
      "На ва шем пути полно врагов. Теперь к вашей задачи прибавилось ещё и не потерять нового друга в бою.")
while hp > 0:
    print("Вам на пути попался")
    enemy = random.choice(enemy_names)
    enemy_hp = random.randint(1, 150)
    enemy_attack = 45 - random.randint(1, enemy_hp // 3)
    while hp > 0 and enemy_hp > 0 and fox_hp > 0:
        print(f"{enemy} {enemy_hp}hp {enemy_attack}dmg")
        print(f"Вы: {hp}hp {attack}dmg {exp}/{max_exp}exp")
        print(f"Fox: {fox_hp}hp {fox_attack}dmg")
        print("1-25% крит")
        print("2-щелбан")
        print("3-run, forest, run")



        # Ход игрока
        ans = int(input("Ваши действия:"))
        if ans == 3:
            hp -=5
            break
        if ans == 1:
            if random.randint(1, 100) > 75:
                enemy_hp = enemy_hp - attack * 3
        elif ans == 2:
            enemy_hp = enemy_hp - attack - fox_attack




        if enemy_hp > 0:
         hp -= enemy_attack
         fox_hp -= enemy_attack / 2
    if hp > 0 and fox_hp > 0:
        exp += enemy_attack // 5
        hp = max_hp
        fox_hp = fox_hp_max

    while exp  > max_exp:
        print("1  + урон")
        print("2  + здoровье")
        print(("3  + здоровье fox"))
        print(("4 + урон fox"))
        ans = int(input("Выбор:"))
        exp -= max_exp
        max_exp *= 1.5
        max_exp = int(max_exp)

        if ans == 4:
            fox_attack += 5
        if ans == 3:
            fox_hp_max += 5
            fox_hp = fox_hp_max
        if ans == 1:
            attack += 10
        elif ans == 2:
            max_hp += 10
            hp = max_hp

if hp <= 0 or fox_hp <= 0:
    print("Задача не выполнена")
''
import random

who = ["Карасик", "Утка","Кряква",
       "Щука", "Судак", "сом", "Пескарь",
       "Скала Джонсон", "Анти-маг",
       "Лобанов", "Маслеников", "Стрелок",
       "ДИО", "Якубович", "Райан Гослинг",
       "Довакин", "Бобр", "математичка",
       "сидорович", "Путин",
       "Рыбак", "Маг", "Евгений",
       "Историк", "Рассказчик", "Шлепа"]
who2 = ["с котом", "с зайцем", "с лисой",
        "С Человеком", "С Собакой",
        "С Червяком", "С Крючком"]
where = ["в лесу", "в подъезде", "в школе", "в баре",
         "в горах", "В колодце", "в реке",
         "В Пруду", "На лавочке", "в гараже",
         "На набережной"]
action = ["пили воду", "Выучили эльфийский язык",
          "Совершили Великую Октябрьскую революцию",
          "вложились в биткойн",
          "Пели", "Играли", "Рыбачили",
          "Смотрели телевизор", "прочитали Войну и мир",
          "вскипятили чайник", "слушали 'Король и шут'",
          "шли на концерт киша"]

why = ["Чтобы поднять настроение", "Чтобы поумнеть", "Чтобы было чем заняться", "т.к. было скучно","Потому что надо думать головой","Чтобы зароботать", "Чтобы собрать сборку с Rtx 4090 ti и xeon E5-2620v2" ]

for i in range(10):
    story = ""
    story += random.choice(who) + " "
    story += random.choice(who2) + " "
    story += random.choice(where) + " "
    story += random.choice(action) + " "
    story += random.choice(why) + " "
    story = story.capitalize()
    print(story)
    print()
''
import random
bot = random.randint(1,3 )
print("сыграть")
print("1 - камень")
print("2 - ножницы")
print("3 - бумага")
ans = int(input("Что показать:"))
if ans == 1:
    if bot == 1:
        print("противник показал камень, ничья")
    if bot == 2:
        print("противник показал ножницы, победа")
    if bot ==3:
        print("противник показал бумагу, поражение")
if ans == 2:
    if bot == 1:
        print("противник показал камень, поражение")
    if bot == 2:
        print("противник показал ножницы, ничья")
    if bot == 3:
        print("противник показал бумагу, победа")
if ans == 3:
    if bot == 1:
        print("противник показал камень, победа")
    if bot == 2:
        print("противник показал ножницы, поражение")
    if bot == 3:
        print("противник показал бумагу, ничья")
''

def print_board(board):
    print("   |   |   ")
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} ")
    print("   |   |   ")

board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

win = False
# X O
#X 1 3 5 7 9
#O  2 4 6 8
hod = 0
hod_x = True
#for line in board:
#    print(line)
print_board(board)

while not win and hod < 9:
    x = int(input())
    y = int(input())
    if board[x][y] == " ":
        if hod_x:
            board[x][y] = "X"
            hod_x = False
        else:
            board[x][y] = "O"
            hod_x = True
        hod += 1

    print_board(board)
    #for line in board:
    #    print(line)

    if board[0][0] == board[0][1] == board[0][2] and board[0][0] != " ":
        win = True
    if board[1][0] == board[1][1] == board[1][2] and board[1][0] != " ":
        win = True
    if board[2][0] == board[2][1] == board[2][2] and board[2][0] != " ":
        win = True

    if board[0][0] == board[1][0] == board[2][0] and board[0][0] != " ":
        win = True
    if board[0][1] == board[1][1] == board[2][1] and board[0][1] != " ":
        win = True
    if board[0][2] == board[1][2] == board[2][2] and board[0][2] != " ":
        win = True

    if board[2][0] == board[1][1] == board[0][2] and board[2][0] != " ":
        win = True
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        win = True

if win:
    if hod_x:
        print("Победили нолики")
'''
d = dict()
for i in range(3):
    key = input("введите ключ")
    val = input("введите значение")
    val2 = int(input("введите здоровье"))
    d[key] = val, val2
print(d)
'''''
import random

weapon = {'копьё': 8,
          'меч': 5,
          'лук': 3,
          'Красный банан ': 4,
          'Костяная нога': 26,
          'Пластиковый нож': 2,
          'Палка ярости': 16,
          'Святая вода': 36,
          'Чёрствый хлеб': 50}

# dmg, hp, exp
armour = {"Футболка с котиком": [12, 10, 10],
         'Ягуаровые трусы': [40, 60, 100],
         "Тяги бархатные": [33, 33, 33],
         "Спортивки адидас": [50, 10, 15],
         "Тёмные очки": [13, 40, 70]}

# dmg, hp
enemy = {'zombie': [15, 50],
         'skeleton': [20, 40],
         'ghost': [10, 70],
         "ящер окаяный": [15, 50],
         "ящер разведчик": [30, 30],
         "ящер мощный": [10, 70],
         "mad strowberry": [5, 15],
         "slime": [8, 35],
         "Друг с вилкой": [20, 55]}

# +dmg +hp
mods = {"горящий": [30, -30],
       'in fire': [30, -30],
       'slow': [-10, 0],
       'with weapon': [20, -10],
       "увеличенный": [25, 70],
       "токсичный": [30, -40],
       "полуразумный": [35, 50],
       "в святой воде": [30, -30],
       "слабый": [10, 10],
       "ордa": [40, 60],
        "очень опасный":[100, -30]}
names = list(enemy.keys())
print(names)
en_name = random.choice(names)
en_dmg, en_hp =enemy[en_name]

print(mods)
mod = mods.keys()
mod = random.choice(list(mod))
en_dmg += mods[mod][0]
en_hp += mods[mod][1]
en_name = mod + " " + en_name
print(en_name)

''
class Points:
    def __init__(self):
        self.a = 0
        self.b = 0
    def add_points_a(self, points=1):
        self.a += points
    def add_points_b(self, points=1):
        self.b += points
    def score(self):
        print(f"Home: {self.a} Guest: {self.b}")
    def winner(self):
        if self.a ==self.b:
            print("Ничья")
        elif self.a > self.b:
            print("Победили Home")
        elif self.a < self.b:
            print("Победили Guest")

    def new_game(self):
        self.a = 0
        self.b = 0
Points = Points()
Points.add_points_a(2)
Points.add_points_a(3)
Points.add_points_a(2)
Points.score()
Points.winner()

Points.new_game()
Points.score()
''
import random
UPGRADE_PRICE = 100
class Base_npc:
    def __init__(self, name = "", hp = 1, at = 1,):
        self.name = name
        self.hp = hp
        self.at = at

    def Upgrade(self, hp, at):
        self.hp += hp
        self.at += at

    def Upgrade_rdm(self, n):
        while n:
            if random.randint(0,1):
                self.hp += 1
            else:
                self.at == 1
            n -= 1

    def take_dmg(self, dmg):
        self.hp -= dmg
    def get_name(self):
        return self.name

class Army:
    def __init__(self, sup = 110):
        self.army = []
        self.player = Base_npc("player")
        self.player.Upgrade_rdm(10)
        self.sup = sup

    def take_dmg(self, dmg):
        if self.army:
            npc = random.choice(self.army)
            npc.take_dmg(dmg)
            if npc.get_hp() <= 0:
                self.army.remove(npc)
        else:
            self.player.take_dmg(dmg)
            if self.player.get.hp() <=0:
                print("End...")
    def upgrade(self, choice, name, choice_at=False, choice_hp=False):
        if self.sup > UPGRADE_PRICE:
            for npc in self.army:
                if npc.get_name == name:
                    if choice_at:
                        npc.upgrade(0, 1)
                    if choice_hp:
                        npc.upgrade(1, 0)

    def get_attack(self):
        dmg = 0
        for npc in self.army:
            dmg += npc.get_at()
        dmg += self.player.get.at()
        return dmg

    def hire(self, npc, value):
        if value <= self.sup:
            self.army.append(npc)
            self.sup -= value
            print(npc.get_name, "Done!")
        else:
            print("Need more money")

def menu(punct):
    for i, line in enumerate(punct, 1):
        print(f"{i}={line}")
    ans = int(input())
    return ans
menu(["Start",  "Settings", "Titles", "About", "Quite"])
'''