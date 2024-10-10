# Integração do MySQL na Azure com Python e Power BI

## Índice
- [Integração do MySQL na Azure com Python e Power BI](#integração-do-mysql-na-azure-com-python-e-power-bi)
  - [Índice](#índice)
  - [Introdução](#introdução)
  - [Criando uma Instância do MySQL na Azure](#criando-uma-instância-do-mysql-na-azure)
  - [Conectando ao MySQL na Azure com Python](#conectando-ao-mysql-na-azure-com-python)
  - [Integração com Power BI](#integração-com-power-bi)
  - [Transformação dos Dados](#transformação-dos-dados)
  - [Troubleshooting](#troubleshooting)
    - [Erros e Soluções](#erros-e-soluções)

## Introdução
Este documento apresenta um relatório de criação e manipulação de uma instância do MySQL na Azure, e integração dessa base de dados com Python e Power BI. 

## Criando uma Instância do MySQL na Azure
1. **Instância na Azure**
   - Nome do Servidor: `desafio-bi-mysql`
   - Versão do MySQL: `8.0`
   - Administrador: `company`

![Instância mysql criada na Azure](/figure/figure_1_cria_instancia_mysql.png)


## Conectando ao MySQL na Azure com Python
1. **Criação do Banco de Dados**
   - Utilize o script `cria_bd.py` para criar o banco de dados `azure_company`.

    ![Cria banco de dados pelo python](/figure/figure_2_mens_cria_bd.png)

    ![Consulta ao banco de dados pelo python](/figure/figure_3_consulta_servidor.png)


2. **Criar, alterar, consultar e inserir dados nas Tabelas**
  Utilize o script `exec_comandos_sql.py` para criar, alterar, consultar e inserir Tabelas e dadaos no banco de dados.

    **Tabelas criadas conforme proposto**

    ![Consulta ao banco de dados pelo python](/figure/figure_4_cria_tabelas.png)

    **Inserções nas Tabelas**

    - Na tabela employee.
    ![inserção de dados na tabela employee](/figure/figure_5_insercao_employee.png)

    - Na tabela dependent.
    ![inserção de dados na tabela dependent](/figure/figure_6_insercao_dependent.png)

    - Na tabela edepartament.
    ![inserção de dados na tabela departament](/figure/figure_7_insercao_departament.png)

    - Na tabela dep locations.
    ![inserção de dados na tabela deplocations](/figure/figure_8_insercao_deplocations.png)

    - Na tabela project.
    ![inserção de dados na tabela project](/figure/figure_9_insercao_project.png)

    - Na tabela work.
    ![inserção de dados na tabela work](/figure/figure_9_insercao_work.png)

## Integração com Power BI
- A integração com o Power BI foi realizada com sucesso, permitindo a visualização e análise dos dados presentes na base.

## Transformação dos Dados
1. **Verificação de Cabeçalhos e Tipos de Dados**
   - Foi assegurado que os cabeçalhos e tipos de dados estão corretos.

2. **Modificação de Valores Monetários**
   - A coluna `Salary` na tabela `employee` foi alterada para o tipo `double` para maior precisão.

3. **Análise de Valores Nulos e Verificação de Gerentes**
   - Identificado que o James estava sem `Super_ssn`, identificado que era gerente. Foi-lhe atribuido seu `Ssn` a `Super_ssn`.

4. **Verificação de Departamentos**
   - Todos os departamentos possuem gerentes; nenhuma ação adicional é necessária.

5. **Verificação de Horas dos Projetos**
   - O número de horas dos projetos foi verificado e está correto.

6. **Separação de Colunas Complexas**
   - Não foram encontradas colunas complexas que necessitem de separação.

<!-- Este é um comentário 
7. **Mesclar consultas employee e departament**
   - À fazer.
-->
7. **Junção dos colaboradores e respectivos gerentes**
   - Resultado da mesclagem entre as tabelas depatarmento e employee.
    ![Junção dos colaboradores e respectivos gerentes](/figure/figure_11_employee_mng.png)

8.  **Mesclar nomes de departamento e localização e porque utilizar mesclar e não atribuir**
    - Resultado da mesclagem entre as tabelas depatarmento e local.

        ![Junção dos colaboradores e respectivos gerentes](/figure/figure_12_dpt_local.png)

    - Porque utilizar mesclar e não atribuir?
        - União dos dados, a mesclagem permite combinar duas tabelas (departamentos e localizações) em uma nova tabela que contém informações de ambas. Isso é essencial para criar um modelo estrela, onde você precisa de dimensões bem definidas que podem ser relacionadas às suas tabelas de fatos;
      
        - Combinações únicas, ao mesclar as tabelas, você pode garantir que cada combinação de departamento e localização seja única. Isso ajuda na normalização dos dados e evita duplicatas. A mesclagem assegura que, para cada registro, você obtenha a combinação exata dos dados de ambas as tabelas;
      
        - Facilidade de Análise, com uma tabela que contém departamentos e suas localizações, você facilita a análise dos dados, permitindo que o modelo estrela seja mais eficiente. Isso facilita a criação de visualizações e relatórios no Power BI, já que as relações entre tabelas ficam mais claras;
      
        - Evita redundância, Se você apenas atribuísse os dados de uma tabela a outra, poderia acabar criando redundâncias ou complicações nos dados, especialmente se houvesse múltiplas localizações para um único departamento. A mesclagem garante que as relações sejam mantidas de forma mais limpa.

9.  **Agrupa os dados a fim de saber quantos colaboradores existem por gerente**
    - Resultado da operação utilizando Group By.
        ![Agrupa os dados a fim de saber quantos colaboradores existem por gerente](/figure/figure_13_count_employees_mng.png)


## Troubleshooting
### Erros e Soluções
1. **1826 (HY000): Duplicate foreign key constraint name 'fk_employee'**
   - Verifique a existência da foreign key com:
     ```sql
     SHOW CREATE TABLE employee;
     ```

2. **1091 (42000): Can't DROP 'departament_ibfk_1'; check that column/key exists**
   - A chave não foi encontrada para remoção. Verifique com:
     ```sql
     SHOW CREATE TABLE departament;
     ```

3. **1091 (42000): Can't DROP 'fk_dept_locations'; check that column/key exists**
   - A chave não foi encontrada para remoção. Verifique com:
     ```sql
     SHOW CREATE TABLE fk_dept_locations;
     ```

4. **1826 (HY000): Duplicate foreign key constraint name 'fk_dept_locations'**
   - Verifique a existência da foreign key com:
     ```sql
     SHOW CREATE TABLE dept_locations;
     ```

5. **1452 (23000): Cannot add or update a child row**
   - O erro foi causado por uma violação de chave estrangeira. A coluna `Super_ssn` na tabela `employee` deve referenciar corretamente a coluna `Ssn`. Realize a correção nos dados e tente novamente.

