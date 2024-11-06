# Alunos
```
GUILHERME COUTO GOMES RA: 22.122.035-3
PEDRO HENRIQUE ALGODOAL PINTO RA: 22.122.035-3
SAMIR OLIVEIRA DA COSTA RA: 22.122.035-3
```

# Estrutura das Coleções MongoDB

## 1. Departamentos
```javascript
{
    "_id": Number,
    "nome": String,
    "coordenador": {
        "_id": Number,
        "nome": String,
        "email": String
    }
}
```

## 2. Professores
```javascript
{
    "_id": Number,
    "nome": String,
    "email": String,
    "departamento": {
        "_id": Number,
        "nome": String
    },
    "historico_disciplinas": [
        {
            "disciplina": {
                "_id": Number,
                "nome": String
            },
            "ano": Number,
            "semestre": Number
        }
    ]
}
```

## 3. Cursos
```javascript
{
    "_id": Number,
    "nome": String,
    "departamento": {
        "_id": Number,
        "nome": String
    },
    "matriz_curricular": [
        {
            "disciplina": {
                "_id": Number,
                "nome": String
            },
            "semestre_recomendado": Number
        }
    ]
}
```

## 4. Alunos
```javascript
{
    "_id": Number,  // RA
    "nome": String,
    "data_nascimento": Date,
    "email": String,
    "curso": {
        "_id": Number,
        "nome": String
    },
    "historico": [
        {
            "disciplina": {
                "_id": Number,
                "nome": String
            },
            "professor": {
                "_id": Number,
                "nome": String
            },
            "ano": Number,
            "semestre": Number,
            "nota_final": Number
        }
    ]
}
```

## 5. Grupos TCC
```javascript
{
    "_id": Number,
    "tema": String,
    "orientador": {
        "_id": Number,
        "nome": String,
        "email": String
    },
    "membros": [
        {
            "_id": Number,  // RA
            "nome": String,
            "curso": {
                "_id": Number,
                "nome": String
            }
        }
    ]
}
```
# Queries MongoDB

## 1. Histórico escolar de um aluno
```javascript
// Substitua <RA_DO_ALUNO> pelo RA desejado
db.alunos.aggregate([
  { $match: { "_id": <RA_DO_ALUNO> } },
  { $unwind: "$historico" },
  { $project: {
    _id: 0,
    disciplina: "$historico.disciplina.nome",
    semestre: "$historico.semestre",
    ano: "$historico.ano",
    nota_final: "$historico.nota_final"
  }},
  { $sort: { "ano": 1, "semestre": 1 } }
])
```

## 2. Histórico de disciplinas ministradas por professor
```javascript
// Substitua <ID_DO_PROFESSOR> pelo ID desejado
db.alunos.aggregate([
  { $unwind: "$historico" },
  { $match: { "historico.professor._id": <ID_DO_PROFESSOR> } },
  { $group: {
    _id: {
      disciplina: "$historico.disciplina.nome",
      ano: "$historico.ano",
      semestre: "$historico.semestre"
    }
  }},
  { $project: {
    _id: 0,
    disciplina: "$_id.disciplina",
    ano: "$_id.ano",
    semestre: "$_id.semestre"
  }},
  { $sort: { "ano": 1, "semestre": 1 } }
])
```

## 3. Alunos formados em um determinado semestre
```javascript
// Substitua <ANO> e <SEMESTRE> pelos valores desejados
db.alunos.aggregate([
  {
    $lookup: {
      from: "cursos",
      localField: "curso._id",
      foreignField: "_id",
      as: "curso_completo"
    }
  },
  { $unwind: "$curso_completo" },
  {
    $match: {
      "historico": {
        $elemMatch: {
          "ano": <ANO>,
          "semestre": <SEMESTRE>
        }
      }
    }
  },
  {
    $project: {
      nome: 1,
      curso: "$curso.nome",
      disciplinas_aprovadas: {
        $size: {
          $filter: {
            input: "$historico",
            as: "h",
            cond: { $gte: ["$$h.nota_final", 5] }
          }
        }
      },
      total_disciplinas: { $size: "$curso_completo.matriz_curricular" }
    }
  },
  {
    $match: {
      $expr: { $gte: ["$disciplinas_aprovadas", "$total_disciplinas"] }
    }
  },
  {
    $project: {
      _id: 0,
      nome: 1,
      curso: 1
    }
  }
])
```

## 4. Coordenadores de departamento
```javascript
db.departamentos.find(
  {},
  {
    _id: 0,
    nome: 1,
    "coordenador.nome": 1
  }
)
```

## 5. Grupos de TCC com alunos e orientador
```javascript
db.grupos_tcc.aggregate([
  {
    $project: {
      _id: 0,
      tema: 1,
      "orientador.nome": 1,
      membros: {
        $map: {
          input: "$membros",
          as: "membro",
          in: {
            nome: "$$membro.nome",
            curso: "$$membro.curso.nome"
          }
        }
      }
    }
  }
])
```

### Exemplos de uso:

1. Para ver o histórico de um aluno específico:
```javascript
db.alunos.aggregate([
  { $match: { "_id": 123456789 } },  // Substitua pelo RA real
  { $unwind: "$historico" },
  { $project: {
    _id: 0,
    disciplina: "$historico.disciplina.nome",
    semestre: "$historico.semestre",
    ano: "$historico.ano",
    nota_final: "$historico.nota_final"
  }}
])
```

2. Para ver disciplinas de um professor:
```javascript
db.alunos.aggregate([
  { $unwind: "$historico" },
  { $match: { "historico.professor._id": 11111111111 } },  // Substitua pelo ID real
  { $group: {
    _id: {
      disciplina: "$historico.disciplina.nome",
      ano: "$historico.ano",
      semestre: "$historico.semestre"
    }
  }}
])
```

3. Para ver formados em 2023/2:
```javascript
db.alunos.aggregate([
  { $lookup: { from: "cursos", localField: "curso._id", foreignField: "_id", as: "curso_completo" } },
  { $match: { "historico": { $elemMatch: { "ano": 2023, "semestre": 2 } } } }
  // ... resto da query como mostrado acima
])
```

### Índices Recomendados:

Para melhor performance, recomendo criar os seguintes índices:

```javascript
// Índice para busca rápida de alunos
db.alunos.createIndex({ "_id": 1 })

// Índice para busca de professores
db.alunos.createIndex({ "historico.professor._id": 1 })

// Índice para busca por ano e semestre
db.alunos.createIndex({ "historico.ano": 1, "historico.semestre": 1 })

// Índice para relacionamento com cursos
db.alunos.createIndex({ "curso._id": 1 })

// Índice para departamentos
db.departamentos.createIndex({ "coordenador._id": 1 })
```
