def alignLst(lists):
    r_lists = []    
    max_lens = [len(str(max(c, key = lambda x : len(str(x))))) for c in zip(*lists)]
    
    print(max_lens)
    
    for row in lists:
        r_lists.append('|'.join('{0:{width}}'.format(x, width = y) for x, y in zip(row, max_lens)))
        
    return r_lists

'''      
l1 = ["name","level","value"]
l2 = ["Some long name", "a level", "a value"]
l3 = ["An even longer name", "another level", "another value"]

lsts = []

lsts.append(l1)
lsts.append(l2)
lsts.append(l3)

alignLst(lsts)
'''