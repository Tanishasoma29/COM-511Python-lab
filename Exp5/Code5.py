'''Experiment5: Write a program to reverse every Kth row in
a matrix.
CODE:'''
test_list=[[5,3,2],[8,6,3],[3,5,2],[3,6],[3,7,4],[2,9]]
print("The original list is:" + str(test_list))
k=int(input("Enter the row value want to reverse:"))
res=[]
for idx,ele in enumerate(test_list):
 if(idx+1)%k==0:
 res.append(list(reversed(ele)))
 else:
 res.append(ele)
print("After reversing tevery Kth row:" + str(res))
