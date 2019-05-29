#словари_dictionary
#
"""
product={'name':'Niva',
        'stock':4,
        'price':120000
        }
product['mileage']=1000       
print(product['name'])
print(product.get('skore',0))
"""
# объединение списков и словарей
car=['toyota','Lada','bmw','Niva']        # это список  []
product={'name':'Niva',                   # это словарь {}
        'stock':4,
        'price':120000
        }
product['recomend']=car   
#print(product['recomend'])   #выдает данные из списка car
product['recomend'].append('uaz')
print(product['recomend'][1])