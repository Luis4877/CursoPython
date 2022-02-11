# #Listas en Python
# nombres = ['Luis','Paula','Carla','Maria']
# #acceder individual
#
#
#
# nombres[3] = 'Patachin'
#
# print(nombres)
#
# for nombre in nombres:
#     print(nombre)
# #entrar en cada elemento individual
#
# else:print('FIn de la lista')
#
# #saber el largo de una lista
#
# elementos = len(nombres)
# print(elementos)
#
# #agregar nuevo elemento
#
# nombres.append('Oyuki')
# print(nombres)
#
# nombres.insert(4,'Carolina')
# print(nombres)
#
# #Elimina el valor de un elemento por similitud
# nombres.remove('Oyuki')
# print(nombres)
#
# #Elimina el ultimo valor de la lista o en el indice que le indiques
# nombres.pop()
# print(nombres)
#
# #eliminar por indice
#
# del nombres[0]
# print(nombres)
#
# #Eliminar elementos de la lista
# nombres.clear()
#
# print(nombres)
#
#
# del nombres #elimina la lista de la memoria definitivamente
#

#Tarea



# frutas = ('naranja','platano','Melon')
#
# #
# # print(len(frutas))
# #
# # print(frutas[0:1])
#
#
#
# #Convertir tuplas a listas e invertir
#
# frutaLista = list(frutas)
#
# frutaLista[0]='Peluza'
#
# frutas = tuple(frutaLista)
#
# print(frutas)







#Tarea

#
#
# #set
#
# planetas = {'Mercurio','Urano','Luna','Marte'}
#
# print(planetas)
#
# #revisar si hay un elemento
#
#
# print('Marte' in planetas)
#
# presente = ('Marte' in planetas)
#
# print(presente)
#
#
# #agregar elementos al set
#
# planetas.add('Tierra')
# print(planetas)
#
#
# #remover un elemento
#
# planetas.remove('Marte')#elimina y manda error sino existe
# planetas.discard('Marte')#elimina sin mandar error por si no existe
# print(planetas)
#
# planetas.clear()#Elimina los elementos del set
#
# del planetas #Elimina definitivamente la variable



diccionario = {
    'IDE':'Integreted Development Enviromente',
    'POO':'Programming oriented objects',
    'DBMS':'Database Management System'

}


diccionario['PK'] = 'Prymary Key'

print(diccionario)

#remover un elemento del diccionario
diccionario.pop('PK')
print(diccionario)


#
# #recuperar los terminos y las llaves
# for termino,valor in diccionario.items():
#
#     print(termino,valor)
# #recuperar solo las llaves
# for termino in diccionario.keys():
#     print(termino)

#recuperar los valores del diccionario
#
# for valor in diccionario.values():
#     print(valor)
#
#
#
#     #saber si existe un elemento
#
#     print('IDE' in diccionario)

#agregar un nuevo elemento al diccionario





# print(diccionario)
#
# print(len(diccionario))
#
# #acceder a un elemento desde su key
#
# print(diccionario['IDE'])
#
#
# #Modificar un elemento
#
# diccionario['IDE'] = 'Sepa la verga que dice xd'
#
# print(diccionario)