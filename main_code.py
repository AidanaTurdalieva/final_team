sales = [1200, 850, 430, 2100, 1750]

print(sales)

def calculate_total(sales):
    total = 0
    for i in sales:
        total += i

    return total
    
res = calculate_total(sales)
print(res)

def find_min_sale(sales):
    min_sale = 0
    for i in sales:
        if i < min_sale:
            min_sale = i

    return min_sale

min_sale = find_min_sale(sales)
print(min_sale)   