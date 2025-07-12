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