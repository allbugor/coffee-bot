from data import MENU
from logic import get_total_price


def print_menu():
    print("\n☕ --- МЕНЮ КОФЕЙНИ --- ☕")
    for drink in MENU:
        print(f"{drink:<12} ...... {MENU[drink]}")

def take_order():
    list_order = []
    print_menu()
    while True:
        order = input("Введите ваш выбор или stop для окончания заказа:\n>> ").lower().strip()
        if order == "stop":
            break
        if order in MENU:
            list_order.append(order)
            print(f"{order.capitalize()} добавлен в заказ.")
        else:
            print(f"{order} нет в меню, попробуйте еще раз!")

    total_price = get_total_price(list_order)
    print(f"Вы заказали: {', '.join(list_order)} к оплате: {total_price} рублей.")

if __name__ == "__main__":
    take_order()






    
        