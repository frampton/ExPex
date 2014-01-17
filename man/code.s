

proc main ()
BegLine()
Find("\framedisplay","")
Mark(_LINE_)
Find("\endframedisplay","")
CopyBlock()
Replace("\framedisplay","\codedisplay","ln")
Replace("\endframedisplay","|endcodedisplay","ln")
UnMarkBlock()
end
