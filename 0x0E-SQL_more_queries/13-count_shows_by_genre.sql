-- Lists all genres contained in hbtn_0d_ and the number of shows linkedto each
SELECT name AS genre, COUNT(*) AS number_of_shows FROM tv_genres
JOIN tv_show_genre ON id=tv_show_genres.genre_id
GROUP BY number_of_shows DESC;
