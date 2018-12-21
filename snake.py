import threading
import time
import random

width = 70
height = 20

vector_x = 0
vector_y = -1

head_x = width / 2
head_y = height - 2

tail = [[head_x, head_y]]

def get_rand_fruit():
    return [random.randrange(0, width), random.randrange(0, height)]

fruits = [get_rand_fruit()]

def render():

    global head_x, head_y, vector_x, vector_y, tail, fruits
    times = 0

    while (True):
        head_x += vector_x
        head_y += vector_y

        tail.append([head_x, head_y])

        if [head_x, head_y] in fruits:
            fruits.remove([head_x, head_y])
            fruits.append(get_rand_fruit())
        else:
            tail.pop(0)

        scene = ""
        for i in range(width+2):
            scene += "-"
        scene += "\n"

        for y in range(height):
            for x in range(-1, width+1):
                if x == -1 or x == width:
                    scene += "|"
                else:
                    if [x, y] in tail:
                        texture_index = 0
                        while tail[texture_index] != [x, y]:
                            texture_index+=1
                        scene += "u" if texture_index % 2 else "r"
                    elif [x, y] in fruits:
                        scene += "*"
                    else:
                        scene += " "
            scene += "\n"

        for i in range(width+2):
            scene += "-"
        scene += "\n"

        print(scene, head_x, head_y, vector_x, vector_y)

        if vector_y != 0:
            time.sleep(0.2)
        else:
            time.sleep(0.1)
        times += 1

        # if times % 150:
        #     fruits.append(get_rand_fruit())

threading.Thread(target=render).start()

from curtsies import Input

def main():
    global vector_x, vector_y
    with Input(keynames='curses') as input_generator:
        for e in input_generator:
            # print(repr(e))
            pressedKey = repr(e)
            if pressedKey == "\'KEY_UP\'":
                # print('UP');
                vector_x = 0
                vector_y = -1
            if pressedKey == "\'KEY_RIGHT\'":
                # print('RIGHT');
                vector_x = 1
                vector_y = 0
            if pressedKey == "\'KEY_DOWN\'":
                # print('DOWN');
                vector_x = 0
                vector_y = 1
            if pressedKey == "\'KEY_LEFT\'":
                # print('LEFT');
                vector_x = -1
                vector_y = 0

if __name__ == '__main__':
    main()
