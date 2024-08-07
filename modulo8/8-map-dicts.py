items = [
    {
        'product': 'book',
        'price': 10
    },
    {
        'product': 'laptop',
        'price': 1000
    },
    {
        'product': 'smartphone',
        'price': 500
    }
]

prices = list(map(lambda item: item['price'], items))
print(prices, '\n')  # Output: [10, 1000, 500]

def add_taxes(item):
    new_item = item.copy() #al crear una copia del diccionario, evitamos modificar el original
    new_item['taxes'] = new_item['price'] * 0.19
    return item

new_items = list(map(add_taxes, items))
print(new_items)
print('\n Old List\n')
print(items)