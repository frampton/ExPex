
def goop (x) :
   if x < 0 : u1 = "-"
   else : u1 = "+"
   x = abs(x)
   u2 = x / 60
   u4 = x % 60
   if u4 < 10 : u3 = "0"
   else : u3 = ""
   return u1 + str(u2) + ":" + u3 + str(u4)

import sys,urllib,string,re

tide_correction = 0
get_month = "Oct"
get_place = "Westport-Harbor-Westport-River"

place_name = "Westport Cottage"

http_file = ("http://www.boatma.com/tides/print/" + get_month + "/" +
   get_place + ".html")

#urllib.urlretrieve(http_file,"tt-raw.txt")

rawfile=open("tt-raw.txt","r")
cleanfile = open("tt-clean.txt","w")

place_pat = re.compile('^<CENTER><FONT SIZE\=\+1><B>(.*)</B></FONT></CENTER>')
month_pat = re.compile('^<CENTER><B><FONT COLOR\="\#CC0000">(.*)<BR>Tide Chart</FONT></B></CENTER>$')
year_pat = re.compile('<CENTER><FONT face\="arial" SIZE\=-1 face\="arial"><B>(.*)</B>')
tabular_cell_pat = re.compile(
   '<TD bgcolor="\#\w\w\w\w\w\w"><FONT face\="arial" SIZE\=-1> *(.*)</FONT></TD>')
moon_pat = re.compile('<TD bgcolor="#ffffff"><FONT SIZE=-1><img src="http://www.boatma.com/tides/' +
   '(.+)' + '.gif"></FONT></TD>')

semi_raw_data = []
L = []
for u in rawfile:
   z = re.search(tabular_cell_pat,u)
   if z:
      L.append(z.group(1))
      if len(L) == 12:
         semi_raw_data.append(L)
         L = []
   else:
      z = re.search(place_pat,u)
      if z:
         tt_place = z.group(1)
      else:
         z = re.search(month_pat,u)
         if z:
            tt_month = z.group(1)
         else:
            z = re.search(year_pat,u)
            if z:
               tt_year = z.group(1)
            else:
               z = re.search(moon_pat,u)
               if z:
                  zz = z.group(1)
                  if zz == "mnew":
                     semi_raw_data[len(semi_raw_data)-1].append("new")
                  elif zz == "mfl":
                     semi_raw_data[len(semi_raw_data)-1].append("full")

rawfile.close()
cleanfile.close()

def showlist (L):
   for x in L : print x
#showlist(semi_raw_data)
# tt_place, tt_month, tt_year are set
# semi_raw_data has all the daily data

def minutes (strtime,ampm):
   st0 = strtime.split()
   strtime = st0[0]
   if len(st0)>1 and st0[1]=="PM" and ampm == "am": ampm = "pm"
   st = strtime.split(":")
   hrs = int(st[0])
   if ampm == "am" :
      if hrs == 12 : hrs = 0
   else:
      if hrs < 12 : hrs = hrs + 12
   return(60*hrs + int(st[1]))

for x in semi_raw_data:
   x[0] = x[0][0:3]
   x[1] = int(x[1])
   for n in [3,5,7,9]:
      if len(x[n]) == 0: x[n]=None
      else: x[n] = int(10*float(x[n]) + .001)
   for n in [2,6,10]:
      if len(x[n]) == 0: x[n]=None
      else: x[n]=minutes(x[n],"am")
   for n in [4,8,11]:
      if len(x[n]) == 0: x[n] = None
      else: x[n]=minutes(x[n],"pm")
   for n in [2,4,6,8,10,11]:
      if isinstance(x[n],int): x[n] = x[n] + 1440*(x[1]-1)

daylist = []
eventlist = []
moonlist = {}
for x in semi_raw_data:
   if len(daylist) < 7: daylist.append(x[0][0:3])
   for n in [2,4]:
      if x[n]: eventlist.append([x[n]+tide_correction,"H",x[n+1]])
   for n in [6,8]:
      if x[n]: eventlist.append([x[n]+tide_correction,"L",x[n+1]])
   eventlist.append([x[10],"SR"])
   eventlist.append([x[11],"SS"])
   if len(x) > 12 :
      z = x[1]
      zz = x[12]
      moonlist[z]=zz

eventlist.sort(key=lambda(x):x[0])

def convert_to_stringtime (longtime):
   longtime = longtime % 1440  # 1440=60*24
   x = longtime / 60
   if x >= 12 :
      suffix = "pm"
      x = x - 12
   else: suffix = "am"
   if x == 0: x = 12
   return str(x) + str( longtime % 60 ).rjust(2,"0"), suffix

