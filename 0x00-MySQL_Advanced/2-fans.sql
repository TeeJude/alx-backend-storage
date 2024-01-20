-- SQL script that ranks country origins of bands, ordered by the
-- number of (non-unque) fans
SELECT origin, SUM(fans) as nb_fans from metals_bands
GROUP BY origin ORDER BY nu_fans DESC;
