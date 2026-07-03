sales = [1200, 850, 430, 2100, 1750]

print(sales)

def calculate_total(sales):
    total = 0
    for i in sales:
        total += i

    return total
    
res = calculate_total(sales)
print(res)


    

