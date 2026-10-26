d = {"a": "hello", "b": "world"}
print(d)
s = {1, 2, 3} # hash set
s.add(3)
print(s)

t = (1,2,3)

data_stc = {"list": {"mutable": True, "Ordered" : True, "Duplicates": True , "lookup": "o(N)"},
                     ,"tuple": {"mutable": False , "Ordered": True, "duplicates":True, "lookup": "O(N)" }, 
                     "dict" : { "mutable": True,  "ordered": True, "duplicates": True, "lookup": "O(1"  } }
