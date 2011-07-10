
proc finddup ()
string s[30]
BegLine()
if Find("{\\def\\.*\{}","x")
   s = GetFoundText(1)
   Down()
   Message("searching for " + s)
   Find(s,"v")
   endif
end

<F8> finddup()


