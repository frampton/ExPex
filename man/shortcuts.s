
proc InsertInventory ()
InsertLine("\begininventory")
InsertLine("\omit Macro:\quad")
In

menu ShortCuts ()
"TT &Escape"           ,  InsertText("«»")
"&Inventory"   ,  InsertInventory()
end

<Alt F5>   ShortCuts()

