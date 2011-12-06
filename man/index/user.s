
proc main ()
   string lastline[80]
   EditFile("c:\users\john\ling\tex\expex\man\0.idx")
   if EditFile("c:\users\john\ling\tex\expex\man\index\index.tex") AbandonFile() endif
   ChangeCurrFileName("c:\users\john\ling\tex\expex\man\index\index.tex",_OVERWRITE_)
   while lFind("\|{[a-z]*}\|\\user\}{.*}$","x")
      AddLine("\indexentry{|\ling" + GetFoundText(1) + "|}"
         + GetFoundText(2))
      endwhile
   lReplace("\user","","gn")
   BegFile()
      repeat
      lReplace("^{\\indexentry\{\|}\\{.*}$","\1\2FIX","gcxn")
      until not Down()
   BegFile()
   MarkLine()
   EndFile()
   MarkLine()
   Sort(_IGNORE_CASE_)
   UnMarkBlock()
   BegFile()
   repeat
      lastline = GetText(1,CurrLineLen())
      Down()
      if GetText(1,CurrLineLen()) == lastline DelLine() endif
      until CurrLine() == NumLines()
   BegFile()
   repeat
      lReplace("^{\\indexentry\{\|}{.*}FIX$","\1\\\2","gcxn")
      until not Down()
   BegFile()
   lReplace("^{\\.*}\\","\1\\char92 ","xgn")
   lReplace("\|{.*}\|","\{\\tt \1\}","xgn")
   lReplace("[]","","gn")
   lReplace("{[a-z]}~","\1","gxn")
   lReplace("~","\char126 ","gn")
   SaveFile()
end
