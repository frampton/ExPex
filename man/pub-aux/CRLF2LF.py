
import os,sys

convert_files_with_extensions = ("tex","txt","py","sty","idx","","toc")
in_directories = ["..\\doc-source","..\\..\\expex"]

def extension (f_name) :
   z = f_name.split(".")
   if len(z) > 1 : return(z[1])
   else : return("")

def convert_dir (do_dir) :
   for f_name in os.listdir("."):
      f_name_out = "convert_temp"
      if os.path.isfile( f_name ) :
         if extension(f_name) in convert_files_with_extensions :
            print do_dir + "\\" + f_name
            f_in = open(f_name,"rb")
            f_out = open(f_name_out,"wb")
            for x in f_in : f_out.write( x.replace("\r\n","\n") )
            f_in.close()
            f_out.close()
            os.remove(f_name)
            os.rename(f_name_out,f_name)

for do_dir in in_directories :
   save_dir = os.getcwd()
   os.chdir(do_dir)
   convert_dir(do_dir)
   os.chdir(save_dir)

def extension (f_name) :
   z = f_name.split(".")
   if len(z) > 1 : return(z[1])
   else : return("")


