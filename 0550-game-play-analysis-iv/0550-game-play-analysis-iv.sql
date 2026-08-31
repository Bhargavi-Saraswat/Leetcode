# Write your MySQL query statement below
select round(count(a.player_id)/(select count(distinct player_id) from Activity),2) as fraction
from Activity a join Activity b
on a.player_id = b.player_id
and b.event_date = a.event_date + interval 1 day
where a.event_date = (
    select min(event_date)
    from Activity
    where player_id = a.player_id
);