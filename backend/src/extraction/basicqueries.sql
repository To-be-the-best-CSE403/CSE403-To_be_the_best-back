/*
Basic queries will consist of accessing a pokemon's type, ability, popular moves (moveset), and EVs/IVs. 
*/

-- accessing the type
/* 
There are two scenarios for this query. If we follow the format of how Pokemon Showdown stores data,
we must create a separate table that contains the types of each species of pokemon. In this case,
queries under this category assume that there are two tables: one consisting of the names of each 
species of pokemon and one contains the types of that species. The columns that the query is accessing 
are the species columns from both tables and the type column from the poketypes table.
*/
SELECT b.species, t.type
FROM pokebase b, poketypes t
WHERE b.species = t.species
GROUP BY b.species;

/* 
In the second scenario, we construct a database that includes the types of a species in the
same table. In this case, queries under this category assume that there is one table consisting 
of a pokemon and their most used ability. The columns that the query is accessing is the type column.
*/
SELECT b.species, b.type
FROM pokebase b
GROUP BY b.species;

-- accessing the ability
/* 
Queries under this category assume that there is one table consisting of a pokemon and
their most used ability. The columns that the query is accessing is the ability column.
*/
SELECT b.species, b.ability
FROM pokebase b
GROUP BY b.species;

-- accessing the moveset
/* 
Queries under this category assume that there is one table consisting of a pokemon and
their most used moveset. The columns that the query is accessing is the moveset column.
*/
SELECT b.species, b.moveset
FROM pokebase b
GROUP BY b.species;

-- accessing the EVs/IVs
/* 
Queries under this category assume that there is one table consisting of a pokemon and
both their EVs and IVs. The columns that the query are accessing is the EVs and IVs columns.
*/
SELECT b.species, b.evs, b.ivs
FROM pokebase b
GROUP BY b.species;