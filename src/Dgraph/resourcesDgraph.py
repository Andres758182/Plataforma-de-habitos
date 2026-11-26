import pydgraph
import csv
import json

client_stub = pydgraph.DgraphClientStub('localhost:9080')
client = pydgraph.DgraphClient(client_stub)

schema = """
    username: string @index(hash) .
    age: int .
    gender: string .
    city_name: string @index(hash) .
    country: string .
    habit_name: string @index(hash) .
    creation_date: string .
    type: string .
    goal: string .
    category_name: string .
    challenge_name: string @index(hash) .
    goal: int .
    description: string .
    duration: int .
    cuantity: int .
    title: string .
    description: string .

    HAS_HABIT: [uid] @reverse .
    PARTICIPATES_IN: [uid] @reverse .
    FRIENDS_WITH: [uid] .
    WINS_A: [uid] .
    LIVE_IN: [uid] @reverse .
    BELONG: [uid] @reverse .
    OWN: [uid] .
    PERTAIN: [uid] @reverse .

    type Users {
        username
        age
        gender
        HAS_HABIT
        PARTICIPATES_IN
        FRIENDS_WITH
        WINS_A
        LIVE_IN
    }

    type City {
        city_name
        country
    }

    type Habit {
        habit_name
        creation_date
        type
        goal
        BELONG
    }

    type Category {
        category_name
    }

    type Challenge {
        challenge_name
        goal
        description
        duration
    }

    type Achivement {
        cuantity
        title
        description
        OWN
        PERTAIN
    }
    
    """

async def create_schema(schema):
    try:
        client.alter(pydgraph.Operation(schema=schema))
        op = pydgraph.Operation(schema=schema)
        client.alter(op)
    finally:
        client_stub.close()

async def drop_all():
    op = pydgraph.Operation(drop_all=True)
    client.alter(op)


async def parse_location(location_str):
    lon, lat = location_str.split(",")
    return {"type": "Point", "coordinates": [float(lon), float(lat)]}

async def load_node(node):
    txn = client.txn()
    try:
        res = txn.mutate(set_obj=node)
        txn.commit()
        return res.uids
    finally:
        txn.discard()

async def create_edges(csvtxt,node1_uids, node2_uids, col1_name, col2_name, relation):
    txn = client.txn()
    try:
        with open(csvtxt) as f:
            reader = csv.DictReader(f)
            for row in reader:
                txn.mutate(set_obj={
                    "uid": node1_uids[row[col1_name]],
                    relation: {
                    "uid": node2_uids[row[col2_name]]
                    }
                })

        txn.commit()
    finally:
        txn.discard()

'''
Requerimiento 1 - Retos de Amigos en la Categoría Principal del Usuario
Requerimiento: 
Encontrar la categoría con más retos de un usuario, y mostrar los retos realizados por los amigos del usuario que pertenezcan a dicha categoría. 
Resultado esperado:
Una lista de retos pertenecientes a la categoría con mayor actividad del usuario, realizados por sus amigos, incluyendo título, descripción y duración.
'''

async def challenge_friends_recom():
    pass
  
'''
Requerimiento 2 - Historial de Hábito Público por Amigos
Requerimiento:
Obtener el historial/estadísticas de un hábito público por los amigos de un usuario. 
Resultado esperado:
Una lista estructurada con el historial de entradas y métricas de uso de un hábito público específico por parte de los amigos del usuario.
'''

async def logs_habits_friends():
    pass

'''
Requerimiento 3 - Logros Asociados a los Hábitos de los Amigos
Requerimiento:
Encontrar los hábitos de los amigos de un usuario. Después mostrar los logros pertenecientes al hábito. 
Resultado esperado:
Una lista de los hábitos de los amigos del usuario junto con los logros asociados a cada uno de ellos (título, descripción y fecha de obtención).
'''

async def achivement_friends():
    pass

'''
Requerimiento 4 - Usuarios con Mayor Afinidad de Categorías
Requerimiento:
Encontrar los usuarios que más compartan su categoría con más hábitos de un usuario. 
Resultado esperado:
Una lista de usuarios ordenada de forma descendente según el número de categorías en común que comparten con los hábitos principales del usuario.
'''

async def users_recom_category():
    pass

'''
Requerimiento 5 - Retos Relacionados al Último Hábito Iniciado
Requerimiento:
Encontrar retos que pertenezcan a la categoría del último habito que empezó un usuario. 
Resultado esperado:
Una lista de retos asociados a la misma categoría del último hábito iniciado por el usuario, mostrando su título, objetivo y descripción.
'''
async def challenge_habit_category():
    pass

'''
Requerimiento 6 - Usuarios Residentes en la Misma Ciudad
Requerimiento:
Encontrar usuarios que compartan ciudad con un usuario especifico. 
Resultado esperado:
Una lista de usuarios que residen en la misma localidad o ciudad que el usuario de referencia, mostrando sus nombres de usuario y datos de perfil básicos.
'''

async def users_city():
    pass


'''
Requerimiento 7 - Retos de una Ciudad y Categoría Específica
Requerimiento:
Encontrar retos de una categoría especifica inscritos por usuarios que viven en la misma ciudad de un usuario especifico. 
Resultado esperado:
Una lista de retos de la categoría dada, filtrados por aquellos en los que están inscritos usuarios que comparten la misma ciudad que el usuario principal.
'''

async def challenge_city_recom():
    pass


'''
Requerimiento 8 - Red de Amigos con Retos Activos en Común
Requerimiento:
Encontrar los amigos de los amigos de un usuario que estén participando en los mismos retos activos.
Resultado esperado:
Una lista de usuarios (amigos de amigos) con sus respectivos nombres de usuario y los retos activos en común que comparten con el usuario principal.
'''
async def friends_challenge():
    pass
