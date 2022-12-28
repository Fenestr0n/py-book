# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
for x in [True,False]:
    for y in [True,False]:
        for z in [True,False]:
            if not (x or y or z) == (not x and not y and not z):
                print(f"¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z}")

'''
¬(True ⋁ True ⋁ True) = ¬True ⋀ ¬True ⋀ ¬True
¬(True ⋁ True ⋁ False) = ¬True ⋀ ¬True ⋀ ¬False
¬(True ⋁ False ⋁ True) = ¬True ⋀ ¬False ⋀ ¬True
¬(True ⋁ False ⋁ False) = ¬True ⋀ ¬False ⋀ ¬False
¬(False ⋁ True ⋁ True) = ¬False ⋀ ¬True ⋀ ¬True
¬(False ⋁ True ⋁ False) = ¬False ⋀ ¬True ⋀ ¬False
¬(False ⋁ False ⋁ True) = ¬False ⋀ ¬False ⋀ ¬True
¬(False ⋁ False ⋁ False) = ¬False ⋀ ¬False ⋀ ¬False
'''              