-- Q1: User activity past 30 days
select
    activity_date as 'day',
    count(distinct user_id) as 'active_users'
from Activity
where activity_date between date_sub('2019-07-27', interval 29 day) and '2019-07-27'
group by activity_date

-- Q2: Number of employees which report to the employee
select 
    m.employee_id, 
    m.name, 
    count(e.employee_id) as 'reports_count',
    round(avg(e.age)) as 'average_age'
from Employees m
join Employees e
on m.employee_id = e.reports_to
group by m.employee_id
order by m.employee_id

-- Q3: Monthly transactions
select 
    date_format(trans_date, '%Y-%m') as month,
    country,
    count(id) as 'trans_count',
    count(case when state = 'approved' then id end) as 'approved_count',
    sum(amount) as trans_total_amount,
    sum(case when state = 'approved' then amount else 0 end) as 'approved_total_amount'
from Transactions
group by month, country