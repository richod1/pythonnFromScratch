# calculating for Mean
list1=[12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
mean=sum(list1)/len(list1)
print(mean)


# calculation for median
list1.sort()
# checking for even number
if len(list1) % 2==0:
    firstMiddle=list1[len(list1)//2]
    secondMiddle=list1[len(list1)//2-1]
    median=(firstMiddle+secondMiddle)/2
else:
    median=list1(len(list1)//2)
print(median)

# finding mode

frequency={}
for i in list1:
    frequency.setdefault(i,0)
    frequency[i]+=1

frequent=max(frequency.values())
for i,j in frequency.items():
    if j==frequent:
        mode=i

print(mode)