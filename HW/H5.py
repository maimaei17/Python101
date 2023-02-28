price = int(input('price: '))
def disc(price):
    if price <= 500:
        dis = price*0.1
    elif price <= 800:
        dis = price*0.15
    elif price <= 1200:
        dis = price*0.2
    else:
        dis = price*0.4

    print('Discount: ',dis)
    print('Total: ',price-dis)

disc(price)
