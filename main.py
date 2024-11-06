from faker import Faker
import random
from pymongo import MongoClient
from datetime import datetime

fake = Faker('pt_BR')

mongo_client = MongoClient('localhost', 27017)
mongo_db = mongo_client['FEII'] #Substitui pelo noome do banco de dados doo mongodb


cursos = [
    'Ciência da Computação', 'Engenharia Elétrica', 'Engenharia Mecânica',
    'Engenharia de Produção', 'Administração'
]

departamentos = [
    'Ciência da Computação', 'Matemática', 'Física',
    'Engenharia Elétrica', 'Engenharia de Produção'
]

disciplinas = [
    'Algoritmos e Estruturas de Dados', 'Cálculo I', 'Cálculo II', 'Cálculo III',
    'Álgebra Linear', 'Física I', 'Física II', 'Física III', 'Química Geral',
    'Química Orgânica', 'Programação I', 'Programação II', 'Programação III',
    'Banco de Dados', 'Redes de Computadores', 'Sistemas Operacionais'
]


def gerar_ra():
    return random.randint(100000000, 999999999)


def gerar_professor_id():
    return random.randint(10000000000, 99999999999)


def gerar_data_nascimento():

    data = fake.date_of_birth(minimum_age=18, maximum_age=30)
    return datetime.combine(data, datetime.min.time())


def insert_departamentos():
    departamentos_collection = mongo_db.departamentos
    departamentos_docs = []

    for i, nome_dep in enumerate(departamentos, 1):
        coordenador = {
            "_id": gerar_professor_id(),
            "nome": fake.name(),
            "email": fake.email()
        }

        departamento = {
            "_id": i,
            "nome": nome_dep,
            "coordenador": coordenador
        }
        departamentos_docs.append(departamento)

    if departamentos_docs:
        departamentos_collection.insert_many(departamentos_docs)
    return departamentos_docs


def insert_professores():
    professores_collection = mongo_db.professores
    departamentos = list(mongo_db.departamentos.find())
    professores_docs = []

    for _ in range(10):
        departamento = random.choice(departamentos)
        professor = {
            "_id": gerar_professor_id(),
            "nome": fake.name(),
            "email": fake.email(),
            "departamento": {
                "_id": departamento["_id"],
                "nome": departamento["nome"]
            },
            "historico_disciplinas": []
        }
        professores_docs.append(professor)

    if professores_docs:
        professores_collection.insert_many(professores_docs)
    return professores_docs


def insert_cursos():
    cursos_collection = mongo_db.cursos
    departamentos = list(mongo_db.departamentos.find())
    cursos_docs = []

    for i, nome_curso in enumerate(cursos, 1):
        departamento = random.choice(departamentos)

        matriz_curricular = []
        for disciplina in random.sample(disciplinas, min(len(disciplinas), 10)):
            matriz_curricular.append({
                "disciplina": {
                    "_id": fake.unique.random_number(digits=6),
                    "nome": disciplina
                },
                "semestre_recomendado": random.randint(1, 8)
            })

        curso = {
            "_id": i,
            "nome": nome_curso,
            "departamento": {
                "_id": departamento["_id"],
                "nome": departamento["nome"]
            },
            "matriz_curricular": matriz_curricular
        }
        cursos_docs.append(curso)

    if cursos_docs:
        cursos_collection.insert_many(cursos_docs)
    return cursos_docs


def insert_alunos():
    alunos_collection = mongo_db.alunos
    cursos = list(mongo_db.cursos.find())
    professores = list(mongo_db.professores.find())
    alunos_docs = []

    for _ in range(50):
        curso = random.choice(cursos)

        historico = []
        for disciplina in random.sample(curso["matriz_curricular"],
                                        min(len(curso["matriz_curricular"]), 5)):
            professor = random.choice(professores)
            historico.append({
                "disciplina": disciplina["disciplina"],
                "professor": {
                    "_id": professor["_id"],
                    "nome": professor["nome"]
                },
                "ano": random.randint(2010, 2024),
                "semestre": random.randint(1, 2),
                "nota_final": round(random.uniform(0, 10), 2)
            })

        aluno = {
            "_id": gerar_ra(),
            "nome": fake.name(),
            "data_nascimento": gerar_data_nascimento(),  # Usando a nova função
            "email": fake.email(),
            "curso": {
                "_id": curso["_id"],
                "nome": curso["nome"]
            },
            "historico": historico
        }
        alunos_docs.append(aluno)

    if alunos_docs:
        alunos_collection.insert_many(alunos_docs)
    return alunos_docs


def insert_grupos_tcc():
    grupos_tcc_collection = mongo_db.grupos_tcc
    professores = list(mongo_db.professores.find())
    alunos = list(mongo_db.alunos.find())
    grupos_docs = []

    for i in range(10):
        orientador = random.choice(professores)
        membros = []

        for aluno in random.sample(alunos, random.randint(2, 4)):
            membros.append({
                "_id": aluno["_id"],
                "nome": aluno["nome"],
                "curso": aluno["curso"]
            })

        grupo = {
            "_id": i + 1,
            "tema": fake.bs(),
            "orientador": {
                "_id": orientador["_id"],
                "nome": orientador["nome"],
                "email": orientador["email"]
            },
            "membros": membros
        }
        grupos_docs.append(grupo)

    if grupos_docs:
        grupos_tcc_collection.insert_many(grupos_docs)
    return grupos_docs


def main():
    # Limpando as coleções existentes
    for collection in mongo_db.list_collection_names():
        mongo_db[collection].drop()

    print("Inserindo departamentos...")
    departamentos = insert_departamentos()

    print("Inserindo professores...")
    professores = insert_professores()

    print("Inserindo cursos...")
    cursos = insert_cursos()

    print("Inserindo alunos...")
    alunos = insert_alunos()

    print("Inserindo grupos de TCC...")
    grupos_tcc = insert_grupos_tcc()

    print("Dados inseridos com sucesso!")


if __name__ == "__main__":
    main()
