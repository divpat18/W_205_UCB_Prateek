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
CREATE TABLE score AS WITH q1 AS
  (SELECT provider_id,
          measureid AS measure_id,
          CASE measureid
              WHEN 'OP_22' THEN 100-cast(score AS float)
              ELSE cast(score AS float)
          END
   FROM effective_care
   WHERE score <> 'Not Available'
     AND measureid<>'EDV'),
             q2 AS
  (SELECT provider_id,
          measure_id,
          100-cast(score AS float)
   FROM readmission
   WHERE score <> 'Not Available')
SELECT *
FROM q1
UNION ALL
SELECT *
FROM q2;


--Creating surveys table
CREATE TABLE surveys AS
SELECT *
FROM survey_responses;

