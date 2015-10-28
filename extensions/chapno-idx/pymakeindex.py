
import re,sys

f_name = sys.argv[1]

f = open(f_name + ".idx","r")
g = open(f_name + ".ind","w")

L = []

for x in f :
   m = re.search(r"\indexentry{" + "(.*)" + r"}{" + "(.*)" + r"}",x)
   if m : L.append( m.group(1,2) )

L.sort( key = lambda z : z[0].lower() )

def indwrite(x) : g.write( x + "\n" )

indwrite( r"\begin{theindex}" + "\n" )
flag = L[0][0][0].lower()
for x in L :
   u = x[0][0].lower()
   if u > flag:
      flag = u
      indwrite( "\n" + r"\indexspace" + "\n")
   indwrite( r"\item " + x[0]+ r", " + x[1] )

indwrite( "\n" + r"\end{theindex}" )


