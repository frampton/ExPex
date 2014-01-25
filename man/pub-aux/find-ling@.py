
#This aids in determining if "\ling"/"\ling@" macros are properly
#marked in the index and text.


f_in = open("../core/expex.tex","r")
f_out = open("found-ling@.txt","w")

for x in f_in :
   k = x.find("ling@")
   if x.find("\\define") > -1 and k != -1 and x[k-1] != "\\" :
      f_out.write(x)

f_in.close()
f_out.close()








