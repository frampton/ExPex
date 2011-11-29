
def maketexfilenamelist  ():
   sourcefile = open('demofilelist.dat','r')
   filelist = []
   for x in sourcefile:
      if len(x)>1 :
         filelist.append('../' + x[:-1] + '.tex')
   sourcefile.close()
   return filelist

def getdisplays ( texfile ) :

   f = open(texfile,'r')
   docopy = 0
   excludeskip = 0
   for line in f:
      if line[:9] == "\\endinput":
         break
      elif line[:22] == "\\vskip\\lingbelowexskip":
         pass
      elif line[:23] == "\\framedisplay%[exclude]":
         excludeskip = 1
      elif line[:13] == "\\framedisplay":
         docopy = 1
         outfile.write("\\filbreak\\hrule\\medskip\n\n\\begingroup\n")
      elif line[:16] == "\\endframedisplay":
         docopy = 0
         if excludeskip == 0 :
            outfile.write("\\endgroup\n\\bigskip\n\n")
         excludeskip = 0
      else:
         if docopy == 1 :
            outfile.write(line)
   f.close()

   return texfile

#filelist = ["01_intro", "02_examples2", "03_XKV", "04_ex",
#   "05_MultiPart-Basics", "05_MultiPart-Advanced",
#   "05_MultiPart-Footnotes", "06_UserStyles", "07_Judgments",
#   "08_Glosses-Basic", "08_Glosses-Advanced", "10_Refs",
#   "09_Tables", "11_PSTricks", "12_PageBreaks"]

outfile = open('expex-demo.tex','w')
infile = open('demopreamble.tex','r')
for xline in infile :
   outfile.write(xline)
infile.close()
for xline in maketexfilenamelist():
   getdisplays(xline)
outfile.write('\\enddemo\\end{document}\\bye')
outfile.close()

