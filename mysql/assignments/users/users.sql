INSERT INTO users (first_name, last_name, email, created_at, updated_at)
VALUES
	('JON','JONN', 'fake1@email.com', NOW(), NOW()),
    ('FAN','QIU', 'fake1@email.com', '1973-04-25 03:22:19', NOW()),
    ('RON','NERD', 'fake1@email.com', NOW(), NOW());

-- RETRIEVE ALL USER DATA    
SELECT *
FROM users;

-- RETRIEVE FIRST USER USING EMAIL
UPDATE users
SET email = 'fake2@email.com'
WHERE id = 5;
UPDATE users
SET email = 'fake3@email.com'
WHERE id = 6;
SELECT *
FROM users
WHERE users.email = "fake1@email.com";
-- RETRIEVE LAST USER USING ID
SELECT *
FROM users
WHERE users.id = 6;

-- CHANGE THE USER WITH ID=3 SO LAST NAME IS PANCAKES
UPDATE users
SET users.last_name = 'PANCAKES'
WHERE users.id = 6;

-- DELETE USER ID=2 FROM DATABASE
DELETE FROM users WHERE users.id = 5;

-- RETREIVE ALL USER DATA IN ORDER OF FIRST NAME
SELECT *
FROM users
ORDER BY users.first_name;

SELECT *
FROM users
ORDER BY users.first_name DESC
