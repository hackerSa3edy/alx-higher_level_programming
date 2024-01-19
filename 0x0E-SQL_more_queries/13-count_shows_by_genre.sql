-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT
	tvG.name AS genre,
	COUNT(tvSh.title) AS number_of_shows
    FROM
	tv_genres AS tvG
    INNER JOIN
	tv_show_genres
    ON
	tvG.id = tv_show_genres.genre_id
    INNER JOIN
	tv_shows AS tvSh
    ON
	tvSh.id = tv_show_genres.show_id
    GROUP BY tvG.name
    ORDER BY number_of_shows DESC;
