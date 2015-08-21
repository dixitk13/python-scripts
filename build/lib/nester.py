"""
GIVEN: a list and the invariant
EFFECT:  prints a item contents if its not a list, else calls itself
INVARIANT: The invariant is inv, which decides how many tab "\t" to be
put in front of each list variable when printing
the default value of inv is 0
STRATEGY: General recursion
EXAMPLES: fun1(items,0) -> prints the items in the list called items
where items -> ["member1","member2",["member1.1","member1.2"]]
"""
def fun1(item,indent=False,inv=0):
    #inv = 0
    for items in item:
        if isinstance(items,list):
            #inv+=1
            fun1(items,indent,inv+1)
        else:
            if indent:
                for tab in range(inv):
                    print("\t",end='')
            print(items)