def goodtime (x) :
   z = convert_to_stringtime(x)
   return( z[0] + z[1] )

def istide(n) :
   e = eventlist[n]
   if e[1] == "L" or e[1] == "H" : return(True)
   else : return(False)

def isSRSS(n) :
   e = eventlist[n]
   if e[1] == "SS" or e[1] == "SR" : return(True)
   else : return(False)

def prevtide(n) :
   for k in range(n-1,-1,-1):
      if eventlist[k][1]=="L" or eventlist[k][1]=="H":
         return(k)
   return(None)

def nexttide(n) :
   for k in range(n+1,len(eventlist)):
      if eventlist[k][1]=="L" or eventlist[k][1]=="H":
         return(k)
   return(None)

for n in range(0,len(eventlist)) :
   if istide(n) :
      if nexttide(n) != None :
         eventlist[n].append(
            eventlist[nexttide(n)][2] - eventlist[n][2] )
      else: eventlist[n].append( -999 )
   elif isSRSS(n) :
      k1 = prevtide(n)
      k2 = nexttide(n)
      if k1 != None and k2 != None :
         r1 = eventlist[n][0]-eventlist[k1][0]
         r2 = eventlist[k2][0]-eventlist[n][0]
         if r1 < r2 :
            eventlist[n].append(eventlist[k1][1])
            eventlist[n].append(r1)
         else :
            eventlist[n].append(eventlist[k2][1])
            eventlist[n].append(-r2)

for x in eventlist:
   x.insert(0,x[0]/1440 + 1)
   x[1] = goodtime(x[1] % 1440)

eventlist.sort(key=lambda(x):[x[0],x[2] == "L" or x[2] == "H"])
#showlist(eventlist)

if tide_correction == 0: z=""
elif tide_correction > 0: z=" [+" + str(tide_correction) + " correction]"
else: z=" ["+ str(tide_correction) + " correction]"
print("\\global\\headline={" + get_place + z + "\\qquad " +
   tt_month + ", " + tt_year + "\\hfil}%")

whichday = 1
k = 4

def decadjust (x) :
   if x == -999 : return( "{\\relax}" )
   else :
      if x > 0 : z = "\\uparrow "
      else : z = "\\downarrow "
      return z + "{:.1f}".format(abs(x/10.0))

#
#
#def finishday(prevday) :
#   if whichtide < 4 : print "\\notide"
#   print "\\moon",
#   if prevday in moonlist : print moonlist[prevday]
#   else : print "{}"
#   print "\\endday"
#   prevday += 1
#   whichtide = 1

#prevday = 0
#whichtide = 4
#for x in eventlist:
#   currday = x[0]
#   if x[2] == "SR" :
#      if k < 4 : print "\\notide"
#      k = 0
#      if x[0] > prevday : finishday(prevday)
#         print "\\moon", mooninfo(currday-1)
#         print "\endday"
#      print "\day", x[0], daylist[ ( x[0] - 1 ) % 7]
#      print "\sunrise", x[1], x[3], goop(x[4])
#   elif x[2] == "SS" :
#      print "\sunset", x[1], x[3], goop(x[4])
#   elif x[2] == "L" or x[2] == "H" :
#      print "\\tide", x[1], x[2], "{:.1f}".format(x[3]/10.0), \
#         decadjust(x[4])
#      k += 1
#if k < 4 : print "\\notide"
#print "\endday"
#
def mooninfo(x) :
   if x in moonlist : print moonlist[x]
   else : print "{}"

prevday = 0
tidecount = 0

def finishday() :
   global tidecount, prevday
   if tidecount < 4 :
      print "\\notide"
      tidecount = 0
   print "\\moon",
   if prevday in moonlist : print moonlist[prevday]
   else : print "{}"
   print "\\endday"

for x in eventlist:
   if x[0] > prevday and prevday > 0 : finishday()
   if x[2] == "SR" :
      prevday = x[0]
      print "\day", x[0], daylist[ ( x[0] - 1 ) % 7]
      print "\sunrise", x[1], x[3], goop(x[4])
   elif x[2] == "SS" :
      print "\sunset", x[1], x[3], goop(x[4])
   elif x[2] == "L" or x[2] == "H" :
      print "\\tide", x[1], x[2], "{:.1f}".format(x[3]/10.0), \
         decadjust(x[4])
      tidecount += 1
finishday()


