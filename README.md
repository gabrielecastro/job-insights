## Projeto Job Insights

### Contexto

Nesse projeto é implementada análises a partir de um conjunto de dados sobre empregos. Essas implementações são incorporadas a um aplicativo Web desenvolvido em Flask.

### Habilidades trabalhadas

* Manipulação de arquivos
* Tratamento de exceções
* Criação de funções
* Testes com Pytest

### Tecnologias usadas

>Python e Pytest

### Instalação do projeto

1. Clonar o link do repositório ```git clone git@github.com:gabrielecastro/job-insights.git``` 
2. Entrar na pasta do projeto: ```cd job-insights```
3. Criar o ambiente virtual: ```python3 -m venv .venv```
4. Ativar o ambiente virtual: ```source .venv/bin/activate```
5. Instalar as dependências no ambiente virtual: ```python3 -m pip install -r dev-requirements.txt```

### Testes

>Para executar os testes o ambiente virtual deve estar ativado

Para executar todos os testes: ```python3 -m pytest```  


Para executar apenas um arquivo de teste: ```python3 -m pytest tests/nomedoarquivo.py```      


<details>
<summary><strong>Requisitos do projeto</strong></summary><br />

#### 1 - Implementa a função read

>src/ jobs.py  


Esta função é responsável por abrir o arquivo CSV e retornar os dados no formato de uma lista de dicionários.

* A função recebe um path como parâmento (uma string com o caminho para o arquivo).
* A função abre o arquivo e lê seu conteúdo (tratando o arquivo como CSV).
* A função retorna uma lista de dicionários, onde as chaves são os cabeçalhos de cada coluna e os valores correspondem a cada linha.


#### 2 - Implementa a função get_unique_job_types

>src/ insights.py    


Esta função é responsável identificar quais tipos de empregos existem.

* A função recebe o path do arquivo csv como parâmetro.
* A função invoca a função jobs.read com o path recebido para obter os dados.
* A função retornaa uma lista de valores únicos presentes na coluna job_type.  

#### 3 - Implementa a função get_unique_industries

>src/ insights.py    


Esta função é responsável identificar quais indústrias estão representadas nesse conjunto de dados.

* A função recebe o path do arquivo csv como parâmetro.
* A função invoca a função jobs.read com o path recebido para obter os dados.
* A função desconsidera valores vazios.
* A função retorna uma lista de valores únicos presentes na coluna industry.  

#### 4 - Implementa a função get_max_salary

>src/ insights.py    


Esta função é responsável identificar qual maior valor de todas as faixas salariais.

* A função recebe o path do arquivo csv como parâmetro.
* A função invoca a função jobs.read com o path recebido para obter os dados.
* A função desconsidera valores vazios.
* A função retorna um valor inteiro com o maior salário presente na coluna max_salary.  

#### 5 - Implementa a função get_min_salary

>src/ insights.py    


Esta função é responsável identificar qual menor valor de todas as faixas salariais.

* A função recebe o path do arquivo csv como parâmetro.
* A função invoca a função jobs.read com o path recebido para obter os dados.
* A função desconsidera valores vazios.
* A função retorna um valor inteiro com o menor salário presente na coluna min_salary.  

#### 6 - Implementa a função filter_by_job_type

>src/ insights.py    


Esta função é responsável por filtrar os empregos por tipo de emprego.

* A função recebe uma lista de dicionários jobs como primeiro parâmetro.
* A função recebe uma string job_type como segundo parâmetro.
* A função retorna uma lista com todos os empregos onde a coluna job_type corresponde ao parâmetro job_type.  

#### 7 - Implementa a função filter_by_industry

>src/ insights.py    


Esta função é responsável por filtrar os empregos por indústria.

* A função recebe uma lista de dicionários jobs como primeiro parâmetro.
* A função recebe uma string industry como segundo parâmetro.
* A função retorna uma lista de dicionários com todos os empregos onde a coluna industry corresponde ao parâmetro industry.  


#### 8 - Implementa a função matches_salary_range

>src/ insights.py    


Esta função é responsável por conferir que o salário procurado está dentro da faixa salarial daquele emprego e se faz sentido, ou seja, se o valor mínimo é menor que o valor máximo.

* A função recebe um dicionário job como primeiro parâmetro, com as chaves min_salary e max_salary.
* A função recebe um inteiro salary como segundo parâmetro.
* A função lança um erro ValueError nos seguintes casos:  
  * alguma das chaves min_salary ou max_salary estão ausentes no dicionário;  
  * alguma das chaves min_salary ou max_salary tem valores não-numéricos;  
  * o valor de min_salary é maior que o valor de max_salary;  
  * o parâmetro salary tem valores não numéricos;  
*A função retorna True se o salário procurado está dentro da faixa salarial ou False se não está.  

#### 9 - Implementa a função filter_by_salary_range

>src/ insights.py    


Esta função é responsável por implementar o filtro.

* A função recebe uma lista de dicionários jobs como primeiro parâmetro.
* A função recebe um inteiro salary como segundo parâmetro.
* A função ignora os empregos com valores inválidos para min_salary ou max_salary. 
* A função retorna uma lista com todos os empregos onde o salário salary está entre os valores da coluna min_salary e max_salary.  

#### 10 - Implementa um teste para a função count_ocurrences

>tests/counter/test_counter.py  

O teste é responsável por garantir que a função garanta as especificações.  

* O teste chama a função count_ocurrences passando dois parâmetros:  
  * path uma string com o caminho do arquivo (src/jobs.csv);
  * word uma string com a palavra a ser contabilizada.
* O teste garante que a função retorna corretamente a quantidade de ocorrências da palavra solicitada.
* A contagem de palavras é case insentitive, ou seja, não diferencia letras maiúsculas de minúsculas. 

#### 11 - Implementa um teste para a função read_brazilian_file

>tests/brazilian/test_brazilian_jobs.py 

O teste é responsável por garantir que a função garanta as especificações.  

* O teste chama a função read_brazilian_file que recebe um parâmetro:  
  * path que é uma string com o caminho do arquivo csv em português (tests/mocks/brazilians_jobs.csv);
* Retorna uma lista de dicionários com as chaves em inglês.   

#### 12 - Implementa um teste para a sort_by

>tests/sorting/test_sorting.py

O teste é responsável por garantir que a função garanta as especificações.  

* A função sort_by recebe dois parâmetros: 
  * jobs uma lista de dicionários com os detalhes de cada emprego;
  * criteria uma string com uma chave para ser usada como critério de ordenação.
* O parâmetro criteria deve ter um destes valores: min_salary, max_salary, date_posted  
* A ordenação para min_salary deve ser crescente, mas para max_salary ou date_posted devem ser decrescentes.  
* Os empregos que não apresentarem um valor válido no campo escolhido para ordenação devem aparecer no final da lista.  

#### 13 - Implementa a página de um job

>src/routes_and_views.py  

Implementa a função job dentro do arquivo routes_and_views.py.  

* A função é decorada com a rota /job/<index>.  
* A função recebe um parâmetro index.  
* A função chama a read para ter uma lista com todos os jobs.  
* A função chama a get_job, declarada no arquivo src/more_insights.py, para selecionar um job específico pelo index.  
* A função renderiza o template job.jinja2, passando um parâmetro job contendo o job retornado pela get_job.
</details>    
 
 
 <details>
<summary><strong>Observações</strong></summary><br />  

 * Todos os arquivos que foram citados nos requisitos do projeto foram desenvolvidos por mim, o restante foram desenvolvidos pela Trybe.
</details>
