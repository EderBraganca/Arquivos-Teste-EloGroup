--create table if not exists sales(
--	year INTEGER NOT NULL,
--	consultant_name VARCHAR(50),
--	branch VARCHAR(2),
--	sale_amount INTEGER
--);

--INSERT INTO sales(year, consultant_name, branch, sale_amount)
--VALUES  (2021, 'Giovanni', 'MG', 170000),
--		(2023, 'Pablo', 'SP', 80000),
--		(2022, 'Celia', 'SP', 95000),
--		(2022, 'Giovanni', 'DF', 15000),
--		(2021, 'Pablo', 'RJ', 950000),
--		(2022, 'Celia', 'MG', 250000),
--		(2023, 'Giovanni', 'RJ', 165000),
--		(2023, 'Pablo', 'RJ', 13000),
--		(2022, 'Celia', 'DF', 387000);

--WITH CTE AS ( 
	--SELECT year, consultant_name, sale_amount, branch, ROW_NUMBER () OVER (PARTITION BY year ORDER BY sale_amount DESC) as row_number FROM sales )SELECT year, consultant_name FROM CTE WHERE row_number = 1;

