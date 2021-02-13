midiccionario = {"Japon":"Tokio", "Spain":"Madrid", "Venezuela":"Caracas", "Alemania":"Berlin"}
midiccionario["Italia"]="Lisboa"

print (midiccionario["Spain"])

print (midiccionario)

midiccionario["Italia"]="Roma"
print (midiccionario)

del midiccionario["Italia"]
print (midiccionario)

del midiccionario["Spain"]

print (midiccionario)