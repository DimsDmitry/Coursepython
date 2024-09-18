text = 'Я уеду жить в Лондон, мне Москва будет сниться'
num_o = 0

for sym in text:
    if sym.lower() == 'о':
        num_o += 1

print('Символов о в тексте:', num_o)