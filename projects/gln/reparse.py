

infile = open("peacock.tex","r")

for u in infile:
   if u[1:4] == "gla" :
      glastring = u.split()
   if u[1:4] == "glb":
      glbstring = u.split()
      for j in range(0,len(glastring)):
         if j < len(glbstring) : v = glbstring[j]
         else: v = ""
         if glastring[j]!="\gla"  and glastring[j]!="//":
            print glastring[j] + "[" + v + "] "





infile.close()



