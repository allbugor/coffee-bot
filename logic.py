from data import MENU

def get_total_price(order_list):
    total_sum = 0
    for order in order_list:
        price = MENU[order]
        total_sum += price

    return total_sum

