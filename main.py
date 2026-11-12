import json
# vemos que los datos estan compuestos de un diccionario de listas que inclueyn diccionarios dentro
# las keys del diccionario grande son los nombres, que incluyen una lista de items comprados, que a su vez el item tiene un diccionario con datos como precio nombre y tipo

with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    print("Apartado 1:")
    totales={} #para apartado2
    quantity={}

    for persona, compras in data.items():
        total = sum(compra["precio"] for compra in compras) #ap1
        print(f"{persona} ha gastado {total:.2f} \u20ac") #ap1
        totales[persona] = total #ap2
        quantity[persona] = len(compras) #ap3

    #Miramos quien ha gastado más, y en qué cantidad
    
    bigspender = max(totales, key=totales.get)
    bigexp = totales[bigspender]
    #print del apartado 2
    print("\nApartado 2:")
    print(
    f"El cliente que más ha gastado es "
    f"{bigspender}, con {bigexp:.2f} \u20ac")

    #miramos quien es el cliente con mas articulos
    #contamos cuantos diccionarios tiene en la lista. supongo que será numero de items de la lista de su nombre

    bigbuyer = max(quantity, key = quantity.get)
    bigbuyerquant = quantity[bigbuyer]
    print("\nApartado 3:")
    print(
    f"{bigbuyer} es quien más productos ha comprado, "
    f"con un total de {bigbuyerquant} artículos.")

    #producto mas caro y mas barato: comparamos los productos de todos los usuarios para ver cuales tienen valores extremos
    

# print(data)

