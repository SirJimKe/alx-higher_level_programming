-- Get the genre ID for Comedy
-- List shows without the genre Comedy
SELECT id FROM tv_genres WHERE name = 'Comedy';

SELECT tv_shows.title FROM tv_shows
WHERE id NOT IN (SELECT show_id FROM tv_show_genres WHERE genre_id = (SELECT id FROM tv_genres WHERE name = 'Comedy'))
ORDER BY tv_shows.title ASC;
