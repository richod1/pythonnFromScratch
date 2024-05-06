from collections import defaultdict

def group_anagram(a):
    dtdict=defaultdict(list)
    for i in a:
        sorted_i=" ".join(sorted(i))
        dtdict[sorted_i].append(i)
    return dtdict.values()


words=["tea","eat","bat","tab","ate","arc","car"]

print(group_anagram(words))