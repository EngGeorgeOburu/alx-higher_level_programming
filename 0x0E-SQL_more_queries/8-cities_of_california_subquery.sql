-- Lists all the cities of california that are in the database
SELECT cities.id, name FROM cities
WHERE state_id = (
    SELCT ID FROM states
    WHERE name = "California")
ORDER BY id;
