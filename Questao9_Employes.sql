--Tem q ser feito:
--order by salario
--partition by departament 
--count departament
--avarage salario baseado no dp

SELECT departament, name, last_name, salary,
RANK() OVER (PARTITION BY departament ORDER BY salary DESC) AS ranking,
COUNT(*) OVER (PARTITION BY departament) AS total_funcionarios, 
AVG(salary) OVER (PARTITION BY departament) AS salario_medio FROM empregados;