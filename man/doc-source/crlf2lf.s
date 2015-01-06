
/*proc convert_type (string s_type)
   integer f_handle, save_eol
   string f_name[100]
   save_eol = Query(EOLType)
   Set(EOLType,2)
   f_handle = FindFirstFile("*." + s_type,_NORMAL_)
      f_name = FFName()
      EditFile(f_name)
   while FindNextFile(f_handle,_NORMAL_)
      f_name = FFName()
      EditFile(f_name)
      SaveAndQuitFile()
   endwhile
   Set(EOLType,save_eol)
   SaveAndQuitFile()
end

integer proc has_extension ( string f_name )
   integer flag
   if Pos(".",f_name) > 0 flag = 1
   else flag = 0
   endif
   return(flag)
   end*/

proc find_no_extension ()
   integer f_handle
   string f_name[100]
   Set(EOLType,2)
   f_handle = FindFirstFile("*.tex" ,_NORMAL_)
      f_name = FFName()
      if Pos(".",f_name) == 0 Warn(f_name) endif
   while FindNextFile(f_handle,_NORMAL_)
      f_name = FFName()
      if Pos(".",f_name) == 0 Warn(f_name) endif
   endwhile
end



proc main ()
//   convert_type("tex")
//   convert_type("txt")
   find_no_extension()
   end
