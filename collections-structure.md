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
