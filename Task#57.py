# Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = "qwerty фыва олдж абв эждло авыфабв абв asdf awsd абв".split()

abc = list(filter(lambda x: "абв" in x, text))
_ = [text.remove(item) for item in abc]

print(text) # ['qwerty', 'фыва', 'олдж', 'эждло', 'asdf', 'awsd']