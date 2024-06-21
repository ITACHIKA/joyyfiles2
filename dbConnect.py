import mysql.connector

driver=mysql.connector.connect(user="itachika",password='1111',host='127.0.0.1')
cursor=driver.cursor()

try:
    cursor.execute("Drop Database test1")
except mysql.connector.errors.DatabaseError as e:
    print("DB not exist. Create one.")

try:
    cursor.execute("Create Database test1")
except mysql.connector.errors.DatabaseError as e:
    print("DB exists. Use existing one.")

tables={}

tables['Student']=(
    "CREATE TABLE `Student` ("
    "  `Sno` int(11) NOT NULL ,"
    "  `Sname` varchar(50) NOT NULL,"
    "  `Ssex` TEXT NOT NULL,"
    "  `Sage` int(5) NOT NULL,"
    "  `Sdept` varchar(50) NOT NULL,"
    "  PRIMARY KEY (`Sno`)"
    ") ENGINE=InnoDB"
)

tables['Course']=(
    "CREATE TABLE `Course` ("
    "  `Cno` varchar(20) NOT NULL,"
    "  `Cname` varchar(50) NOT NULL,"
    "  `Credit` int(10) NOT NULL,"
    "  PRIMARY KEY (`Cno`)"
    ") ENGINE=InnoDB"
)

tables['SC']=(
    "CREATE TABLE `SC` ("
    "  `Sno` int(11) NOT NULL ,"
    "  `Cno` varchar(10) NOT NULL,"
    "  `Grade` int(10) NOT NULL,"
    "  PRIMARY KEY (`Sno`,`Cno`)"
    ") ENGINE=InnoDB"
)

driver.connect(database="test1")

for i in tables:
    cursor.execute(tables[i])

stu_data="""
insert into student 
(Sno,Sname,Ssex,Sage,Sdept)
values
(10001,"Jack","男",21,"CS"),
(10002,"Rose","女",20,"SE"),
(10003,"Michael","男",21,"IS"),
(10004,"Hepburn","女",19,"CS"),
(10005,"Lisa","女",20,"SE");
"""

course_data="""
insert into course
(Cno,Cname,Credit)
values
("00001","DataBase",4),
("00002","DataStructure",4),
("00003","Algorithms",3),
("00004","OperatingSystems",5),
("00005","ComputerNetwork",4);
"""

course_select="""
insert into sc
(Sno,Cno,Grade)
values
(10002,"00003",86),
(10001,"00002",90),
(10002,"00004",70),
(10003,"00001",85),
(10004,"00002",77),
(10005,"00003",88),
(10001,"00005",91),
(10002,"00002",79),
(10003,"00002",83),
(10004,"00003",67);
"""

cursor.execute(stu_data)
cursor.execute(course_data)
cursor.execute(course_select)
driver.commit()

select_stu="""
select * from student st
right join sc on st.Sno=sc.Sno
right join course on course.Cno=sc.Cno
where st.Sno=10002
order by st.Sno asc
"""

cursor.execute(select_stu)

print("Student ID 10002")
print('\n'.join(str(e) for e in cursor.fetchall()))

select_score85="""
select * from student st
right join sc on st.Sno=sc.Sno
right join course on course.Cno=sc.Cno
where sc.grade>85
order by st.Sno asc
"""

cursor.execute(select_score85)
print("Score>85")
print('\n'.join(str(e) for e in cursor.fetchall()))

change_credit="""
update course
set Credit=5
where Cno="00001";
"""
opt="select * from course;"

cursor.execute(change_credit)
driver.commit()
cursor.execute(opt)
print("change_credit")
print('\n'.join(str(e) for e in cursor.fetchall()))

add_grade="""
insert into sc values
("10005","00004",73)
"""
cursor.execute(add_grade)
driver.commit()
print("add score")
cursor.execute("Select * from sc")
print('\n'.join(str(e) for e in cursor.fetchall()))

remove_stu1="""
delete from student
where Sno=10003;
"""
cursor.execute(remove_stu1)
driver.commit()

remove_stu2="""
delete from sc
where Sno=10003;
"""

cursor.execute(remove_stu2)
driver.commit()

print("remove student")
cursor.execute("Select * from sc")
print('\n'.join(str(e) for e in cursor.fetchall()))