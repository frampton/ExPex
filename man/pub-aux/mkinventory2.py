
import re

f = open("localexpex.tex","r")
#f_out = open("inventory.txt","w")

s = ""
for x in f : s = s + x[:-1]

bracks = r" *(?:\[(.*?)\])?"
braces = r" *\{([^\}]*)\}"

def ml (keykind,what) :
   r1 = re.compile(r"(?<!def)(\\" + keykind + ")" + what)
   L = r1.findall(s)
   for x in L : print x

#ml( "define@key", bracks + braces + braces )
#ml( "define@lingcmdkeys" , braces )
#ml( "define@ling@cmdkeys" , braces )
#ml( "define@lingincskipkeys" , braces )
#ml( "define@lingincdimenkeys" , braces )

r = re.compile(r"\\def\\([a-zA-Z]+)[ \#]")
L = r.findall(s)
known = ['ExPexMessage','csname','setlist']
for x in L :
   for y in known :
      if L.count(y) > 0 : L.remove(y)
for x in L : print "\\" + x

f.close()
#f_out.close()





