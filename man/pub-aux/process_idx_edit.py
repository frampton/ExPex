
#Tranform the idx file produced when the doc is Texed into a file
#suitable for "JF-mkindex.tex", edited and rearranged to make checking
#on editing easier.

f_in = open("../0.idx","r")
f_out = open("0-index-edit-check.tex","w")

index_list = []
for x in f_in :
   x = x.split("}{")
   x[0] = x[0][12:]
   x[1] = x[1][:-2]
   idx_key = x[0][1:3].replace("\\","") + x[0][3:]
   k = idx_key.find("|")
   idx_key = idx_key[:k]
   index_list.append( {'name':x[0],
      'page': [ int(x[1]) ],
      'key': idx_key } )
index_list.sort( key = lambda x : x['key'] )

L2 = []
sofar = index_list[0]
for j in range(1,len(index_list)) :
   if index_list[j]['name'] == sofar['name'] :
      if sofar['page'] != index_list[j]['page'] :
         sofar['page'] = sofar['page'] + index_list[j]['page']
   else :
      L2.append(sofar)
      sofar = index_list[j]
L2.append(sofar)

def key1 (x) :
   if len(x['key']) == 1 and x['name'][1] != "\\" : return(0)
   else : return(1)

def key2 (x) :
   if x['name'][1] == "\\" : return(1)
   else : return(0)

def key3 (x) :
   if x['name'].find("\\user") != -1 : return(0)
   else : return(1)

def key4 (x) : return( x['key'].lower() )

L2.sort( key = lambda x : ( key1(x), key2(x), key3(x) , key4(x) ) )

#for x in L2: print x

for x in L2 :
   pages = x['page']
   f_out.write( x['name'] + "\\enspace" + " " + str(pages[0]) )
   for n in range(1,len(pages)) :
      f_out.write( ", " + str(pages[n]) )
   f_out.write("\r")
f_in.close()
f_out.close()

