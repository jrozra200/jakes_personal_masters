SELECT DISTINCT(movies.title) AS name
FROM movies, stars, people, ratings
WHERE movies.id = stars.movie_id AND 
    stars.person_id = people.id AND 
    movies.id = ratings.movie_id AND
    people.name = 'Chadwick Boseman'
ORDER BY ratings.rating DESC
LIMIT 5;