-- Bu skript 'first_table' adlı cədvəli yaradır.
-- Cədvəlin sütunları: id (tam ədəd) və name (256 simvola qədər mətn).
-- Əgər cədvəl artıq mövcuddursa, skript xəta vermir.
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);