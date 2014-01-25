
#Goes through "expex.tex" and extracts parameters and public macros.
#They are alphabetically sorted and written to "namelist.txt".  This
#helps to edit "0-index.tex" to make sure page references exist.

#It assumes that when multiple parameters are defined, the names are
#all on one line.

names_source = open("../../core/expex.tex","r")
raw_names = open("namelist.txt","w")

par_list = []
mac_list = []

for x in names_source :
   flag = 0
   if x.find("\\define@") == 0 :
      k = x.find("{")
      x = x[k:-1].replace("{ling}","")
      x = x.replace("{labels}","")
      x = x.replace("[ling@]","")
      k = x.find("}")
      x = x[:k+1]
      x = x.replace("{","").replace("}","")
      L = x.split(",")
      for x in L : par_list.append(x)
   elif x.find("\\def\\") == 0 :
      k = x.find("{")
      x = x[4:k]
      if x.find("@") == -1 :
         k = x.find("#")
         if k > 0 : x = x[:k]
         mac_list.append(x)
par_list.sort(key=str.lower)
mac_list.sort(key=str.lower)
for x in par_list : raw_names.write(x + "\r")
for x in mac_list : raw_names.write(x + "\r")

names_source.close()
raw_names.close()








