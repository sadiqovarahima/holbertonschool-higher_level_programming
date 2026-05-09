-- Bu skript 'second_table' cədvəlindəki yazıları siyahılayır.
-- Adı (name) olmayan (NULL olan) sətirlər siyahıya alınmır.
-- Nəticələr score və name ardıcıllığı ilə, score-a görə azalan sıra ilə düzülür.
SELECT score, name 
FROM second_table 
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;