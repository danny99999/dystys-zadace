def uspoređivanje(lista1,lista2):
  print("Prvi parametar: ", type(lista1))
  
  print("Drugi parametar: ", type(lista2))

  lista3 = [x if x == y else -1 for x,y in zip(lista1, lista2)]
  print(lista3)

uspoređivanje([1,2,3,4,5],[2,2,4,4,5,])
    