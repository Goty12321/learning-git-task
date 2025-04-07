lista_zakupów = {
    "piekarnia": ['chleb','pączek','bułki'],
    "warzywniak": ['marchew','seler','rukola']
}

for key in lista_zakupów:
    values = lista_zakupów[key]
    updated_values = []
    for value in values:
        updated_values.append(value.capitalize())
    print(f"Idę do {key.capitalize()} i kupuję tam {updated_values}.")