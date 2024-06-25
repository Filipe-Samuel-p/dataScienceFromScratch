""" Dado 10 valores digitados pelo usuario, diga qual é o maior e o menor valor"""


def bublleSort(listOfElements: list[int]) -> list[int]:
   change = True
   while change:
       change = False
       for index in range(len(listOfElements) - 1):
           if listOfElements[index] > listOfElements[index + 1]:
               aux = listOfElements[index]
               listOfElements[index] = listOfElements[index + 1]
               listOfElements[index + 1] = aux
               change = True
        
       if change != True:
          return listOfElements
          
    
def main ()-> None:
    elements: list[int] = []
    x: int = 0

    while(x < 10):
        number = int(input("---- Digite um numero inteiro ---- "))
        elements.append(number)
        x += 1
    finalList = bublleSort(elements)
    print(f"O menor elemento digitado é {finalList[0]} e o maior elemento é o {finalList[len(elements) - 1]}")

    

main()