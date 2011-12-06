
proc main ()
integer n
n = 1
while FileExists("c:\users\john\dropbox\epbak\expex-src-" + Str(n) + ".tex")
   n = n + 1
   endwhile
EditFile("c:\users\john\ling\tex\expex\core\expex-src.tex")
SaveAs("c:\users\john\dropbox\epbak\expex-src-" + Str(n) + ".tex")
AbandonFile()
end


