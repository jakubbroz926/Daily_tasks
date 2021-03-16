SELECT c.country,
case when WEEKDAY(cbd.`date`) < 5 then 0 else 1 end as weekday,
QUARTER(cbd.`date`)-1 as period
from countries c 
join covid19_basic_differences cbd on c.country  = cbd.country
;
#èasové promìnné jsou vytvoøeny
#nyní poèasí a poté tabulka ekonomická