-- Create the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa)

-- Creates the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;
-- Creates the table states
CREATE TABLE IF NOT EXISTS states(
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	name VARCHAR(256) NOT NULL
	)
