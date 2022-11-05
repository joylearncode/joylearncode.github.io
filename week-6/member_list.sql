CREATE DATABASE IF NOT EXISTS database_6;
USE database_6;

CREATE TABLE IF NOT EXISTS accounts (
	id bigint primary KEY AUTO_INCREMENT,
    -- 姓名 
    name varcharacter(255) NOT NULL,
    -- 帳號 
  	username varcharacter(255) NOT NULL,
    -- 密碼 
    password varcharacter(255) NOT NULL
) ;
INSERT INTO accounts (id, name, username, password) VALUES (1, 'test_name','test', 'test');
select*from accounts;

