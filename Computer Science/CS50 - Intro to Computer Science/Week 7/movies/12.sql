SELECT a.*
FROM (
    SELECT movies.title
    FROM movies, stars, people
    WHERE movies.id = stars.movie_id AND 
        stars.person_id = people.id AND 
        people.name = 'Johnny Depp'
) a
JOIN (
    SELECT movies.title
    FROM movies, stars, people
    WHERE movies.id = stars.movie_id AND 
        stars.person_id = people.id AND 
        people.name = 'Helena Bonham Carter'
) b
ON a.title = b.title;