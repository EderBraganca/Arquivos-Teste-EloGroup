--Tem que ter:
--um modo de subdivisao de tabelas
--separar pelo ano
--order by desc, pro primeiro ser o maior valor

WITH CTE AS ( 
	SELECT year, consultant_name, sale_amount, branch, 
	ROW_NUMBER () OVER (PARTITION BY year ORDER BY sale_amount DESC) as row_number FROM sales )
	SELECT year, consultant_name FROM CTE WHERE row_number = 1;

