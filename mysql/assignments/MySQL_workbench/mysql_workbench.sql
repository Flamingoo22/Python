SELECT *
FROM names;

INSERT INTO names(name, created_at, updated_at)
VALUES
	('FAN',NOW(),NOW()),
    ('QIU',NOW(),NOW());
-- INSERT MULTIPLE USERS IN ONE STATEMENT
SELECT *
FROM names;

SELECT name, DATE_FORMAT(created_at, '%a %m/%e/%Y %T') AS user_created_at
FROM names;

DELETE from names
WHERE names.id=1;

UPDATE names
SET name='JONNY', created_at = NOW(), updated_at = NOW()
WHERE names.id=4;

INSERT INTO names(name, created_at, updated_at)
VALUES('Ron',NOW(),NOW())
