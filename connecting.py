import xmlrpc.client

url = '' #URL de conexión
db = '' #Base de datos usándose
username = '' #Credencial
password = '' #Credencial de contraseña

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
    [[('title', 'ilike', '%curso 5%')]]))[0]

#Crear la nueva sesión para el curso 5:
models.execute_kw(db, uid, password,
    'my_modulee.sessions', 'create',
    [{'name':'Sesión del Curso 5 desde programación', 'courses_id': course_id}])