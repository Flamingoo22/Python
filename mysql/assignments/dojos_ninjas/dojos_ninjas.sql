-- CREATE DOJOS
INSERT INTO dojos (name, created_at, updated_at)
VALUES 
	('A', NOW(), NOW()),
	('B', '2000-01-01 01:01:01', NOW()),
    ('C', '1988-02-21 13:00:00', NOW());
    
SELECT *
FROM dojos;

-- REMOVE DOJOS
DELETE FROM dojos WHERE id=1 or id=2 or id=3;

-- CREATE 3 NEW DOJOS
INSERT INTO dojos (name, created_at, updated_at)
VALUES 
	('PYTHON', NOW(), NOW()),
	('CODING', '2011-07-23 01:01:01', NOW()),
    ('PROGRAMMING', '2088-02-21 13:00:00', NOW());
    
    
-- INSERT 3 NINJAS FOR FIRST DOJO
INSERT INTO ninjas ( dojo_id, first_name, last_name, age, created_at, updated_at) 
VALUES 
	(4, 'PANCAKE', 'SYRUP', 21, NOW(), NOW()),
    (4, 'SNAKE', 'ROBERT', 20, NOW(), NOW()),
    (4, 'HOTDOG', 'KETUP', 12, NOW(), NOW());
    
    
    
-- INSERT 3 NINJAS FOR SECOND DOJO
INSERT INTO ninjas ( dojo_id, first_name, last_name, age, created_at, updated_at) 
VALUES 
	(5, 'MAPLE', 'DONUT', 21, NOW(), NOW()),
    (5, 'CHEESE', 'CAKE', 20, NOW(), NOW()),
    (5, 'CREAM', 'CAKE', 12, NOW(), NOW());
    
    
-- INSERT 3 NINJAS FOR 3RD DOJO
INSERT INTO ninjas ( dojo_id, first_name, last_name, age, created_at, updated_at) 
VALUES 
	(6, 'BUFFLO', 'WINGS', 21, NOW(), NOW()),
    (6, 'FRIED', 'CHICKEN', 20, NOW(), NOW()),
    (6, 'PATATO', 'BURRITO', 12, NOW(), NOW());
    
    
-- SELECT NINJAS IN FIRST DOJO
SELECT *
FROM NINJAS
WHERE dojo_id = 4;

-- SELECT NINJAS IN THIRD DOJO
SELECT *
FROM NINJAS
WHERE dojo_id = 6;

-- SELECT LAST NINJA'S DOJO
SELECT *
FROM dojos
JOIN ninjas
ON ninjas.dojo_id = dojos.id
WHERE ninjas.id = last_insert_id()