-- Bu skript eyni xala malik yazıların sayını hesablayır.
-- Nəticədə 'score' və həmin xalın sayı ('number' etiketi ilə) göstərilir.
-- Siyahı sayına görə (number) çoxdan aza doğru sıralanır.
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;