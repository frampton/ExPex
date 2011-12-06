
proc main ()
integer flag
flag = 0
EditFile("expex.tex")
AbandonFile()
EditFile("expex-src.tex")
ChangeCurrFileName("expex.tex",_OVERWRITE_)
BegFile()
repeat
   if lFind("^%/!","xgc")
         flag = 1
         Down()
      elseif lFind("^%!/","xgc")
         flag = 0
         Down()
      elseif lFind("^%","xgc") and ( flag == 0 )
         KillLine()
      else Down()
      endif
   until CurrLine() == NumLines()
end

