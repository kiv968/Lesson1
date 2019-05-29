"""
price=100
discount=5
price_with_discount=price - price*discount/100
print(price_with_discount)
"""
"""
# объявляем переменную
def discounted(price,discount):
    price_with_discounted=price-(price*discount/100)
    print(price_with_discounted)
discounted(100,5)
discounted(200,101)   # результат не должен быть отрицат. числом, поэтому нужны условия
"""
def discounted (price,discount,max_discount=50):
    price=abs(float(price))
    discount=abs(float(discount))
    max_discount=abs(float(max_discount))
    if max_discount>99:
        raise ValueError ('скидка не может быть больше 99%')
    if discount>=100:
        price_with_discount=price
    else:
        price_with_discount=price-(price*discount/100)
    #print(price_with_discount)
    return price_with_discount
price2=100
#discount2=8
#discounted(price2,discount2)
discounted(100,5,max_discount=101)
product={'name':'Niva',                   # это словарь {}
        'stock':4,
        'price':120000,
        'discount':50
        }
product['with_discount']=discounted(product['price'],product['discount'])
print(product)
