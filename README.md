# AcademiaAPI

## Descrição

Adaptação do projeto da DIO [digitalinnovationone/workout_api](https://github.com/digitalinnovationone/workout_api) para criar uma API de competição de crossfit chamada WorkoutAPI. Desenvolvida utilizando o framework FastAPI, esta API foi adaptada para incluir funcionalidades específicas e utiliza MySQL como banco de dados.

## Modelagem de Entidade e Relacionamento - MER

![MER](/mer.jpg "Modelagem de entidade e relacionamento")

## Stack da API

A API foi desenvolvida utilizando as seguintes tecnologias:

- `fastapi`
- `alembic`
- `SQLAlchemy`
- `pydantic`
- `MySQL`

## Execução da API
````bash
uvicorn app.main:app --reload
````

## Funcionalidades e Mudanças

### Funcionalidades Implementadas

1.  **CRUD de Atletas, Categorias e Centros de Treinamento:**
    
    -   Endpoints para criar, ler, atualizar e deletar atletas, categorias e centros de treinamento.
2.  **Query Parameters:**
    
    -   Endpoints para buscar atletas pelo nome e CPF.
3.  **Customização de Response:**
    
    -   Endpoint para obter detalhes completos de um atleta, incluindo o centro de treinamento e a categoria.
4.  **Manipulação de Exceções de Integridade:**
    
    -   Tratamento de exceção para garantir que não haja duplicidade de CPFs na tabela de atletas com mensagem customizada e status code 303.
5.  **Verificação de Existência de IDs:**
    
    -   Verificação se o `centro_treinamento_id` e `categoria_id` existem antes de atribuir um atleta a esses registros.
6.  **Modelagem SQL Limpa:**
    
    -   Estrutura SQL das tabelas organizada e documentada para fácil replicação.

### Alterações e Melhorias

-   Atualização de dependências e configurações para suportar o método `from_orm` nos modelos Pydantic.

##Estrutura das Tabelas SQL

```bash
-- Table structure for table `atleta`
DROP TABLE IF EXISTS `atleta`;
CREATE TABLE `atleta` (
  `pk_id` int NOT NULL AUTO_INCREMENT,
  `id` binary(16) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `cpf` varchar(11) NOT NULL,
  `idade` int NOT NULL,
  `peso` float(10,2) NOT NULL,
  `altura` float(10,2) NOT NULL,
  `sexo` varchar(1) NOT NULL,
  `centro_treinamento_id` int DEFAULT NULL,
  `categoria_id` int NOT NULL,
  PRIMARY KEY (`pk_id`),
  UNIQUE KEY `cpf` (`cpf`),
  KEY `centro_treinamento_id` (`centro_treinamento_id`),
  KEY `categoria_id` (`categoria_id`)
);

-- Table structure for table `categoria`
DROP TABLE IF EXISTS `categoria`;
CREATE TABLE `categoria` (
  `pk_id` int NOT NULL AUTO_INCREMENT,
  `id` binary(16) NOT NULL,
  `nome` varchar(10) NOT NULL,
  PRIMARY KEY (`pk_id`),
  UNIQUE KEY `nome` (`nome`)
);

-- Table structure for table `centro_treinamento`
DROP TABLE IF EXISTS `centro_treinamento`;
CREATE TABLE `centro_treinamento` (
  `pk_id` int NOT NULL AUTO_INCREMENT,
  `id` binary(16) NOT NULL,
  `nome` varchar(20) NOT NULL,
  `endereco` varchar(60) NOT NULL,
  `proprietario` varchar(30) NOT NULL,
  PRIMARY KEY (`pk_id`),
  UNIQUE KEY `nome` (`nome`)
);
```



