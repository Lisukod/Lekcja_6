import sys

saldo = 0
logs = []

def saldo_fun():
    global saldo
    saldo += int(input())
    comment = input()
    print("{}: {}".format(comment, saldo))

def buy_fun():
    global saldo
    product_id = input()
    unit_price = int(input())
    product_amount = int(input())
    if saldo - unit_price*product_amount < 0:
        print("Błąd. Ujemne saldo po zakupie {} w ilości {}".format(product_id, product_amount))
        return False
    elif product_amount < 0:
        print("Błąd. Ujemna ilość zakupionego towaru {} w ilości {}".format(product_id, product_amount))
        return False
    elif unit_price*product_amount < 0:
        print("Błąd. Ujemna kwota zakupu {} w ilości {}".format(product_id, product_amount))
        return False
    saldo -= unit_price*product_amount

def sale_fun():
    global saldo
    product_id = input()
    unit_price = int(input())
    product_amount = int(input())
    if product_amount < 0:
        print("Błąd. Ujemna ilość zakupionego towaru {} w ilości {}".format(product_id, product_amount))
        return False
    elif unit_price*product_amount < 0:
        print("Błąd. Ujemna kwota zakupu {} w ilości {}".format(product_id, product_amount))
        return False
    saldo += unit_price*product_amount

switchCase = {
    "saldo": saldo_fun(),
    "sprzedaż": sale_fun(),
    "zakup": buy_fun(),
    "konto": "4",
    "magazyn": "5",
    "przegląd": "6"
}

print("Wybierz jedną z poniższych akcji.\nsaldo | zakup | sprzedaż")
while True:
    action = input()
    if action == "saldo" or "zakup" or "sprzedaż":
            check = switchCase[action]
            if not check:
                break
    elif action == "stop":
        break
    else:
        print("Błędna nazwa operacji")