# MySQL Review
## 基本函数
- **DISTINCT** 去重
```sql
SELECT DISTINCT name FROM table #对姓名去重后提取数据
```
- **IFNULL(item,value)** 类似于ifelse语句，如果判断对象是NULL则返回value
```sql
SELECT IFNULL(name,'noname') FROM table #如果姓名为空则填充'noname'
```
- **LIMIT a OFFSET b** 输出数据时跳过前b行并只输出接下来的a行：注意LIMIT内不能出现计算，因此a，b只能是int数字
```sql
SELECT name FROM table
LIMIT 11 OFFSET 9 #输出10-20行的数据
```
- **ROW_NUMBER()/RANK()/DENSE_RANK()OVER()** 排序函数
  - **ROW_NUMBER()** 常规排序函数，返回排名为123456....
  - **RANK()** 跳跃排序函数，如存在相同值则排名相同，后续排名不连续，如1,2,2,4,4,4,7
  - **DENSE_RANK()** 连续排序函数，如存在相同值则排名相同，后续排名连续，如1,2,2,3,3,3,4
- **PARTITION BY** 窗口函数：常搭配排序函数/求和函数等使用
```sql
SELECT RANK()OVER(PARTITION BY class ORDER BY score DESC) #返回跳跃排序排名，排序对象为score降序，窗口函数限定按class分开排序
FROM table
```
- **WHERE/HAVING** 设定一些筛选条件，要注意二者之间的区别！！！
  - **WHERE** 是一个约束声明，是在查询结果集返回之前**约束来自数据库**的数据，且WHERE中不能使用聚合函数
  - **HAVING** 是一个过滤声明，是在查询结果集返回以后**对查询结果进行的过滤操作**，在Having中可以使用聚合函数，通常与GROUP BY语句联合使用，用来过滤由GROUP BY语句返回的记录集
## 日期相关函数
- **DATE()** 将datetime的格式转化为YYYY-MM-DD
- **DATETIME()** 将datetime的格式转化为YYYY-MM-DD HH:MM:SS
- **DATEPART(UNIT,datetime)** 返回datetime中指定UNIT部分的整数
```sql
SELECT DATEPART(MONTH, '2004-10-25') #返回月份的整数，即10
```
- **DATEDIFF(datetime1, datetime2, unit)** 计算两个时间的差值，并转换成指定的单位
  - 注意：datetime1和datetime2只能是datetime格式，不能是date格式
  - unit可以是yyyy、mm、dd、hh、mi、ss，或是year、month、day、hour
```sql
SELECT DATEDIFF(dt1,dt2,day) #计算两个时间相差多少天
```
- **DATE_FORMAT(datetime,format)** 用于以不同的格式显示日期/时间数据
```sql
SELECT DATE_FORMAT(datetime, "%Y-%m") #转换为“YYYY-mm”的格式
```
- **DATE_SUB(datetime, INTERVAL n UNIT)** 对datetime进行计算, 返回减去n个UNIT时间的datetime
```sql
SELECT DATE_SUB("2017-06-15 09:34:21", INTERVAL 15 MINUTE) #返回减去15分钟后的时间
```
- 
