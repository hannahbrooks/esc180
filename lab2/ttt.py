from tttlib import *

T = genBoard()
while True:
   printBoard(T)
   moveX = input("X move?")
   L = [0, 1, 2, 3, 4, 5, 6, 7, 8]
   for x in L:
    if moveX == str(x):
      if T[int(moveX)] == 0:
        T[int(moveX)] = 1

   state = analyzeBoard(T)
   if state == 1:
    print("Win for X! Final board:")
    printBoard(T)
    break
   elif state == 3:
     print("Cat's game!")
     break
   elif state == -1:
     print("ERROR!")
     break


   if genWinningMove(T, 2) != -1:
    T[genWinningMove(T, 2)] = 2
   elif genNonLoser(T, 2) != -1:
    T[genNonLoser(T, 2)] = 2
   elif (genRandomMove(T, 2) != -1) and (genOpenMove(T, 2) != -1):
    choice = random.randint(0,1)
    if choice == 0:
      T[genRandomMove(T, 2)] = 2
    else:
      T[genOpenMove(T, 2)] = 2
   else:
    print("ERROR")
    break


   state = analyzeBoard(T)
   if state == 2:
    print("Win for O! Final board:")
    printBoard(T)
    break
   elif state == 3:
     print("Cat's game!")
     break
   elif state == -1:
     print("ERROR!")
     break
