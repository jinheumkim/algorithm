select animal_type, count(*) as count
from animal_ins
where animal_type = 'cat' or animal_type = 'dog'
group by animal_type
order by animal_type