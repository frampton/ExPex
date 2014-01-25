
#Before this script is run, the file "filelist.txt" has to be created
#by running
#
#   dir ..\*.tex > filelist.txt
#
#in DOS and deleting the excess material.  After it is run, material
#must be added to the beginning and end of "gathered.tex" to make it
#Texable.  Some fine tuning must then be done - problems deleted, etc.


gather_source = open("filelist.txt","r")
gathered = open("gathered.tex","w")
f_preamble = open("expex-demo-preamble.tex","r")
f_close = open("expex-demo-close.tex","r")

#for x in f_preamble : gathered.write(x)

filelist = []
for x in gather_source :
   if len(x) > 1 : filelist.append(x[:-1])
gather_source.close()

for f_name in filelist :
   f = open("..\\" + f_name,"r")
   flag = 0
   for line in f :
      if line.find("\\framedisplay") != -1 :
         if line.find("%[exclude]") == -1 :
            gathered.write("\\bigskip\r")
            gathered.write("\r")
            gathered.write("\\filbreak\\hrule\\medskip\r")
            gathered.write("\r")
            gathered.write("\\begingroup\r")
            flag = 1
         else : flag = 2
      elif line.find("\\endframedisplay") != -1 and flag == 1 :
         gathered.write("\\endgroup\r")
         flag = 0
      elif flag == 1 :
         gathered.write(line)
   f.close()

#for x in f_close : gathered.write(x)


gathered.close()
gather_source.close()
f_preamble.close()
f_close.close()
