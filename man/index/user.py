import re

infile = open("..\\0.idx","r")
outfile = open("idx.txt","w")
for xline in infile:
   x = r"indexentry{|" + "([a-z]*)" + r"|\user}" + "(.*)$"
   m = re.search(x,xline)
   print(m)
   if m == None :
      pass
   else :
      print(m.group(1))
      print(m.group(2))
#      print(m.group(1)+"\\ling"+m.group(2)+m.group(3)+"\n")
#      outfile.write(m.group(1)+r"\ling"+m.group(2)+m.group(3)+"\n")

outfile.close()
infile.close()

