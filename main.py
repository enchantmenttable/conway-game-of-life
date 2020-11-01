from matplotlib.animation import FuncAnimation
from itertools import permutations
import matplotlib.pyplot as plt
import random
import copy
from numpy import array

# TODO: 4: refactor code

surface = []


def initialize(size):
    global surface
    surface = [[0 for _ in range(size)] for _ in range(size)]


def add_live_cells(live_cells):
    global surface
    size = len(surface)

    # patterns = {}

    # while live_cells and not live_cells.isnumeric():
    #     live_cells = input("Please enter a number: ")

    if not live_cells:
        live_cells = random.randint(
            round(size**2/10), round(size**2*0.9))
        print("Randomizing live cells...")
        positions = list(permutations(range(size), 2))
        live_cell_positions = random.sample(positions, live_cells)

    for position in live_cell_positions:
        surface[position[1]][position[0]] = 1


def progress(frame, img):
    global surface

    new_surface = copy.deepcopy(surface)
    for y in range(len(surface)):
        for x in range(len(surface)):
            live_cells_count = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (y-1 > 0 and y+1 < len(surface)) and (x-1 > 0 and x+1 < len(surface)) and not (i == 0 and j == 0):
                        if surface[y+i][x+j] == 1:
                            live_cells_count += 1
            if surface[y][x] == 0 and live_cells_count == 3:
                new_surface[y][x] = 1
            elif surface[y][x] == 1 and (live_cells_count in [2, 3]):
                pass
            else:
                new_surface[y][x] = 0
    img.set_data(new_surface)
    surface = copy.deepcopy(new_surface)
    return img,


def main():
    size = int(input("Set grid size: "))
    initialize(size)
    speed = int(
        input("Set animation speed (time between frames in milliseconds): "))
    live_cells = False
    # speed = int(input("Set animation speed (in millisecond): "))
    # live_cells = input(
    #     "Set live cells in 1 of 3 ways:\n"
    #     "- Input patterns and positions <pattern> <[x,y]> (different patterns separated by semicolon). For example: 'glider' [3,3]; 'block' [5, 7]\n"
    #     "- Enter the number of live cells: \n"
    #     "- Press 'return' and live cells will be randomized."
    # )
    add_live_cells(live_cells)

    fig, ax = plt.subplots()
    img = ax.imshow(surface, interpolation="nearest")
    animation = FuncAnimation(fig, progress, fargs=(
        img, ), frames=20, interval=speed)
    plt.show()


if __name__ == "__main__":
    main()
