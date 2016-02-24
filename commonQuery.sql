select * from stock where security='fln';
select sum(`net_proceeds`) from stock
-- -- where security = 'fln'
;
select security, sum(`net_proceeds`) from stock
-- where security='fln'
group by security;

-- total profit
select  sum(`net_proceeds`) as  total_profit from stock;