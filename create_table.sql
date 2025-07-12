use industry_db;

create table machines_tbl
(
machineID numeric,
 model varchar(26), 
 age numeric
);

create table failures_tbl 
(datetime varchar(26), 
machineID numeric,
failure varchar(26)
);

create table errors_tbl 
(datetime varchar(26), 
machineID numeric, 
errorID varchar(26)
);

create table maintainances_tbl 
(datetime varchar(26), 
machineID numeric,
comp varchar(26)
);

create table telemetry_tbl 
(datetime varchar(26), 
machineID numeric,
volt numeric, 
rotate numeric, 
pressure numeric, 
vibration numeric);

create table test_tbl
(machineID numeric, 
age numeric, 
volt numeric, 
rotate numeric, 
pressure numeric, 
vibration numeric, 
comp1_cnt numeric, 
comp2_cnt numeric, 
comp3_cnt numeric, 
comp4_cnt numeric, 
error1_cnt numeric, 
error2_cnt numeric, 
error3_cnt numeric, 
error4_cnt numeric, 
error5_cnt numeric, 
model_model1 numeric, 
model_model2 numeric,
model_model3 numeric, 
model_model4 numeric);

create table prediction_results
(machineID numeric, 
age numeric, 
volt numeric, 
rotate numeric, 
pressure numeric, 
vibration numeric, 
comp1_cnt numeric, 
comp2_cnt numeric, 
comp3_cnt numeric, 
comp4_cnt numeric, 
error1_cnt numeric, 
error2_cnt numeric, 
error3_cnt numeric, 
error4_cnt numeric, 
error5_cnt numeric, 
model_model1 numeric, 
model_model2 numeric,
model_model3 numeric, 
model_model4 numeric,
failure1_prob numeric,
failure2_prob numeric,
failure3_prob numeric,
failure4_prob numeric   
);