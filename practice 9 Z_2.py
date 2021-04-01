class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def get_asphalt(self, weight=25, thickness=5):
        return f"{self.__length} * {self.__width} * {weight} * {thickness} =" \
               f"{(self.__length * self.__width * weight * thickness) / 1000}"


road = Road(5000, 20)
print(road.get_asphalt())
