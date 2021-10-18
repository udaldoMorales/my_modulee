##Programa de Python que se conecta a la API externa de Odoo para leer datos y escribir en ellos.

import xmlrpc.client

url = 'http://localhost:8069' #Localhost y el puerto
db = 'prueba53' #La base de datos que se use en ese momento.
username = 'admin' #Usuario de Odoo
password = 'admin' #Contraseña de usuario de odoo.

#Conectarnos al servidor
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

#Obtener un uid para autenticarnos y "loggearnos"
uid = common.authenticate(db, username, password, {})

#Función para poder hacer los llamados
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

#Guardando en una variable los modelos 
res = (models.execute_kw(db, uid, password,
    'my_modulee.sessions', 'search_read',
    []))

for x in res:
	print (x)
	print("\n")

#Obtener un course_id para la sesión a crear:
course_id = (models.execute_kw(db, uid, password,
    'my_modulee.courses', 'search',
    [[('title', 'ilike', '%curso 1%')]]))[0]

#Crear la nueva sesión para el curso 5:
models.execute_kw(db, uid, password,
    'my_modulee.sessions', 'create',
    [{'name':'Sesión del Curso 5 desde programación', 'courses_id': course_id}])