
integer proc Fetch (string tag)
string target[100]
integer n
Dos("kpsewhich " + tag + " >kresults.txt",
   _START_HIDDEN_ | _DONT_PROMPT_ )
PushPosition()
CreateTempBuffer()
InsertFile("kresults.txt")
target = GetText(1,100)
EraseDiskFile("kresults.txt")
AbandonFile()
PopPosition()
n = 0
if ( Length(target) > 0 ) and EditFile(target,_DONT_PROMPT_)
   n = 1 endif
return(n)
end

proc GetFileonCursorLine (string ext)
string tempstr [80]
if lFind("\\input #" + "{[~ ]#}","gcx")
   tempstr = GetFoundText(1)
   if SplitPath(tempstr,_EXT_)==""
      tempstr = tempstr + "." + ext endif
   if Fetch(tempstr) else Message("File not found") endif
   endif
end

<F9> GetFileonCursorLine ("tex")

//\input pst-asr

//   Find("\\" + LoadTriggers + ".# ","xcg")
//     if returnpred == 1 PushPosition() endif
//     Find("[ ]+\c[~ ]","xc")
//     MarkStream()
//     Find("\c{ }|{$}","xc")
//     Left()
//     MarkStream()
//     tempstr = GetMarkedText()
//     UnMarkBlock()
//     if SplitPath(tempstr,_EXT_)==""
//          GetTexFile(tempstr+".tex")
//          else
//          EditFile(tempstr)
//          endif
//     if returnpred == 1 PopPosition() Down() endif
//     else
//     Down()
////     Warn("No \input or \get on line")
//     endif
//end


