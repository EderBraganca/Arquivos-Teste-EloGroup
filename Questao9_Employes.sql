--CREATE TABLE if not exists empregados(
--	worker_id INTEGER PRIMARY KEY,
--	name VARCHAR(20),
--	last_name VARCHAR(20),
--	salary INTEGER,
--	departament VARCHAR(20)
--);

--INSERT INTO empregados(worker_id, name, last_name, salary, departament)
--VALUES  (1, 'Rener', 'Escobar', 26300, 'TI'),
--		(2, 'Marcio', 'Gather', 3500, 'RH'),
--		(3, 'Luana', 'Sier', 12000, 'Financeiro'),
--		(4, 'Fernanda', 'Luna', 5000, 'Financeiro'),
--		(5, 'Cristine', 'Paiva', 8800, 'Marketing'),
--		(6, 'Rafael', 'Costa', 16000, 'TI'),
--		(7, 'Pablo', 'Henrique', 9300, 'Administrador'),
--		(8, 'Jose', 'Maria', 7860, 'RH'),
--		(9, 'Ronalda', 'Batista', 15000, 'Marketing'),
--		(10, 'Tihago', 'Silva', 7500, 'TI');

--order by salario
--partition by departament 
--count departament
--avarage salario baseado no dp

SELECT departament, name, last_name, salary,
RANK() OVER (PARTITION BY departament ORDER BY salary DESC) AS ranking,
COUNT(*) OVER (PARTITION BY departament) AS total_funcionarios, 
AVG(salary) OVER (PARTITION BY departament) AS salario_medio FROM empregados;