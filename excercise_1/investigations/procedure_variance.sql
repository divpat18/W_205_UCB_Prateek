SELECT s.measure_id,
       s.variance m.measure_name
FROM
  (SELECT measure_id,
          var_samp(score) AS variance
   FROM score
   GROUP BY measure_id) s,
     measure m
WHERE m.measure_id=s.measure_id
ORDER BY s.variance DESC LIMIT 10;
