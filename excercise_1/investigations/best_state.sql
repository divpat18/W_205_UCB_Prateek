SELECT avg(s.score_agg) AS aggregate,
       h.state
FROM
  (SELECT provider_id,
          avg(score)AS score_agg
   FROM score
   GROUP BY provider_id) s,
     hospital h
WHERE s.provider_id=h.provider_id
GROUP BY h.state
ORDER BY aggregate DESC LIMIT 10;
