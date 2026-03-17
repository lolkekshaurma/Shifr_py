
cart = {'ноутбук': 3000.90, 'телефон': 150000.99, 'наушники': 400.55}
allowed_coupons =["SALE20", "NEWYEAR", "VIP"]

product_name = input("Название товара ")
price = cart.get(product_name, "default")
quantity = int(input("Кол-во товаров "))
ismember = int(input("Клубный клиент 1 2"))
coupon_code = str(input("Промокод "))

print(product_name, price) #проверка

is_member = False #мембер или нет
if (ismember == 1):
    is_member = True
    

#есть купон или нет
is_coupon = False
if ((coupon_code in allowed_coupons)== True):
    is_coupon = True

base_sum = price * quantity #сумма
if (is_coupon == True and price >= 10000):
    sum_sale = base_sum - ((base_sum * 20)/100)
elif(is_member == True):
    sum_sale = base_sum - ((base_sum * 5)/100)
else:
    sum_sale = base_sum

sale = round(base_sum-sum_sale,2)

sum_sh =  round(sum_sale + ((sum_sale * 13)/100),2) #налог
nalog = sum_sh-round(sum_sale,2)

#бонусные баллы
bonus = int(sum_sh//100)
bonus_quantity = quantity**2
bonus += bonus_quantity


#проверка на акцию
is_sale = ""
if (product_name.find("а") == True or product_name.find("А") == True):
    is_sale = "(АКЦИЯ)"

print(f"=== ЧЕК МАГАЗИНА === \nТовар: {product_name} {is_sale}\nЦена за шт: {price} \nКоличество: {quantity} \n-------------------") 
print(f"Сумма до скидки: {base_sum} \nСкидка: {round(sale,2)}\nСумма после скидки: {round(sum_sale,2)}\nНалог (13%): {round(nalog,2)}")
print(f"Начислено баллов: {bonus} (вкл. бонус за объем: {bonus_quantity}) \nТип данных суммы: {type(sum_sh)} ")