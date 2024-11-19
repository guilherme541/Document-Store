# Projeto Document Store - FEI 

## Integrantes do Grupo
| Nome                             | RA            |
|---------------------------------|---------------|
| GUILHERME COUTO GOMES           | 22.122.035-3 |
| PEDRO HENRIQUE ALGODOAL PINTO   | 22.122.072-6 |
| SAMIR OLIVEIRA DA COSTA         | 22.122.030-4 |

##  Descrição
Este projeto consiste na conversão de um sistema universitário originalmente desenvolvido em PostgreSQL para MongoDB, demonstrando a implementação de um banco de dados do tipo Document Store. O sistema gerencia informações sobre alunos, professores, cursos, departamentos, disciplinas e TCCs.

##  Estrutura do Projeto
```
├── src/
│   ├── collections-structure.md   # Estrutura das Coleções 
│   ├── create-collections.js    # Criação das coleções no MongoDB
│   ├── main.py                 # Script de população dos dados
│   └── queries.js              # Queries MongoDB para relatórios
├── README.md
└── requirements.txt
```

##  Pré-requisitos
- MongoDB 
- Python
- pymongo
- Faker

##  Executando o Projeto

### 1. Criar um banco de dados no MongoDB

### 2. Criar as seguintes coleções no MongoDB
    1. `departamentos`
    2. `professores`
    3. `cursos`
    4. `alunos`
    5. `grupos_tcc`
### 3. Populando os Dados
```bash
python src/main.py #Alterar o banco de dados dentro do codigo
```



---
CC6240 - TÓPICOS AVANÇADOS DE BANCOS DE DADOS - Projeto 1 - Document Store 
