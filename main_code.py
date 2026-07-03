sales = [1200, 850, 430, 2100, 1750]

print(sales)

def calculate_total(sales):
    total = 0
    for i in sales:
        total += i

    return total
    
res = calculate_total(sales)
print(res)


def avarage_value(sales):
    avarage_sale = sum(sales)/len(sales)
    return avarage_sale
avarage = avarage_value(sales)
print(f'Средняя продажа:{avarage}')

def max_sale(sales):
    max1 = max(sales)
    return max1
maximum = max_sale(sales)
print(f'Максимальная продажа:{maximum}')


    

