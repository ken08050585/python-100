#题目：输入三个整数x,y,z，请把这三个数由小到大输出。
x=int(input("integer:\n"))#輸入x
y=int(input("integer:\n"))#輸入y
z=int(input("integer:\n"))#輸入z
a=[x,y,z]#將x,y,z加入陣列
a.sort()#使用sort函數自動排列
print(a)