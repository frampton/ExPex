
import re

f = open("..\\..\\expex\\expex.tex","r")
f_out = open("inventory.txt","w")

r1 = re.compile("(?<=,) *\n")
#any number of spaces at the end of a line following a comma gets reduced
#to a single space, eol is deleted, and a flag is set so that spaces at
#the beinning of the next line are eliminated

r2 = re.compile("%+[^%]*\n")
#the rightmost % (if there is one) and all following characters and eol
#are deleted and a flag is set as above

def readtexline(f) :
   """ generator function which reads lines and collapses them as
   necessary, so that the computation which follows does not have to deal
   with multiline parameter lists and the like
   """
   u, flag = ("",0)
   while True :
      v = f.readline()
      if v == "" :
         yield u + "\n"
         return
      if flag == 1 : u = u + v.lstrip()
      else: u = v
      u, flag = r2.subn("",u)
      if flag == 0 :
         u,flag = r1.subn(" ",u)
         if flag == 0 :
            yield u
            u = ""

# as parameters (and defined public macros) are located, they are made
#into a list, associated with a descriptor
def addpars (m,par_kind) :
   x = m.group(1)
   y = x.split(",")
   if not y : y = list(x)
   return [ (x.strip(),par_kind) for x in y]

V = []

for x in readtexline(f) :
   m = re.match(r"\\define@key(?:\[.*\])?{.*?}{(.*?)}",x)
   if m : V = V + addpars(m,"key")
   m = re.match(r"\\define@boolkey{.*?}\[.*?\]{(.*?)}",x)
   if m : V = V + addpars(m,"bool")
   m = re.match(r"\\define@choicekey{.*?}{(.*?)}",x)
   if m : V = V + addpars(m,"choice")
   m = re.match(r"\\define@ling@cmdkeys{(.*?)}",x)
   if m : V = V + addpars(m,"ling@cmd")
   m = re.match(r"\\define@lingcmdkeys{(.*?)}",x)
   if m : V = V + addpars(m,"lingcmd")
   m = re.match(r"\\define@lingincdimenkeys{(.*?)}",x)
   if m : V = V + addpars(m,"incdimen")
   m = re.match(r"\\define@lingincskipkeys{(.*?)}",x)
   if m : V = V + addpars(m,"incskip")
   m = re.match(r"\\defineglwlevels{(.*?)}",x)
   if m : V = V + addpars(m,"glwlevel")
   m = re.match(r"\\def(\\[a-zA-Z@]+)[\# {]",x)
   if m :
      x = m.group(1)
      if x.find("@") == -1 :
         V = V + addpars(m,"\\def")

V.sort(key=lambda x : x[0].lower())
for x in V : f_out.write( "{0:<22}".format(x[0]) + x[1] + "\r" )

f_out.write("----------------------------------------------\n")

V.sort(key=lambda x : x[1].lower())
for x in V : f_out.write( "{0:<22}".format(x[1]) + x[0] + "\r" )

f.close()
f_out.close()





