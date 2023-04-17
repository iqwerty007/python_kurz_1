sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

kod = input("Uveďte kód součástky: \n")
mnozstvi = int(input("Jaké množství požadujete?: \n"))

if kod not in sklad :
    print("Součástka není skladem.")
elif sklad[kod] < mnozstvi:
    print("Lze prodat jen omezený počet kusů.")
    del sklad[kod]
else:
    print("Poptávku lze uspokojit v plné výši.")        
