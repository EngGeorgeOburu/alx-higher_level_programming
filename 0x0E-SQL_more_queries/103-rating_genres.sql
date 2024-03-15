-- List all gnres in the database hbtn_0d_tvshows_rate
SELECT tv_genres.name, SUM(rating.rating) AS rating_sum
FROM tv_genres
JOIN shows_genres ON tv_genres.id = shows_genres.genre_id
JOIN tv_shows ON tv_shows.id = shows_genres.show_id
JOIN ratings ON tv_shows.id = ratings.tv_show_id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;
