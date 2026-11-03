# Plataforma de Hábitos

## Integrantes
- Andres Alfonso Olvera Gonzalez – Expediente: 758182
- OMARA NICOLE CAMARA LEYVA – Expediente: 757320
- SANTIAGO BARRAGAN PINZON – Expediente: 740433

## Descripción
Plataforma para registrar hábitos y dar seguimiento al bienestar de los usuarios. Usa MongoDB, Cassandra y Dgraph para guardar y consultar la información.

## Flujo de trabajo
1. Levantar los contenedores de MongoDB, Cassandra y Dgraph.
2. Correr `python connect.py` para probar las conexiones.
3. Correr `python populate.py` para insertar los datos de prueba.
4. Correr `python main.py` para ver el menú y elegir una consulta.