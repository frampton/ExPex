
proc insertion (integer x)
case x
   when 0 InsertText(Chr(171))
   when 1 InsertText(Chr(187))
   when 2 InsertText(Chr(171)+Chr(187))
   when 3 InsertText(Chr(166))
   endcase
end

menu insertionmenu()
"<< >>" , insertion(2)
"<<" ,  insertion(0)
">>" ,  insertion(1)
"|-sub" , insertion(3)
end


proc main ()
   insertionmenu()
end

