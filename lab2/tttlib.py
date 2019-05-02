import random

def genBoard():
   return [0,0,0,0,0,0,0,0,0]

def printBoard(T):
   if len(T) != 9:
      return False
   for i in T:
      if (i != 0) and (i != 1) and (i != 2):
         return False

   msg=[]
   pos=0
   for i in T:
      if (i==1):
         msg += ["X"]
      elif (i==2):
         msg += ["O"]
      else:
         msg += list(str(pos))
      pos+=1
     
   s = " " + msg[0] + " | " + msg[1] + " | " + msg[2]
   print(s)
   print("---|---|---")
   s = " " + msg[3] + " | " + msg[4] + " | " + msg[5]
   print(s)
   print("---|---|---")
   s = " " + msg[6] + " | " + msg[7] + " | " + msg[8]
   print(s)
   return True


def analyzeBoard(t):
    if t[0] == t[1] == t[2] != 0:
        return t[0]
    if t[3] == t[4] == t[5] != 0:
        return t[3]
    if t[6] == t[7] == t[8] != 0:
        return t[6]
    if t[0] == t[3] == t[6] != 0:
        return t[0]
    if t[1] == t[4] == t[7] != 0:
        return t[1]
    if t[2] == t[5] == t[8] != 0:
        return t[2]
    if t[0] == t[4] == t[8] != 0:
        return t[0]
    if t[2] == t[4] == t[6] != 0:
        return t[2]

    n_opens=0
    for i in t:
       if i==0:
          n_opens+=1
    if n_opens == 0:
        return 3
    else:
        return 0

####################################
def genNonLoser(T, player):
  TTTcopy = list(T)

  count = 0
  while True:
    if TTTcopy[count] == 0:
      TTTcopy[count] = 1
      if analyzeBoard(TTTcopy) == 1:
        return count
        break
      else:
        TTTcopy[count] = 0
    if count == 8:
      break
    count+=1
  return -1


def genWinningMove(T, player):
  TTTcopy = list(T)

  count = 0
  while True:
    if TTTcopy[count] == 0:
      TTTcopy[count] = 2
      if analyzeBoard(TTTcopy) == 2:
        return count
        break
      else:
        TTTcopy[count] = 0
    if count == 8:
      break
    count+=1
  return -1


def genRandomMove(T, player):
  TTTcopy = T

  while True:
    r = random.randint(0,8)

    if TTTcopy[r] == 0:
      return r
      break
  return -1

def genOpenMove(T, player):
  TTTcopy = T

  count = 0
  for x in TTTcopy:
    if x == 0:
      return count
      break
    count+=1
  return -1

