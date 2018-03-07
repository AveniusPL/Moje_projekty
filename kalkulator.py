print("Witaj w programie <|::Kalkultor::|>")
def menu():
    print (""" """)
    print ("""..::::::::::::::::::::.. || MENU || ..::::::::::::::::::::..""")
    print (""" """)
    print ("..:: 1 - dodawanie           ::..")
    print ("..:: 2 - odejmowanie         ::..")
    print ("..:: 3 - mnożenie            ::..")
    print ("..:: 4 - dzielenie           ::..")
    print ("..:: 5 - dzielenie całkowite ::..")
    print ("..:: 6 - potęgowanie         ::..")
    print ("..:: 7 - autor               ::..")
    print ("..:: 8 - koniec              ::..")
    print ("..:: 0 - MENU                ::..")
    print (""" """)
    

def dodawanie():
    print("Trzecia liczba jest alternatywna, jeśli jej nie potrzebujesz wpisz 0 ")
    try:
        a = input("Pierwsza liczba ")
        b = input("Druga liczba ")
        c = input("Trzecia liczba ")
        wynik = float(a)+float(b)+ float(c)
        print (wynik)
    except ValueError:
                   print ("Nie podałeś poprawnie liczby ")
    return
 
def odejmowanie():
    print("Trzecia liczba jest alternatywna, jeśli jej nie potrzebujesz wpisz 0 ")
    try:
        a = input("Pierwsza liczba ")
        b = input("Druga liczba ")
        c = input("Trzecia liczba ")
        wynik = float(a)-float(b)- float(c)
        print (wynik)
    except ValueError:
                   print ("Nie podałeś poprawnie liczby ")
    return

def mnozenie():
    print("Trzecia liczba jest alternatywna, jeśli jej nie potrzebujesz wpisz 0 ")
    try:
        a = int(input("Pierwsza liczba "))
        b = int(input("Druga liczba "))
        c = int(input("Trzecia liczba "))
    if c == 0:
        wynik = a * b
        print (wynik)
    else:
        wynik = a * b * c
        print (wynik)

    except ValueError:
        print ("Nie podałeś poprawnie liczby ")
    except ValueError:
        print ("Nie podałeś poprawnie liczby ")
    return

def dzielenie():
    print("Trzecia liczba jest alternatywna, jeśli jej nie potrzebujesz wpisz 0 ")
    try:
        a = input("Pierwsza liczba ")
        b = input("Druga liczba ")
        c = input("Trzecia liczba ")
        wynik = float(a) / float(b)/ float(c)
        print (wynik)
    except ValueError:
        print ("Nie podałeś poprawnie liczby ")
    except ZeroDivisionError:
        wynik = float(a) / float(b)
        print (wynik)
    return

def dzieleniecal():
    a = input("Pierwsza liczba ")
    b = input("Druga liczba ")
    dziel = int(a)/int(b)
    reszta = int(a)%int(b)
    wynik = "wynik",dziel,"reszty",reszta
    print (wynik)
    return
def potegowanie():
    a = input("Liczba ")
    b = input("Potęga ")
    wynik = float(a)**float(b)
    print (wynik)
    return
def autor():
    wynik = "Program stworzył Patryk Janusz"
    print (wynik)
    return

 
menu()
operacja = input("Co wybierzesz ? ")
while operacja != "8":
    if operacja=="1": print (":::wybrałeś dodawanie:::\n"),dodawanie()
    elif operacja=="2": print (":::wybrałeś odejmowanie:::\n"),odejmowanie()
    elif operacja=="3": print (":::wybrałeś mnożenie:::\n"),mnozenie()
    elif operacja=="4": print (":::wybrałeś dzielenie :::\n"),dzielenie()
    elif operacja=="5": print (":::wybrałeś dzielenie calkowite:::\n"),dzieleniecal()
    elif operacja=="6": print (":::wybrałeś potegowanie:::\n"),potegowanie()
    elif operacja=="7": print (":::wybrałeś autor:::\n"),autor()
    elif operacja=="0": menu()
    elif operacja=="8": break
    else: print("Wpisałeś niewłaściwą liczbę")
    operacja = input("Co wybierzesz ? ")
