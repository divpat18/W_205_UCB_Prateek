SELECT s.provider_id,
       s.aggregate,
       h.hospital_name,
       h.state
FROM
  (SELECT provider_id,
          avg(score)AS AGGREGATE
   FROM score
   GROUP BY provider_id) s,
     hospital h
WHERE s.provider_id=h.provider_id
ORDER BY AGGREGATE DESC LIMIT 10;
