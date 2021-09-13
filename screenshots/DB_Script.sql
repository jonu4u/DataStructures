--  Sequence by different groups example
-- Table: Failed
-- 
-- +--------------+---------+
-- | Column Name  | Type    |
-- +--------------+---------+
-- | fail_date    | date    |
-- +--------------+---------+
-- Primary key for this table is fail_date.
-- Failed table contains the days of failed tasks.
-- Table: Succeeded
-- 
-- +--------------+---------+
-- | Column Name  | Type    |
-- +--------------+---------+
-- | success_date | date    |
-- +--------------+---------+
-- Primary key for this table is success_date.
-- Succeeded table contains the days of succeeded tasks.
--  
-- 
-- A system is running one task every day. Every task is independent of the previous tasks. The tasks can fail or succeed.
-- 
-- Write an SQL query to generate a report of period_state for each continuous interval of days in the period from 2019-01-01 to 2019-12-31.
-- 
-- period_state is 'failed' if tasks in this interval failed or 'succeeded' if tasks in this interval succeeded. Interval of days are retrieved as start_date and end_date.
-- 
-- Order result by start_date.
-- 
-- The query result format is in the following example:
-- 
-- Failed table:
-- +-------------------+
-- | fail_date         |
-- +-------------------+
-- | 2018-12-28        |
-- | 2018-12-29        |
-- | 2019-01-04        |
-- | 2019-01-05        |
-- +-------------------+
-- 
-- Succeeded table:
-- +-------------------+
-- | success_date      |
-- +-------------------+
-- | 2018-12-30        |
-- | 2018-12-31        |
-- | 2019-01-01        |
-- | 2019-01-02        |
-- | 2019-01-03        |
-- | 2019-01-06        |
-- +-------------------+
-- 
-- 
-- Result table:
-- +--------------+--------------+--------------+
-- | period_state | start_date   | end_date     |
-- +--------------+--------------+--------------+
-- | succeeded    | 2019-01-01   | 2019-01-03   |
-- | failed       | 2019-01-04   | 2019-01-05   |
-- | succeeded    | 2019-01-06   | 2019-01-06   |
-- +--------------+--------------+--------------+
-- 
-- The report ignored the system state in 2018 as we care about the system in the period 2019-01-01 to 2019-12-31.
-- From 2019-01-01 to 2019-01-03 all tasks succeeded and the system state was "succeeded".
-- From 2019-01-04 to 2019-01-05 all tasks failed and system state was "failed".
-- From 2019-01-06 to 2019-01-06 all tasks succeeded and system state was "succeeded".


with combined_data as (
select success_date dt , 'succeeded' as colType from Succeeded
union 
select fail_date dt , 'failed' as colType from Failed
),
finaldata as (
select *,ROW_NUMBER() over (order by dt) as seq1,
ROW_NUMBER() over (partition by colType order by dt) as seq2 from combined_data
where dt>='2019-01-01' and dt<='2019-12-31'
),
resultdata as (
select dt,(seq1-seq2) as diffrow ,colType from finaldata
)
select  colType as period_state, min(dt) as start_date,max(dt) as end_date from resultdata
group by colType,diffrow order by start_date


-- Nth Highest using correlated subquery
select distinct e1.salary from employee e1 where N-1=(select count(distinct e2.salary) from employee e2 where e2.salary>e1.salary)


