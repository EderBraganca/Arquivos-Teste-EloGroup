--Tem que ter:
--Somatorio da receita
--ordenar pelo periodo


SELECT actual_revenue, 
SUM(actual_revenue) OVER (ORDER BY periodo ASC) AS cumulative_revenue, 
periodo FROM revenue;