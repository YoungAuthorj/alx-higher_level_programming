-- Import the database dump from hbtn_0d_tvshows to your MySQL server:
-- +download (same as 13-count_shows_by_genre.sql)
-- ===========================================================================
-- Write a script that uses the hbtn_0d_tvshows database to lists all genres of
-- +the show Dexter.
-- ===========================================================================
--  The tv_shows table contains only one record where title = Dexter (but the
--     	+id can be different)
--  Each record should display: tv_genres.name
--  Results must be sorted in ascending order by the genre name
--  You can use only one SELECT statement
--  The database name will be passed as an argument of the mysql command
SELECT g.`name`
  FROM `tv_genres` AS g
       INNER JOIN `tv_show_genres` AS s
       ON g.`id` = s.`genre_id`

       INNER JOIN `tv_shows` AS t
       ON t.`id` = s.`show_id`
       WHERE t.`title` = "Dexter"
 ORDER BY g.`name`;
