/*
Basic queries will consist of accessing a pokemon's type, ability, popular moves, and EVs/IVs. 
*/

-- accessing the type
/* Queries under this category assume that there are two tables: one consisting of the names
of each species of pokemon and one contains the types of that species.*/
SELECT types.species
FROM pokebase base, poketypes types
WHERE base.species = types.species
GROUP BY types.species;

-- accessing the ability
/* Queries under this category assume that there are two tables: one consisting of the names
of each species of pokemon and one contains the types of that species.*/

-- accessing the popular moves
/* Queries under this category assume that there are two tables: one consisting of the names
of each species of pokemon and one contains the types of that species.*/

-- accessing the EVs/IVs
/* Queries under this category assume that there are two tables: one consisting of the names
of each species of pokemon and one contains the types of that species.*/
