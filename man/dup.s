
proc main ()
if Find("\framedisplay","b")
   BegLine()
   Down()
   UnMarkBlock()
   MarkLine()
   if Find("\endframedisplay","")
      Up()
      MarkLine()
      Down()
      BegLine()
      case YesNo("Make code display?")
         when 0
            return()
         when 1
            AddLine("|endcodedisplay")
            InsertLine("\codedisplay~")
            CopyBlock()
         endcase
      UnMarkBlock()
      endif
   endif
end

