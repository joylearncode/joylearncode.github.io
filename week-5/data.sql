SHOW databases;
CREATE database website;
USE website;
SHOW tables;
CREATE table member(
	id bigint primary KEY AUTO_INCREMENT,
    name varcharacter(255) NOT NULL,
    username varcharacter(255) NOT NULL,
    password varcharacter(255) NOT NULL,
    follower_count int unsigned NOT NULL DEFAULT 0,
    time datetime NOT NULL default CURRENT_TIMESTAMP
);
select * from member;
insert into member(name,username,password) values('First','test','test');
insert into member(name,username,password) values('Second','2ndusername','1234');
insert into member(name,username,password) values('Third','3rdusername','5678');
insert into member(name,username,password) values('Forth','4thusername','9101112');
insert into member(name,username,password) values('Fifth','5thusername','13141516');

select*from member ORDER BY time ASC;
select*from member order by time limit 1,3;
select*from member where username = 'test';
select*from member where username = 'test' and password='test';
update member SET name='test' where id=1;
update member SET name='test2' where username='test';
update member SET follower_count=100 where id=2;
update member SET follower_count=500 where id=3;
update member SET follower_count=250 where id=4;
update member SET follower_count=450 where id=5;

select count( * ) as 會員人數 from member;
select sum(follower_count) as 追蹤者數量總和 , avg(follower_count ) as 追蹤者數量平均 from member;

create table message(
 id bigint primary KEY AUTO_INCREMENT,
 member_id bigint not null,
 FOREIGN KEY (member_id) REFERENCES member (id),
 content varchar(255) not null,
 like_count int unsigned NOT NULL DEFAULT 0,
 time datetime NOT NULL default CURRENT_TIMESTAMP
);
select * from message;
insert into message(member_id,content,like_count) values (2, 'good day', 25);
insert into message(member_id,content,like_count) values (4, 'Im good', 45);
insert into message(member_id,content,like_count) values (3, 'keep going', 50);
insert into message(member_id,content,like_count) values (1, 'good start', 30);
insert into message(member_id,content,like_count) values (5, 'we help', 60);
insert into message(member_id,content,like_count) values (1, '2nd commit', 5);

select*from member inner join message on member.id=message.member_id;
select member.id,member.name,member.username,message.content,message.like_count 
from member inner join message on member.id=message.member_id;
select member.id,member.name,member.username,message.content,message.like_count 
from member inner join message on member.id=message.member_id where member.username='test';
select username,like_count from member inner join message on member.id=message.member_id;
select username,avg(like_count) total
from member inner join message on member.id=message.member_id
-- group by member.id
-- having member.username='test'
where member.username='test'

