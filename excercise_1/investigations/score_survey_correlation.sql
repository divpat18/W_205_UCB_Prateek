SELECT corr(s.score,su.overall_rating_achv)AS achievement_corr,
       corr(s.score,su.overall_rating_impv) AS impv_corr,
       corr(s.score,su.overall_rating_dim) AS dimension_corr
FROM
  (SELECT provider_id,
          avg(score) AS score
   FROM score
   GROUP BY provider_id) s,
     survey su
WHERE s.provider_id=su.provider_id;
