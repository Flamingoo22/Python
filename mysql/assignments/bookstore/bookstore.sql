
-- Query: Create 5 different users: Jane Amsden, Emily Dixon, Theodore Dostoevsky, William Shapiro, Lao Xiu
INSERT INTO users(first_name, last_name)
VALUES
	('Jane','Amsden'),
	('Emily','Dixon'),
	('Theodore','Dostoevsky'),
	('William','Shapiro'),
	('Lao','Xiu');


-- Query: Create 5 books with the following names: C Sharp, Java, Python, PHP, Ruby     
INSERT INTO books(title)
VALUES
   ('C Sharp'),
   ('Java'),
   ('Python'),
   ('PHP'),
   ('Ruby');


-- Query: Change the name of the C Sharp book to C#     
UPDATE books
SET books.title = 'C#'
WHERE books.id = 1;

-- Query: Change the first name of the 4th user to Bill
UPDATE users
SET first_name = 'Bill'
WHERE users.id = 4;

-- Query: Have the first user favorite the first 2 books
-- Query: Have the second user favorite the first 3 books
-- Query: Have the third user favorite the first 4 books

INSERT INTO fav_books(user_id, book_id)
VALUES
  (1,1),
  (1,2),
  (2,1),
  (2,2),
  (2,3),
  (2,4),
  (3,1),
  (3,2),
  (3,3),
  (3,4),
  (4,1),
  (4,2),
  (4,3),
  (4,4),
  (4,5);


-- Query: Have the fourth user favorite all the books
SELECT *
FROM users
JOIN fav_books
ON users.id = fav_books.user_id
JOIN books
ON fav_books.book_id = books.id
WHERE books.id = 3;

-- WITH first_fav3 AS
-- (
-- SELECT TOP 1 * 
-- FROM fav_books
-- WHERE fav_books.book_id = 3
-- )

-- Query: Remove the first user of the 3rd book's favorites
DELETE
FROM fav_books
WHERE book_id = 3 AND user_id = 2;

SELECT *
FROM fav_books;

-- Query: Have the 5th user favorite the 2nd book
INSERT INTO fav_books(user_id, book_id)
VALUES (5,2);

-- Find all the books that the 3rd user favorited
SELECT *
FROM books
JOIN fav_books
ON books.id = fav_books.book_id
JOIN users
ON fav_books.user_id = users.id
WHERE users.id = 3;

-- Query: Find all the users that favorited to the 5th book
SELECT *
FROM users
JOIN fav_books
ON users.id = fav_books.user_id
JOIN books
ON fav_books.book_id = books.id
WHERE books.id = 5;