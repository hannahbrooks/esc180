import sys

FIN=""
newfin = ""
FOUT=""
newfout=""
COLUMN = 0
newcolumn = 0
DIRECTION = ""
newdirection = True
nargs=len(sys.argv)
skip=False
for i in range(1,nargs):
  if not skip:
      arg=sys.argv[i]
      if arg == "--fin":
        if i != nargs-1:
          FIN=sys.argv[i+1]
          skip=True
      elif arg == "--fout":
        if i != nargs-1:
          FOUT=sys.argv[i+1]
          skip=True
      elif arg == "--col":
        COLUMN=sys.argv[i+1]
        newcolumn = int(COLUMN)
        skip=True
      elif arg == "--dir":
        DIRECTION=sys.argv[i+1]
        if DIRECTION == "+":
            newdirection = True
        else:
          newdirection = False
        skip=True
      else:
        print("ERR: unknown arg:",arg)
  else:
    skip=False

newfin = open(FIN,'r')
lines = newfin.readlines()
newfin.close()
accum=[]
for i in lines:
   j=i.split('\n')[0]  # first get rid of the '\n'
   k=j.split(',')      # now split on the comma
   r=[]
   for x in k:
      r = r + [float(x)]
   accum = accum + [r] # accumulateprint(accum)

def genSortKey(col, d):
  def key(x):
    if  d == True:
      return x[col]
    else:
      return -x[col]
  return key

sortKey = genSortKey(newcolumn, newdirection)
accum= sorted(accum, key=sortKey)

newfout = open(FOUT, 'w')

for i in range(0,3,1):
  for j in range(0,4,1):
    if j == 3 and i != 2:
      newfout.write(str(accum[i][j]) + "\n")
    elif j==3 and i == 2:
      newfout.write(str(accum[i][j]))
    else:
      newfout.write(str(accum[i][j]) + ",")
