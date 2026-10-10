from ursina import *
import random

app = Ursina()

# Игрок
player = FirstPersonController()
player.speed = 3
player.cursor.visible = False

# Окружение
ground = Entity(model='plane', scale=50, texture='white_cube', texture_scale=(50,50), color=color.dark_gray)

# Стены лабиринта
walls = []
for i in range(-20, 21, 5):
    walls.append(Entity(model='cube', color=color.black, scale=(2,5,0.5), position=(i,2,10)))
    walls.append(Entity(model='cube', color=color.black, scale=(2,5,0.5), position=(10,2,i)))

# Фонарик
flashlight = Entity(model='cube', color=color.yellow, scale=(0.1,0.1,0.5), parent=player, position=(0.5,-0.5,1))
light = PointLight(parent=flashlight, color=color.white)

# Монстр
monster = Entity(model='cube', color=color.red, scale=(1,2,1), position=(random.randint(-10,10),1,random.randint(-10,10)))

# События
def update():
    # Монстр двигается к игроку
    if distance(monster, player) < 12:
        monster.position += (player.position - monster.position).normalized() * time.dt * 1.5

    # Если монстр близко — конец игры
    if distance(monster, player) < 1.5:
        print("👻 Game Over! Монстр поймал тебя.")
        application.quit()

    # Фонарик мигает
    if random.random() < 0.01:
        light.enabled = not light.enabled

app.run()

