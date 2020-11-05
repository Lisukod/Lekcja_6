from sys import argv

saldo = 0
check = True
logs = []
storehouse = {}

def saldo_fun(temp_saldo, comment):
    global saldo
    saldo += temp_saldo
    logs.append(("saldo", temp_saldo, comment))

def buy_fun(product_id, unit_price, product_amount):
    global saldo, check
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
    logs.append(("zakup", product_id, unit_price, product_amount))
    if product_id in storehouse:
        storehouse[product_id] += product_amount
    else:
        storehouse[product_id] = product_amount
    saldo -= unit_price*product_amount

def sale_fun(product_id, unit_price, product_amount):
    global saldo, check
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
    logs.append(("sprzedaz", product_id, unit_price, product_amount))
    if product_id in storehouse:
        storehouse[product_id] -= product_amount
    else:
        print("Błąd. Brak produktu {} na magazynie".format(product_id))
        check = False
        return 
    saldo += unit_price*product_amount

def printOut(logs):
    for log in logs:
        if log == "stop":
            print("{}".format(log))
        else:
            for log_element in log:
                print("{}".format(log_element))

switchCase = {
    "sprzedaz": sale_fun,
    "zakup": buy_fun
}

while check:
    action = input().strip()
    if action == "saldo":
        x = int(input())
        y = input()
        saldo_fun(x, y)
    elif action == "zakup" or action == "sprzedaz":
        x = input()
        y = int(input()) 
        z = int(input())
        switchCase[action](x, y, z)
    elif action == "stop":
        if len(argv) == 1:
            printOut(logs)
        elif argv[1] == "saldo":
            saldo_fun(int(argv[2]), argv[3])
            print(saldo)
            break
        elif argv[1] == "zakup":
            buy_fun(argv[2], int(argv[3]), int(argv[4]))
            printOut(logs)
        elif argv[1] == "sprzedaz":
            sale_fun(argv[2], int(argv[3]), int(argv[4]))
            printOut(logs)
        elif argv[1] == "konto":
            print(saldo)
            break
        elif argv[1] == "magazyn":
            for name in argv[2:]:
                if name in storehouse:
                    print("{}: {}".format(name, storehouse[name]))
                else:
                    print("{}: 0".format(name))
        elif argv[1] == "przeglad":
            for index, log in enumerate(logs):
                if index >= int(argv[2]) and index <= int(argv[3]):
                    if log == "stop":
                        print("{}".format(log))
                        break
                    else:
                        for log_element in log:
                            print("{}".format(log_element))
        else:
            printOut(logs)
        logs.append("stop")
        print(logs[-1])
        break
    else:
        print("Błędna nazwa operacji. Podano {}".format(action))
        break
