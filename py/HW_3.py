# 1 задание
int_item = 10

# 2 задание
comp_item = 18

# 3 задание
mult_int = int_item * 2

# 4 задание
item_2 = True

# 5 задание
item_3 = False

# 6 задание
item_4 = 0

# 7 задание
item_5 = 1

# 8 задание
usd_item = 'usd'

# 9 задание
usd_usd_rate = 1

# 10 задание
eur_item = 'eur'

# 11 задание
usd_eur_rate = 0.86

# 12 задание
uah_item = 'uah'

# 13 задание
usd_uah_rate = 26.23

# 14 задание
chf_item = 'chf'

# 15 задание
usd_chf_rate = 0.91

# 16 задание
rub_item = 'rub'

# 17 задание
usd_rub_rate = 71.88

# 18 задание
byn_item = 'byn'

# 19 задание
usd_byn_rate = 2.46


# 20 задание
if mult_int > comp_item:
    print('Переменная mult_int больше', comp_item)

# 21 задание
div_int = int_item/2

# 22 задание
if div_int < comp_item:
    print('Переменная div_int меньше', comp_item)

# 23 задание
item_1 = 10 + int_item

# 24 задание
if item_1 < comp_item:
    print('Переменная item_1 меньше', comp_item)
else:
    print('Переменная item_1 больше или равна', comp_item)

# 25 задание
if item_2:
    print('Переменная item_2 = ', item_2)
else:
    print('Переменная item_2 = ', item_3)

# 26 задание
if item_3:
    print('Переменная item_3 = ', item_2)
else:
    print('Переменная item_3 = ', item_3)

# 27 задание
if item_5:
    print('Переменная item_5 = ', item_5)
else:
    print('Переменная item_5 = ', item_4)

# 28 задание
if item_4:
    print('Переменная item_4 = ', item_5)
else:
    print('Переменная item_4 = ', item_4)

# 29 задание
currency_convertor = item_2

# 30 задание
if currency_convertor:
    currency_usd = usd_item
    target_currency = eur_item
    target_currency_amount = 50
    currency_result = 0
    if target_currency == 'eur':
        currency_result = target_currency_amount/usd_eur_rate

        print(target_currency_amount, eur_item, '=', currency_result, usd_item)
    elif target_currency == 'uah':
        currency_result = target_currency_amount / usd_uah_rate
        print(target_currency_amount, uah_item, '=', currency_result, usd_item)
    elif target_currency == 'usd':
        currency_result = target_currency_amount / usd_usd_rate
        print(target_currency_amount, usd_item, '=', currency_result, usd_item)
    elif target_currency == 'byn':
        currency_result = target_currency_amount / usd_byn_rate
        print(target_currency_amount, byn_item, '=', currency_result, usd_item)
    elif target_currency == 'rub':
        currency_result = target_currency_amount / usd_rub_rate
        print(target_currency_amount, rub_item, '=', currency_result, usd_item)
    elif target_currency == 'chf':
        currency_result = target_currency_amount / usd_chf_rate
        print(target_currency_amount, chf_item, '=', currency_result, usd_item)
    else:
        print('Unknown currency')
else:
    print('Переменная currency_convertor = ', item_3)


