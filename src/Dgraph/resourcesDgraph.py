import pydgraph
import csv
import json
from collections import Counter

class ResourcesDgraph:
    def __init__(self, client, client_stub):
        self.client = client
        self.client_stub = client_stub

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
    HAVE: [uid] .

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
        HAVE
    }

    type Category {
        category_name
    }

    type Challenge {
        challenge_name
        goal
        description
        duration
        OWN
        PERTAIN
    }

    type Achivement {
        cuantity
        title
        description
    }
    
    """

    async def create_schema(self, schema):
        try:
            self.client.alter(pydgraph.Operation(schema=schema))
            op = pydgraph.Operation(schema=schema)
            self.client.alter(op)
        finally:
            self.client_stub.close()

    async def drop_all(self):
        op = pydgraph.Operation(drop_all=True)
        self.client.alter(op)

    async def parse_location(self, location_str):
        lon, lat = location_str.split(",")
        return {"type": "Point", "coordinates": [float(lon), float(lat)]}

    async def load_node(self, node):
        txn = self.client.txn()
        try:
            res = txn.mutate(set_obj=node)
            txn.commit()
            return res.uids
        finally:
            txn.discard()

    async def create_edges(self, csvtxt, node1_uids, node2_uids, col1_name, col2_name, relation):
        txn = self.client.txn()
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

    async def challenge_friends_recom(self,username):
    
        top_cat_query = """
        query top_user_category($username: string) {
          user(func: eq(username, $username)) {
            PARTICIPATES_IN {
              user_ch_uid as uid
            }
          }
    
          top_category(func: type(Category), orderdesc: val(cat_count), first: 1) @cascade {
            category_name
            cat_count as count(~PERTAIN @filter(uid(user_ch_uid)))
          }
        }
        """
    
        cat_res = self.client.txn(read_only=True).query(top_cat_query, variables={"$username": username})
        cat_data = json.loads(cat_res.json)
    
        top_cats = cat_data.get("top_category", [])
        if not top_cats or top_cats[0].get("cat_count", 0) == 0:
            print(json.dumps([], indent=2, ensure_ascii=False))
            return
    
        top_category = top_cats[0]["category_name"]
    
        friends_query = """
        query friends_challenges_by_category($username: string, $category: string) {
          user(func: eq(username, $username)) {
            FRIENDS_WITH {
              PARTICIPATES_IN @cascade {
                challenge_name
                description
                duration
                PERTAIN @filter(eq(category_name, $category)) {
                  category_name
                }
              }
            }
          }
        }
        """
    
        friends_res = self.client.txn(read_only=True).query(
            friends_query,
            variables={"$username": username, "$category": top_category},
        )
        friends_data = json.loads(friends_res.json)
    
        challenges = []
        seen = set()
    
        for u in friends_data.get("user", []):
            for friend in u.get("FRIENDS_WITH", []):
                for ch in friend.get("PARTICIPATES_IN", []):
                    item = {
                        "titulo": ch.get("challenge_name"),
                        "descripcion": ch.get("description"),
                        "duracion": ch.get("duration"),
                    }
                    key = (item["titulo"], item["descripcion"], item["duracion"])
                    if key not in seen:
                        seen.add(key)
                        challenges.append(item)
    
        print(json.dumps(challenges, indent=2, ensure_ascii=False))

    '''
    Requerimiento 2 - Historial de Hábito Público por Amigos ¡¡¡¡¡¡¡¡¡PREGUNTAR!!!!!!!!!!
    Requerimiento:
    Obtener el historial/estadísticas de un hábito público por los amigos de un usuario.
    Resultado esperado:
    Una lista estructurada con el historial de entradas y métricas de uso de un hábito público específico por parte de los amigos del usuario.
    '''

    async def logs_habits_friends(self,habit):
        pass

    '''
    Requerimiento 3 - Logros Asociados a los Hábitos de los Amigos
    Requerimiento:
    Encontrar los hábitos de los amigos de un usuario. Después mostrar los logros pertenecientes al hábito.
    Resultado esperado:
    Una lista de los hábitos de los amigos del usuario junto con los logros asociados a cada uno de ellos (título, descripción y fecha de obtención).
    '''

    async def achivement_friends(self,username,habit_name):
        query = """
        query achivement_friends($username: string, $habit_name: string) {
            user(func: eq(username, $username)) {
              FRIENDS_WITH {
                username
                HAS_HABIT {
                  habit_name
                  HAVE {
                    title
                  }
                }
              }
            }
        }
        """
        res = self.client.txn(read_only=True).query(query, variables={'$username': username ,'$habit_name': habit_name })
        print(json.dumps(json.loads(res.json), indent=2))

    '''
    Requerimiento 4 - Usuarios con Mayor Afinidad de Categorías
    Requerimiento:
    Encontrar los usuarios que más compartan su categoría con más hábitos de un usuario.
    Resultado esperado:
    Una lista de usuarios ordenada de forma descendente según el número de categorías en común que comparten con los hábitos principales del usuario.
    '''

    async def users_recom_category(self,username):
        top_cat_query = """
        query top_user_category($username: string) {
          user(func: eq(username, $username)) {
            HAS_HABIT {
              user_ch_uid as uid
            }
          }
    
          top_category(func: type(Category), orderdesc: val(cat_count), first: 1) @cascade {
            category_name
            cat_count as count(~BELONG @filter(uid(user_ch_uid)))
          }
        }
        """
    
        cat_res = self.client.txn(read_only=True).query(top_cat_query, variables={"$username": username})
        cat_data = json.loads(cat_res.json)
    
        top_cats = cat_data.get("top_category", [])
        if not top_cats or top_cats[0].get("cat_count", 0) == 0:
            print(json.dumps([], indent=2, ensure_ascii=False))
            return
    
        top_category = top_cats[0]["category_name"]

        query = '''
        query users_by_top_category($username: string, $category: string) {
          users(func: type(Users), orderdesc: val(coincidencias)) @filter(not(eq(username, $username))) @cascade {
            uid
            username
            HAS_HABIT {
              habit_name
              coincidencias as count(BELONG @filter(eq(category_name, $category)))
              BELONG @filter(eq(category_name, $category)) {
                category_name
              }
            }
          }
        }
        '''
        res = self.client.txn(read_only=True).query(query,variables={"$username": username, "$category": top_category})
        print(json.dumps(json.loads(res.json), indent=2))

    '''
    Requerimiento 5 - Retos Relacionados al Último Hábito Iniciado
    Requerimiento:
    Encontrar retos que pertenezcan a la categoría del último habito que empezó un usuario.
    Resultado esperado:
    Una lista de retos asociados a la misma categoría del último hábito iniciado por el usuario, mostrando su título, objetivo y descripción.
    '''
    async def challenge_habit_category(self):
        pass

    '''
    Requerimiento 6 - Usuarios Residentes en la Misma Ciudad
    Requerimiento:
    Encontrar usuarios que compartan ciudad con un usuario especifico.
    Resultado esperado:
    Una lista de usuarios que residen en la misma localidad o ciudad que el usuario de referencia, mostrando sus nombres de usuario y datos de perfil básicos.
    '''

    async def users_city(self):
        pass

    '''
    Requerimiento 7 - Retos de una Ciudad y Categoría Específica
    Requerimiento:
    Encontrar retos de una categoría especifica inscritos por usuarios que viven en la misma ciudad de un usuario especifico.
    Resultado esperado:
    Una lista de retos de la categoría dada, filtrados por aquellos en los que están inscritos usuarios que comparten la misma ciudad que el usuario principal.
    '''

    async def challenge_city_recom(self):
        pass

    '''
    Requerimiento 8 - Red de Amigos con Retos Activos en Común
    Requerimiento:
    Encontrar los amigos de los amigos de un usuario que estén participando en los mismos retos activos.
    Resultado esperado:
    Una lista de usuarios (amigos de amigos) con sus respectivos nombres de usuario y los retos activos en común que comparten con el usuario principal.
    '''
    async def friends_challenge(self):
        pass
