from sys import argv

saldo = 0
logs = []
storehouse = []
check = True

def saldo_fun():
    global saldo
    temp_saldo = int(input())
    saldo += temp_saldo
    comment = input()
    logs.append((comment, saldo))
    # print("{}: {}".format(comment, saldo))

def buy_fun():
    global saldo, check
    product_id = input()
    unit_price = int(input())
    product_amount = int(input())
    if saldo - unit_price*product_amount < 0:
        print("Błąd. Ujemne saldo po zakupie {} w ilości {}".format(
            product_id, product_amount))
        check = False
        return
    elif product_amount < 0:
        print("Błąd. Ujemna ilość zakupionego towaru {} w ilości {}".format(
            product_id, product_amount))
        check = False
        return
    elif unit_price*product_amount < 0:
        print("Błąd. Ujemna kwota zakupu {} w ilości {}".format(
            product_id, product_amount))
        check = False
        return
    logs.append((product_id, unit_price, product_amount))
    if product_id in storehouse:
        storehouse[storehouse.index(product_id)+1] += product_amount
    else:
        storehouse.append(product_id)
        storehouse.append(product_amount)
    saldo -= unit_price*product_amount

def sale_fun():
    global saldo, check
    product_id = input()
    unit_price = int(input())
    product_amount = int(input())
    if product_amount < 0:
        print("Błąd. Ujemna ilość zakupionego towaru {} w ilości {}".format(
            product_id, product_amount))
        check = False
        return
    elif unit_price*product_amount < 0:
        print("Błąd. Ujemna kwota zakupu {} w ilości {}".format(
            product_id, product_amount))
        check = False
        return
    logs.append((product_id, unit_price, product_amount))
    if product_id in storehouse:
        storehouse[storehouse.index(product_id)+1] -= product_amount
    else:
        print("Błąd. Brak takiego {} produktu na magazynie".format(product_id))
        check = False
        return 
    saldo += unit_price*product_amount

switchCase = {
    "saldo": saldo_fun,
    "sprzedaż": sale_fun,
    "zakup": buy_fun,
    # "konto": konto_fun()
}

print("Wybierz jedną z poniższych akcji.\nsaldo | zakup | sprzedaż")
while check:
    action = input()
    if action == "saldo" or  action == "zakup" or action == "sprzedaż":
        switchCase[action]()
    elif action == "stop":
        break
    else:
        print("Błędna nazwa operacji")

if check:
    print(saldo)

for index, log in enumerate(logs):
    print("{}. {}".format(index, log))