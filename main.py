import datetime
import json

print("-------------------------")
x = datetime.datetime.now()
print(x)
print("-------------------------")


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict1 =	{
  "brand": "Chevrolet",
  "model": "Astra",
  "year": 1964
}

thisdict2 =	{
  "brand": "Chevrolet",
  "model": "corsa",
  "year": 1964
}

thisdict3 =	{
  "brand": "Chevrolet",
  "model": "Astra",
  "year": 1964
}

vector = [thisdict,thisdict1,thisdict2,thisdict3]

contchevy=0
contFord=0

for recorrer in vector:
  recorrer.get("brand")
  if(recorrer["brand"]=="Chevrolet"):
     contchevy=contchevy+1
  else:
     contFord+=contFord+1

print ("chevis:"+str(contchevy)+" ford:"+str(contFord))

print(thisdict3.values())
print("----------------------------------------")
print("-leer con with")

with open('jeison1.json') as file:
  data = json.load(file)
  #leer a nivel 'members'
  cont=0
  age=0
  menosde30=0
  masde30=0
  for x in data['members']:
      cont=cont+1
      age=x.get("age")
      if age < 30:
        menosde30=menosde30+1
      else:
        masde30=masde30+1

      if age == thisdict3.get('year'):
        print("-----------------------------------------------")
        print("age(",age,") es igual al year del vector (",thisdict3.get('year'),")")
        print("-----------------------------------------------")

      print("(",cont,")")
      print('name:', x['name'])
      print('age:', x['age'])
      print('')
      print("menos de 30:",menosde30," mas de 30:",masde30)

      total=masde30+menosde30

      print("-------------------------------------")
      print("lambda para saber que porcentaje tiene menos de 30:")

      lambdaresult = lambda a : a * 100 / total
      print(lambdaresult(menosde30))