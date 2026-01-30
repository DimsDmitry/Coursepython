promo = input('Введите промокод:')
while promo != 'sale' and promo != 'hello':
    promo = input('Этот промокод недействителен. Попробуйте снова:')
print('Промокод принят.')