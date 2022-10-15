
#print(type(osoba2))

def spajanje(parametar1, parametar2):
   
   print('Parametar1 je: ', type(parametar1))
   print('Parametar2 je: ', type(parametar2))
   
   if type(parametar1) == type(parametar2):
       print('Parametri su istog tipa')
       if type(parametar1 and parametar2) is list:
           print('2 parametra su liste')
           list3= list1 + list2
           print(list3)
       elif type(parametar1 and parametar2) is dict:
           print('2 parametra su dictionary')
           newdict= parametar1.copy()
           newdict.update(parametar2)
           print(newdict)
           
   else:
        print('Parametri nisu isti')
        
          
spajanje({1:2, 3:2},{5:2, 4:1})




           
           
   

        
          