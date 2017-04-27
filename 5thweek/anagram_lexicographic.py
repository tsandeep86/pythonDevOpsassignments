"""
Given an array of strings, group anagrams together.
For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], Return:
[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
For the return value, each inner list's elements must follow the lexicographic
order.
All inputs will be in lower-case.
"""

l=["eat", "tea", "tan", "ate", "nat", "bat"]
#l=["ate"]
tl=[]
nl=[]
ld={}
for i in range(len(l)):
    tl.append(l[i])

    for j in range(len(tl[i])):

        nl.append(tl[i][j])
        nl.sort() 

    #ld.update({tl[i]:"".join(nl)})
    if "".join(nl) not in ld:
        ld.update({"".join(nl):[tl[i]]})
    else:
        ld["".join(nl)].append(tl[i])
    del nl[:]

#print ld
print ld.values()    












        
