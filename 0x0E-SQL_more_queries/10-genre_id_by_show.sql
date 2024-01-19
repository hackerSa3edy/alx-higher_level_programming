-- Lists all shows contanied in hbtn_0d_tvshows
SELECT
	TvSh.title AS title,
	TvShG.genre_id AS genre_id
    FROM
	tv_shows AS TvSh
    INNER JOIN
	tv_show_genres AS TvShG
    ON
	TvShG.show_id = TvSh.id
    ORDER BY TvSh.title, TvShG.genre_id;

