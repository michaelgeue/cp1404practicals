def main():
    total_cost = 0
    item_quantity = int(input("Number of items: "))

    while item_quantity < 0:
        print("Invalid number of items!")
        item_quantity = int(input("Number of items: "))

    for each_item in range(0, item_quantity):
        item_price = float(input("Price of item: "))
        total_cost += item_price

    if total_cost > 100:
        discount = total_cost * .1
        total_cost -= discount

    if item_quantity == 1:
        item_quantity = "1 item"
    else:
        item_quantity = str(item_quantity) + " items"

    total_cost = format(total_cost, '.2f')
    print("Total price for " + item_quantity + " is $" + total_cost)


main()
