import random

list_of_card= [2, 3, 4 ,5 ,6, 7, 8, 9 ,10, 'J', 'K', 'Q', 'A']
broadways = [10, 'J', 'Q', 'K']
classifiction = ''
pay_out_value = {'none': -1,'pair': 3,'trips': 30, 'trips broadway': 100, 'trips Aces': 200}

symbol1 = random.choice(list_of_card)
symbol2 = random.choice(list_of_card)
symbol3 = random.choice(list_of_card)



if symbol1 == symbol2 or symbol1 == symbol3 or symbol2 == symbol3:
    classifiction = 'pair'

total = 100 

for i in range(1000):
    symbol1 = random.choice(list_of_card)
    symbol2 = random.choice(list_of_card)
    symbol3 = random.choice(list_of_card)

    if symbol1 == symbol2 or symbol1 == symbol3 or symbol2 == symbol3:
        classifiction = 'pair'
    else:
        classifiction = 'none'
    
    if symbol1 == symbol2 == symbol3:
        classifiction = 'trips'
    
    if symbol1 == symbol2 == symbol3 == 'A':
        classifiction = 'trips Aces'
    
    total += pay_out_value[classifiction]
    
    if classifiction == 'trips Aces':
        print(symbol1, symbol2, symbol3, 'payout is'  f' {pay_out_value[classifiction]}')
print(total)
print('test')
