# Integração do MySQL na Azure com Python e Power BI

## Índice
- [Integração do MySQL na Azure com Python e Power BI](#integração-do-mysql-na-azure-com-python-e-power-bi)
  - [Índice](#índice)
  - [Introdução](#introdução)
  - [Instância do MySQL na Azure](#instância-do-mysql-na-azure)
  - [Conectando ao MySQL na Azure com Python](#conectando-ao-mysql-na-azure-com-python)
  - [Integração com Power BI](#integração-com-power-bi)
  - [Transformação dos Dados](#transformação-dos-dados)
  - [Troubleshooting](#troubleshooting)
    - [Erros e Soluções](#erros-e-soluções)
  - [Conclusão](#conclusão)

## Introdução
Este documento apresenta um relatório de criação e manipulação de uma instância do MySQL na Azure, e integração dessa base de dados com Python e Power BI. 

## Instância do MySQL na Azure
1. **Instância criada na Azure**
   - Nome do Servidor: `desafio-bi-mysql`
   - Versão do MySQL: `8.0`
   - Administrador: `company`

<div align="center">
  <img src="/figure/figure_1_cria_instancia_mysql.png" alt="Instância mysql criada na Azure" width="1000" height="200"/>
</div>


## Conectando ao MySQL na Azure com Python
1. **Criação do Banco de Dados**
   - Utilização do script `cria_bd.py` para criar o banco de dados `azure_company` na instância `desafio-bi-mysql`.

   <div align="center">
   <img src="/figure/figure_2_mens_cria_bd.png" alt="Cria banco de dados pelo python" width="1000" height="100"/>
   </div>

   <div align="center">
   <img src="/figure/figure_3_consulta_servidor.png" alt="Consulta ao banco de dados pelo python" width="1000" height="150"/>
   </div>


2. **Criar, alterar, consultar e inserir dados nas Tabelas**
  Utilize o script `exec_comandos_sql.py` para criar, alterar, consultar e inserir Tabelas e dadaos no banco de dados.

    2.1 **Tabelas criadas conforme proposto**

   <div align="center">
   <img src="/figure/figure_4_cria_tabelas.png" alt="Consulta ao banco de dados pelo python" width="1000" height="200"/>
   </div>

    2.2 **Populando as Tabelas**

    - **Na tabela employee.**
   <div align="center">
   <img src="/figure/figure_5_insercao_employee.png" alt="inserção de dados na tabela employee" width="1000" height="200"/>
   </div>

    - **Na tabela dependent.**
   <div align="center">
   <img src="/figure/figure_6_insercao_dependent.png" alt="inserção de dados na tabela dependent" width="1000" height="200"/>
   </div>

    - **Na tabela edepartament.**
   <div align="center">
   <img src="/figure/figure_7_insercao_departament.png" alt="inserção de dados na tabela departament" width="1000" height="200"/>
   </div>

    - **Na tabela dep locations.**
   <div align="center">
   <img src="/figure/figure_8_insercao_deplocations.png" alt="inserção de dados na tabela deplocations" width="1000" height="200"/>
   </div>

    - **Na tabela project.**
   <div align="center">
   <img src="/figure/figure_9_insercao_project.png" alt="inserção de dados na tabela project" width="1000" height="200"/>
   </div>

    - **Na tabela work.**
   <div align="center">
   <img src="/figure/figure_9_insercao_work.png" alt="inserção de dados na tabela work" width="1000" height="250"/>
   </div>

## Integração com Power BI
A integração com o Power BI foi realizada com sucesso, permitindo a visualização e análise dos dados presentes na base.
   <div align="center">
   <img src="/figure/figure_15_int_dados.png" alt="inserção de dados na tabela work" width="400" height="300"/>
   </div>

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

   <div align="center">
   <img src="//figure/figure_11_employee_mng.png" alt="inserção de dados na tabela work" width="400" height="300"/>
   </div>

8.  **Mesclar nomes de departamento e localização e porque utilizar mesclar e não atribuir**
    - Resultado da mesclagem entre as tabelas depatarmento e local.
   <div align="center">
   <img src="/figure/figure_12_dpt_local.png" alt="Mesclar nomes de departamento e localização e porque utilizar mesclar e não atribuir" width="400" height="300"/>
   </div>

    - Porque utilizar mesclar e não atribuir?
        - União dos dados, a mesclagem permite combinar duas tabelas (departamentos e localizações) em uma nova tabela que contém informações de ambas. Isso é essencial para criar um modelo estrela, onde você precisa de dimensões bem definidas que podem ser relacionadas às suas tabelas de fatos;
      
        - Combinações únicas, ao mesclar as tabelas, você pode garantir que cada combinação de departamento e localização seja única. Isso ajuda na normalização dos dados e evita duplicatas. A mesclagem assegura que, para cada registro, você obtenha a combinação exata dos dados de ambas as tabelas;
      
        - Facilidade de Análise, com uma tabela que contém departamentos e suas localizações, você facilita a análise dos dados, permitindo que o modelo estrela seja mais eficiente. Isso facilita a criação de visualizações e relatórios no Power BI, já que as relações entre tabelas ficam mais claras;
      
        - Evita redundância, Se você apenas atribuísse os dados de uma tabela a outra, poderia acabar criando redundâncias ou complicações nos dados, especialmente se houvesse múltiplas localizações para um único departamento. A mesclagem garante que as relações sejam mantidas de forma mais limpa.

9.  **Agrupa os dados a fim de saber quantos colaboradores existem por gerente**
    - Resultado da operação utilizando Group By.
   <div align="center">
   <img src="/figure/figure_13_count_employees_mng.png" alt="Agrupa os dados a fim de saber quantos colaboradores existem por gerente" width="400" height="300"/>
   </div>


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


## Conclusão
Esse projeto teve como objetivo o tratamento de dados em uma instância `MySQL` na `Azure`, manipulação do banco de dados criado com `Python` e `DBeaver`, e integração com `Power BI` para a transformação dos dados necessários. Ao final, conseguimos não apenas otimizar a gestão das informações. A abordagem adotada permitiu uma maior eficiência nos processos de extração, transformação e carregamento (ETL), garantindo que os dados estejam sempre atualizados e acessíveis para tomadas de decisão mais ágeis e informadas. Assim, o projeto contribui significativamente para a melhoria dos processos de análise de dados na organização, permitindo um suporte mais robusto às estratégias de negócios.

