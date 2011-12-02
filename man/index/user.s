
proc main ()
   EditFile("0-idx.tex")
   AbandonFile()
   ChangeCurrFileName("0-idx.tex")
   while lFind("\|{[a-z]*}\|\\user\}{.*}$","x")
      AddLine("\indexentry{\ling" + GetFoundText(1) + "}"
         + GetFoundText(2))
      endwhile
   lReplace("\user","","gn")
end
