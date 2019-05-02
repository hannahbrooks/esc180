import sys

NUMBER=""
WORD=""
nargs=len(sys.argv)
skip=False
for i in range(1,nargs):
   if not skip:
      arg=sys.argv[i]
      print("INFO: processing",arg)
      if arg == "--n":
         if i != nargs-1:
            NUMBER=sys.argv[i+1]
            skip=True
      elif arg == "--word":
         if i != nargs-1:
            WORD=sys.argv[i+1]
            skip=True
      else:
         print("ERR: unknown arg:",arg)
   else:
      skip=False

print("INFO: NUMBER",NUMBER)
print("INFO: WORD",WORD)
