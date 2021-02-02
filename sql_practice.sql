-- Refer to https://zhuanlan.zhihu.com/p/38354000
create table student(
    '学号' VARCHAR(255),
    '姓名' VARCHAR(255),
    '出生日期' DATE,
    '性别' VARCHAR(255),
    PRIMARY KEY ('学号')
);

create table score(
    '学号' VARCHAR(255),
    '课程号' VARCHAR(255),
    '成绩' FLOAT(3),
    PRIMARY KEY('学号', '课程号')
);

create table course(
    '课程号' VARCHAR(255),
    '课程名称' VARCHAR(255),
    '教师号' VARCHAR(255),
    PRIMARY Key('课程号')
);

create table teacher(
    '教师号' VARCHAR(255),
    '教师姓名' VARCHAR(255),
    PRIMARY KEY('教师号')
);

insert into student(学号,姓名,出生日期,性别) 
values('0001' , '猴子' , '1989-01-01' , '男');

insert into student(学号,姓名,出生日期,性别) 
values('0002' , '猴子' , '1990-12-21' , '女');

insert into student(学号,姓名,出生日期,性别) 
values('0003' , '马云' , '1991-12-21' , '男');

insert into student(学号,姓名,出生日期,性别) 
values('0004' , '王思聪' , '1990-05-20' , '男');

insert into score(学号,课程号,成绩) 
values('0001' , '0001' , 80);

insert into score(学号,课程号,成绩) 
values('0001' , '0002' , 90);

insert into score(学号,课程号,成绩) 
values('0001' , '0003' , 99);

insert into score(学号,课程号,成绩) 
values('0002' , '0002' , 60);

insert into score(学号,课程号,成绩) 
values('0002' , '0003' , 80);

insert into score(学号,课程号,成绩) 
values('0003' , '0001' , 58);

insert into score(学号,课程号,成绩) 
values('0003' , '0002' , 80);

insert into score(学号,课程号,成绩) 
values('0003' , '0003' , 59);

insert into course(课程号,课程名称,教师号)
values('0001' , '语文' , '0002');

insert into course(课程号,课程名称,教师号)
values('0002' , '数学' , '0001');

insert into course(课程号,课程名称,教师号)
values('0003' , '英语' , '0003');

insert into teacher(教师号,教师姓名) 
values('0001' , '孟扎扎');

insert into teacher(教师号,教师姓名) 
values('0002' , '马化腾');

-- 这里的教师姓名是空值（null）
insert into teacher(教师号,教师姓名) 
values('0003' , null);

-- 这里的教师姓名是空字符串（''）
insert into teacher(教师号,教师姓名) 
values('0004' , '');

-- Questions:
-- 查询姓“猴”的学生名单
select * from student where 姓名 like '猴%'

-- 查询姓“孟”老师的个数
select count(*) from teacher where 教师姓名 like '孟%'

-- 查询课程编号为“0002”的总成绩
select sum(成绩) from score where 课程号 == '0002'

-- 查询选了课程的学生人数
select count(distinct 学号) from score

-- 查询各科成绩最高和最低的分， 以如下的形式显示：课程号，最高分，最低分
select 课程号, max(成绩) as 最高分, min(成绩) as 最低分 from score group by 课程号

-- 查询每门课程被选修的学生数
select 课程号, count(distinct 学号) as 学生数 from score group by 课程号

-- 查询男生、女生人数
select 性别, count(性别) from student group by 性别

-- 查询平均成绩大于60分学生的学号和平均成绩
select 学号, avg(成绩) as 平均成绩 from score group by 学号 having 平均成绩 > 60

-- 查询至少选修两门课程的学生学号
select 学号, count(课程号) from score group by 学号 having count(课程号) >= 2

-- *查询同名同姓学生名单并统计同名人数
select 姓名, count(*) from student group by 姓名 having count(*) > 1

-- 查询不及格的课程并按课程号从大到小排列
select 课程号 from score where 成绩 < 60 order by 课程号 desc

-- 查询每门课程的平均成绩，结果按平均成绩升序排序，平均成绩相同时，按课程号降序排列
select 课程号, avg(成绩) as 平均成绩 from score group by 课程号 order by 平均成绩, 课程号 desc

-- 检索课程编号为“0004”且分数小于60的学生学号，结果按按分数降序排列
select 学号 from score where 课程号 = '0004' and 成绩 < 60 order by 成绩 desc

-- 统计每门课程的学生选修人数(超过2人的课程才统计)
-- 要求输出课程号和选修人数，查询结果按人数降序排序，若人数相同，按课程号升序排序
select 课程号, count(*) as 选修人数 from score group by 课程号 having 选修人数 > 2 order by 选修人数 desc, 课程号

-- *查询两门以上不及格课程的同学的学号及其平均成绩
-- （这题目回答有点问题，计算的平均成绩没包括及格的成绩）
select 学号, avg(成绩) as 平均成绩 from score where 成绩 < 60 group by 学号 having count(*) > 2

-- 查询学生的总成绩并进行排名
select 学号, sum(成绩) as 总成绩 from score group by 学号 order by 总成绩 desc

-- 查询平均成绩大于60分的学生的学号和平均成绩
select 学号, avg(成绩) as 平均成绩 from score group by 学号 having 平均成绩 > 60

