lista_zakupów = {
    "piekarnia": ['chleb','pączek','bułki','gniazdko'],
    "warzywniak": ['marchew','seler','rukola']
}
ilość_produktów = 0
for key in lista_zakupów:
    values = lista_zakupów[key]
    ilość_produktów = ilość_produktów + len(values)
    updated_values = []
    for value in values:
        updated_values.append(value.capitalize())
    print(f"Idę do {key.capitalize()} i kupuję tam {updated_values}.")
print(f"W sumie kupuję {ilość_produktów} produktów.")