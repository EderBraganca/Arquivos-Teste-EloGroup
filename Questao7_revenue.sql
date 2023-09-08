--create table if not exists revenue(
--	id_revenue INTEGER PRIMARY KEY,
--	actual_revenue INTEGER NOT NULL,
--	periodo DATE NOT NULL 
--);

--INSERT INTO revenue(id_revenue, actual_revenue, periodo)
--VALUES(1, 8748441, '2023-01-01'),
--      (2, 10487444, '2023-02-01'),
--		(3, 7481457, '2023-03-01'),
--		(4, 7497441, '2023-04-01'),
--		(5, 8697415, '2023-05-01'),
--		(6, 12497441, '2023-06-01'),

--select * from revenue;

--SELECT actual_revenue, SUM(actual_revenue) OVER (ORDER BY periodo ASC) AS cumulative_revenue, periodo FROM revenue;