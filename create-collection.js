db.createCollection("departamentos", {
   validator: {
      $jsonSchema: {
         bsonType: "object",
         required: ["_id", "nome"],
         properties: {
            _id: { bsonType: "number" },
            nome: { bsonType: "string" },
            coordenador: {
               bsonType: "object",
               required: ["_id", "nome", "email"],
               properties: {
                  _id: { bsonType: "number" },
                  nome: { bsonType: "string" },
                  email: { bsonType: "string" }
               }
            }
         }
      }
   }
});

db.createCollection("professores", {
   validator: {
      $jsonSchema: {
         bsonType: "object",
         required: ["_id", "nome", "email", "departamento"],
         properties: {
            _id: { bsonType: "number" },
            nome: { bsonType: "string" },
            email: { bsonType: "string" },
            departamento: {
               bsonType: "object",
               required: ["_id", "nome"],
               properties: {
                  _id: { bsonType: "number" },
                  nome: { bsonType: "string" }
               }
            },
            historico_disciplinas: {
               bsonType: "array",
               items: {
                  bsonType: "object",
                  required: ["disciplina", "ano", "semestre"],
                  properties: {
                     disciplina: {
                        bsonType: "object",
                        required: ["_id", "nome"],
                        properties: {
                           _id: { bsonType: "number" },
                           nome: { bsonType: "string" }
                        }
                     },
                     ano: { bsonType: "number" },
                     semestre: { bsonType: "number" }
                  }
               }
            }
         }
      }
   }
});

db.createCollection("cursos", {
   validator: {
      $jsonSchema: {
         bsonType: "object",
         required: ["_id", "nome", "departamento"],
         properties: {
            _id: { bsonType: "number" },
            nome: { bsonType: "string" },
            departamento: {
               bsonType: "object",
               required: ["_id", "nome"],
               properties: {
                  _id: { bsonType: "number" },
                  nome: { bsonType: "string" }
               }
            },
            matriz_curricular: {
               bsonType: "array",
               items: {
                  bsonType: "object",
                  required: ["disciplina", "semestre_recomendado"],
                  properties: {
                     disciplina: {
                        bsonType: "object",
                        required: ["_id", "nome"],
                        properties: {
                           _id: { bsonType: "number" },
                           nome: { bsonType: "string" }
                        }
                     },
                     semestre_recomendado: { bsonType: "number" }
                  }
               }
            }
         }
      }
   }
});

db.createCollection("alunos", {
   validator: {
      $jsonSchema: {
         bsonType: "object",
         required: ["_id", "nome", "data_nascimento", "email", "curso"],
         properties: {
            _id: { bsonType: "number" },
            nome: { bsonType: "string" },
            data_nascimento: { bsonType: "date" },
            email: { bsonType: "string" },
            curso: {
               bsonType: "object",
               required: ["_id", "nome"],
               properties: {
                  _id: { bsonType: "number" },
                  nome: { bsonType: "string" }
               }
            },
            historico: {
               bsonType: "array",
               items: {
                  bsonType: "object",
                  required: ["disciplina", "professor", "ano", "semestre", "nota_final"],
                  properties: {
                     disciplina: {
                        bsonType: "object",
                        required: ["_id", "nome"],
                        properties: {
                           _id: { bsonType: "number" },
                           nome: { bsonType: "string" }
                        }
                     },
                     professor: {
                        bsonType: "object",
                        required: ["_id", "nome"],
                        properties: {
                           _id: { bsonType: "number" },
                           nome: { bsonType: "string" }
                        }
                     },
                     ano: { bsonType: "number" },
                     semestre: { bsonType: "number" },
                     nota_final: { bsonType: "number" }
                  }
               }
            }
         }
      }
   }
});

db.createCollection("grupos_tcc", {
   validator: {
      $jsonSchema: {
         bsonType: "object",
         required: ["_id", "tema", "orientador", "membros"],
         properties: {
            _id: { bsonType: "number" },
            tema: { bsonType: "string" },
            orientador: {
               bsonType: "object",
               required: ["_id", "nome", "email"],
               properties: {
                  _id: { bsonType: "number" },
                  nome: { bsonType: "string" },
                  email: { bsonType: "string" }
               }
            },
            membros: {
               bsonType: "array",
               items: {
                  bsonType: "object",
                  required: ["_id", "nome", "curso"],
                  properties: {
                     _id: { bsonType: "number" },
                     nome: { bsonType: "string" },
                     curso: {
                        bsonType: "object",
                        required: ["_id", "nome"],
                        properties: {
                           _id: { bsonType: "number" },
                           nome: { bsonType: "string" }
                        }
                     }
                  }
               }
            }
         }
      }
   }
});
