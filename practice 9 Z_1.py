from time import sleep
from itertools import cycle


class TrafficLight:
    __color = ["   ", [7, 2, 4], ["\033[41m\033[1m", "\033[43m\033[1m", "\033[42m\033[1m"]]

    def run(self):
        color_list = ["", ""]
        for i in cycle((0, 1, 2)):
            color_list[1] = self.__color[2][i]
            print(f"\r({color_list[int(i == 0)]}{self.__color[0]}\033[0m)" "\n"
                  f"({color_list[int(i == 1)]}{self.__color[0]}\033[0m)" "\n"
                  f"({color_list[int(i == 2)]}{self.__color[0]}\033[0m)", end="")
            sleep(self.__color[1][i])
# как можно сделать вертикальный цикл без пустых строк?
traf_light = TrafficLight()
traf_light.run()