-- *查询课程成绩小于60分学生的学号、姓名
select 学号, 姓名 from student where 学号 in (select 学号 from score where 成绩 < 60)

-- *查询没有学全所有课的学生的学号、姓名
select 学号, 姓名 from student where 学号 in (select 学号 from score group by 学号 having count(*) < (select count(*) from course))

-- 查询出只选修了两门课程的全部学生的学号和姓名
select 学号, 姓名 from student where 学号 in (select 学号 from score group by 学号 having count(*) == 2)

-- *1990年出生的学生名单
select * from student where year(出生日期) = 1990

-- *查询各科成绩前两名的记录
(select * from score where 课程号 = '0001' order by 成绩  desc limit 2)
union all
(select * from score where 课程号 = '0002' order by 成绩  desc limit 2)
union all
(select * from score where 课程号 = '0003' order by 成绩  desc limit 2);

-- *查询各学生的年龄（精确到月份）
select 学号, timestampdiff(month, 出生日期, now())/12  from student

-- *查询所有学生的学号、姓名、选课数、总成绩
select a.学号, a.姓名, sum(b.成绩) as 总成绩, count(b.课程号) as 选课数 
from student as a
left join score as b
on a.学号 = b.学号
group by a.学号

--查询平均成绩大于85的所有学生的学号、姓名和平均成绩
select a.学号, a.姓名, avg(b.成绩) as 平均成绩
from student as a
left join score as b
on a.学号 = b.学号
group by a.学号
having 平均成绩 > 85

-- 查询学生的选课情况：学号，姓名，课程号，课程名称
select a.学号, a.姓名, d.课程号, d.课程名称
from student as a
left join (select b.学号, b.课程号, c.课程名称 from score as b left join course as c on b.课程号 = c.课程号) as d
on a.学号 = d.学号
-- OR
select a.学号, a.姓名, c.课程号,c.课程名称
from student as a left join score as b on a.学号=b.学号
left join course as c on b.课程号=c.课程号;

-- *查询出每门课程的及格人数和不及格人数
select 课程号,
sum(case when 成绩 >= 60 then 1 else 0 end) as 及格人数,
sum(case when 成绩 < 60 then 1 else 0 end) as 不及格人数
from score
group by 课程号

-- 使用分段[100-85],[85-70],[70-60],[<60]来统计各科成绩，分别统计：各分数段人数，课程号和课程名称
select a.课程号, b.课程名称,
sum(case when 成绩 <= 100 and 成绩 >= 85 then 1 else 0 end) as '[100-85]',
sum(case when 成绩 < 85 and 成绩 >= 70 then 1 else 0 end) as '[85-70]',
sum(case when 成绩 < 70 and 成绩 >= 60 then 1 else 0 end) as '[70-60]',
sum(case when 成绩 < 60 then 1 else 0 end) as '[<60]'
from score as a
left join course as b
on a.课程号 = b.课程号
group by a.课程号

-- 查询课程编号为0003且课程成绩在80分以上的学生的学号和姓名
select a.学号, b.姓名 from score as a
left join student as b
on a.学号 = b.学号
where a.课程号 = '0003' and a.成绩 > 80

-- *使用sql实现将该表行转列为下面的表结构（列变为学号、课程0001、课程0002、课程0003，行为对应成绩）
select a.学号, a.成绩 as '课程0001', b.成绩 as '课程0002', c.成绩 as '课程0003' from
(select 学号,成绩 from score where 课程号 = '0001') as a
full outer join
(select 学号,成绩 from score where 课程号 = '0002') as b
on a.学号 = b.学号
full outer join
(select 学号,成绩 from score where 课程号 = '0003') as c
on b.学号 = c.学号
-- OR
select 学号,
max(case 课程号 when '0001' then 成绩 else 0 end) as '课程号0001',
max(case 课程号 when '0002' then 成绩 else 0 end) as '课程号0002',
max(case 课程号 when '0003' then 成绩 else 0 end) as '课程号0003'
from score
group by 学号;

-- 检索"0001"课程分数小于60，按分数降序排列的学生信息
select * from student as a
inner join score as b
on a.学号 = b.学号
where b.课程号 = '0001' and b.成绩 < 60
order by b.成绩 desc

-- 查询不同老师所教不同课程平均分从高到低显示
select a.课程号, c.教师姓名, avg(a.成绩) as 平均分 from score as a
inner join course as b
on a.课程号 = b.课程号
inner join teacher as c
on b.教师号 = c.教师号
group by a.课程号, c.教师姓名
order by 平均分 desc

-- 查询课程名称为"数学"，且分数低于60的学生姓名和分数
select a.姓名, b.成绩 from student as a
inner join score as b
on a.学号 = b.学号
inner join course as c
on b.课程号 = c.课程号
where c.课程名称 = "数学" and b.成绩 < 60

-- 查询两门及其以上不及格课程的同学的学号，姓名及其平均成绩
select a.学号, a.姓名, avg(b.成绩) as 平均成绩 from student as a
inner join score as b
on a.学号 = b.学号
where b.成绩 < 60 group by b.学号 having count(b.学号) >= 2

-- 查询不同课程成绩相同的学生的学生编号、课程编号、学生成绩
