
/* Sort alphabetically*/
proc AlphaSort ()
UnMarkBlock()
BegFile()
MarkLine()
EndFile()
MarkLine()
Sort()
UnMarkBlock()
BegFile()
lReplace("{0@}{[1-9][0-9]@}"," \2","gnx")
end

proc RenameAndSave ()
string s[100]
integer n
n = GetBufferID("0.idx")
if n > 0 AbandonFile(n) endif
EditFile("0.idx")
s = SplitPath(CurrFileName(),_DRIVE_ | _NAME_)
n = GetBufferID(s+"-index.tex")
if n > 0 AbandonFile(n) endif
ChangeCurrFilename(s+"-index.tex",_OVERWRITE_)
end

proc JoinEntries ()
string s1[120],s2[120],t1[4],t2[4]
BegFile()
while CurrLine() < NumLines()
lFind("{^.*\\enspace }{.*}$","xgnc")
s1 = GetFoundText(1)
t1 = GetFoundText(2)
Down()
lFind("{^.*\\enspace }{.*}$","xgnc")
s2 = GetFoundText(1)
t2 = GetFoundText(2)
if s1 == s2
   if Val(t2) > Val(t1) + 1
      Up()
      EndLine()
      InsertText(", " + t2)
      Down()
      endif
   DelLine()
   endif
endwhile
end

proc main ()
integer j
string s[120],r[11],t[4]
RenameAndSave()
for j = 1 to NumLines()
   GotoLine(j)
   if lFind("\\indexentry\{{[\\\| ]@}{.*}\}\{{[0-9]@}\}","cgnx")
      s = GetFoundText(1) + GetFoundText(2)
      r = GetFoundText(2)
      t = GetFoundText(3)
      while Length(t) < 3 t = "0" + t endwhile
      r = r + "!!!!!!!!!!"
      if (r[1] >= "A") and (r[1] <= "Z")
         r = InsStr("b",r,11)
      elseif (r[1] >= "a") and (r[1] <= "z")
         r = InsStr("a",r,11)
      else
         r = InsStr("!",r,1)
      endif
   DelLine()
   InsertLine("{"+Lower(r)+"}" + s + "\enspace"+ t)
   endif
endfor
AlphaSort()
lReplace("\{.*\}","","xgn")
JoinEntries()
JoinEntries()
lReplace("^.*:: ","\\quad ","xgn")
BegFile()
end


