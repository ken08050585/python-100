#题目：输入某年某月某日，判断这一天是这一年的第几天？
y=int(input("year:"))#輸入年分
m=int(input("month:"))#輸入月分
d=int(input("day:"))#輸入天數
a=[0,31,28,31,30,31,30,31,31,30,31,30,31]#建立一個平年月曆陣列
if y%4==0 and y%100!=0 or y%400==0:#判斷閏年，如果成立將二月份改成閏年天數
    a[2]=29
day=0#建立總天數
for i in range(13):#數字i從0跑到12代表月份
    if i<m:#判斷輸入月分，如果成立將該月份天數加總
        day+=a[i]
day+=d#補齊天數
print("it is the %dth day."%day)