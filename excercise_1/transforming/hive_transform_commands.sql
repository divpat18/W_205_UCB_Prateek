-- Creating hospital table from the hospital bank
CREATE TABLE hospital AS
SELECT provider_id,
       hospital_name,
       state
FROM hospital_bank;

--Creating procedure table from measure
CREATE TABLE procedure AS
SELECT measure_id,
       measure_name
FROM measure;


-- Creating score table from effective care and readmission
REATE TABLE score AS WITH q1 AS
  (SELECT provider_id,
          measureid AS measure_id,
          CASE measureid
              WHEN 'OP_22' THEN 100-cast(score AS float)
              ELSE cast(score AS float)
          END AS score
   FROM effective_care
   WHERE score <> 'Not Available'
     AND score <= 100
     AND measureid NOT IN('EDV',
                          'OP_21',
                          'OP_20',
                          'OP_18b',
                          'OP_3b',
                          'OP_1',
                          'ED_2b',
                          'ED_1b')),
             q2 AS
  (SELECT provider_id,
          measure_id,
          100-cast(score AS float) AS score
   FROM readmission
   WHERE score <> 'Not Available')
SELECT *
FROM q1
UNION ALL
SELECT *
FROM q2;

--Creating surveys table
CREATE TABLE survey AS
SELECT provider_id,
       cast(regexp_extract(overall_rating_achv,'[0-9]*',0) AS int) AS overall_rating_achv,
       cast(regexp_extract(overall_rating_impv,'[0-9]*',0) AS int) AS overall_rating_impv,
       cast(regexp_extract(overall_rating_dim,'[0-9]*',0) AS int) AS overall_rating_dim
FROM survey_responses;
