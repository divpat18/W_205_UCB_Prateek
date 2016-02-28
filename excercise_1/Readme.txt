Before running any of the sql file please ensure the following directories exist in the HDFS:
/user/w205/hospital_compare/measures
/user/w205/hospital_compare/hospitals
/user/w205/hospital_compare/readmissions
//user/w205/hospital_compare/effective_care
/user/w205/hospital_compare/survey_responses

This can be done by
hdfs dfs -put /data/medical/modified/effective_care.csv /user/w205/hospital_compare
hdfs dfs -put /data/medical/modified/effective_care.csv /user/w205/hospital_compare/effective_care
hdfs dfs -put /data/medical/modified/hospitals.csv /user/w205/hospital_compare/hospitals
hdfs dfs -put /data/medical/modified/readmissions.csv /user/w205/hospital_compare/readmissions
hdfs dfs -put /data/medical/modified/measures.csv /user/w205/hospital_compare/measures
hdfs dfs -put /data/medical/modified/surveys_responses.csv /user/w205/hospital_compare/survey_responses

Please place the following files in these directories:
measures.csv in /user/w205/hospital_compare/measures
hospitals.csv in /user/w205/hospital_compare/hospitals
readmissions.csv in /user/w205/hospital_compare/readmissions
effective_care.csv in /user/w205/hospital_compare/effective_care
surveys_responses.csv in /user/w205/hospital_compare/survey_responses

Running the load_data_lake.sh from the loading and modeling directory should load the CSV filed into Hive. (Please ensure the first line has been removed from the files)
Running the hive_base_ddl.sql should create tables out of them. These should be measure, hospital_bank, effective_care, readmission and survey_responses.
Running the hive transform commands should run the sql that will generate tables matching out ERD.

Now all of the Investigation files can be run to answer the questions.
