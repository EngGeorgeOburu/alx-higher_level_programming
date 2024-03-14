-- Lists all the cities of california that are in the database
SELECT cities.id, name FROM cities WHERE state_id = (
    SELECT id FROM WHERE name = 'California') ORDER BY cities.id ASC;
