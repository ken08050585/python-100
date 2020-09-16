#题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
for i in range(1,5): #數字i從1到4
 for j in range(1,5): #數字j從1到4
  for k in range(1,5): #數字k從1到4
   if i!=j and i!=k and j!=k: #如果三個數字不相等就印出
       print(i,j,k)