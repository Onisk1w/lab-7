import math

def count_ways_to_climb_stairs(n):
    golden_ratio = (1 + math.sqrt(5)) / 2
    a = int(((golden_ratio ** n - (-golden_ratio) ** -n) / math.sqrt(5)))
    return a

n = int(input(" Введите количество ступеней ")) + 1
ways_to_climb = count_ways_to_climb_stairs(n)
print("Количество способов ", ways_to_climb)
