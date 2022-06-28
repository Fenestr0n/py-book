# Напишите программу перевода введенного веса в граммы, килограммы, тонны.
# Приставки, которые будет использовать программа: g – граммы, kg – килограммы, t – тонны.
weight = input("Введите вес (g, kg, t) >>> ")

if "t" in weight:
    ton = int(weight.replace("t", ""))
    print(f"{ton * 1e6} g")
    print(f"{ton * 1000} kg")
elif "kg" in weight:
    kilogram = int(weight.replace("kg", ""))
    print(f"{kilogram * 1000} g")
    print(f"{kilogram / 1000} t")
elif "g" in weight:
    gram = int(weight.replace("g", ""))
    print(f"{gram / 1000} kg")
    print(f"{gram / 1e6} t")
else:
    print("Вес не указан")
