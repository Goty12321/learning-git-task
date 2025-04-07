lista_zakupów = {
    "piekarnia": "['chleb','pączek','bułki']",
    "warzywniak": "['marchew','seler','rukola']"
}

for key in lista_zakupów:
    values = lista_zakupów[key]
    print(f"Idę do {key} i kupuję tam {values}.")