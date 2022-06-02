SELECT DISTINCT(people.name) AS kevins_costars
FROM stars 
JOIN people
ON stars.person_id = people.id
WHERE stars.movie_id IN (
    SELECT movies.id
    FROM movies, stars, people
    WHERE movies.id = stars.movie_id AND 
        stars.person_id = people.id AND 
        people.name = 'Kevin Bacon' AND 
        people.birth = 1958) AND 
    NOT people.name = 'Kevin Bacon'
ORDER BY kevins_costars ASC;