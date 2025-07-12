select machines_tbl.machineID,

machines_tbl.age,  machines_tbl.datetime,

maintainances_tbl.comp

from machines_tbl

left join maintainances_tbl

on machines_tbl.machineID=maintainances_tbl.machineID

and maintainances_tbl.datetime = machines_tbl.datetime;

 

select t.*, m.comp from telemetry_tbl as t

left join maintainance_tbl as m

on t.machineID = m.machineID and t.datetime = m.datetime;

 

select datetime, machineID, volt, rotate, pressure, vibration,

case when comp = 'comp1' then 1 else 0 end as maint_comp1_count,

case when comp = 'comp2' then 1 else 0 end as maint_comp2_count,

case when comp = 'comp3' then 1 else 0 end as maint_comp3_count,

case when comp = 'comp4' then 1 else 0 end as maint_comp4_count

from maintainance_tbl;

 

select t.*, case when f.failure= "comp1" then 1 else 0 end as fail_comp1,

case when f.failure= "comp2" then 1 else 0 end as fail_comp2,

case when f.failure= "comp3" then 1 else 0 end as fail_comp3,

case when f.failure= "comp4" then 1 else 0 end as fail_comp4

from t

left join f

on t.datetime=f.datetime;

 

select t.*, case when e.errorID= "error1" then 1 else 0 end as error1,

case when e.errorID= "error2" then 1 else 0 end as error2,

case when e.errorID= "error3" then 1 else 0 end as error3,

case when e.errorID= "error4" then 1 else 0 end as error4

from t

left join f

on t.datetime=f.datetime;

 

select machineID, model, age, volt, rotate, pressure, vibration,

sum(maint_comp1_count) over(partition by machineID order by datetime) as comp1_cnt,

sum(maint_comp2_count) over(partition by machineID order by datetime) as comp2_cnt,

sum(maint_comp3_count) over(partition by machineID order by datetime) as comp3_cnt,

sum(maint_comp4_count) over(partition by machineID order by datetime) as comp4_cnt,

sum(error1) over(partition by machineID order by datetime) as error1_cnt,

sum(error2) over(partition by machineID order by datetime) as error2_cnt,

sum(error3) over(partition by machineID order by datetime) as error3_cnt,

sum(error4) over(partition by machineID order by datetime) as error4_cnt

from t;