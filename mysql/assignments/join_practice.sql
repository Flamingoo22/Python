-- SELECT *
-- FROM users
-- LEFT JOIN tweets
-- ON users.id = tweets.user_id
-- WHERE users.id = 1; 

-- SELECT tweets.tweet
-- FROM users
-- LEFT JOIN tweets
-- ON users.id = tweets.user_id
-- WHERE users.id = 1;

-- SELECT tweets.tweet AS kobe_tweets
-- FROM users
-- LEFT JOIN tweets
-- ON users.id = tweets.user_id
-- WHERE users.id = 1;

-- SELECT tweets.tweet, users.first_name, users.last_name
-- FROM users
-- LEFT JOIN faves
-- ON faves.user_id = users.id
-- LEFT JOIN tweets
-- ON faves.tweet_id = tweets.id
-- WHERE users.id = 2;

-- SELECT tweets.tweet, users.first_name, users.last_name
-- FROM users
-- LEFT JOIN faves
-- ON users.id = faves.user_id
-- LEFT JOIN tweets
-- ON faves.tweet_id = tweets.id
-- WHERE users.id = 2 or users.id = 1;

-- SELECT users.first_name AS 'followed' , user2.first_name AS 'followers'
-- FROM users
-- LEFT JOIN follows
-- ON users.id = follows.followed_id
-- LEFT JOIN users AS user2
-- ON user2.id = follows.follower_id 
-- WHERE users.id = 1;


-- SELECT users.first_name AS 'followed' , user2.first_name AS 'not followers'
-- FROM users
-- LEFT JOIN follows
-- ON users.id = follows.followed_id
-- LEFT JOIN users AS user2
-- ON user2.id <> follows.follower_id and user2.id <> 2 
-- WHERE users.id = 2;

-- SELECT *
-- FROM users
-- WHERE users.id NOT IN (
-- SELECT follower_id
-- FROM follows
-- WHERE followed_id = 2
-- ) AND users.id != 2;

SELECT users.first_name AS user, COUNT(users2.first_name) AS follower_count
FROM users
LEFT JOIN follows
ON users.id = follows.followed_id
LEFT JOIN users AS users2
ON users2.id = follows.follower_id
WHERE users.id = 1
GROUP BY users.id;


