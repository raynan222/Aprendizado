I=1
J=7
while(I!=11):
   aux=J
   while(J!=aux-3):
       print("I=" + str(I), " J=" + str(J))
       J-=1
   I+=2
   J=aux+2