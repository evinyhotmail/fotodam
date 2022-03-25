## Aplicativo FotoDAM
**Breve Descripción:**
FotoDAM, es una aplicación web que permite a sus usuarios gestionar sus imágenes; parte del nombre de esta aplicación lo componen las siglas "DAM", del inglés: Digital Asset Management.

FotoDAM en su primera versión pretende ir más allá de un simple banco de imágenes, donde puedas añadir, modificar y eliminar una imagen.

En su primera versión está concebida para que quien la use, pueda, de una manera sencilla, realizar búsquedas de las imágenes almacenadas, es decir, esta aplicación cuenta con un elemento de búsqueda que permite al usuario encontrar rápidamente la imagen que se esté buscando, tomando en cuenta el nombre de la imagen, título o descripción. 

FotoDAM está pensado para que en sus próximas versiones se puedan manipular los metadatos de las imágenes.

Nos vemos en las próximas versiones...

## ¿Qué necesito para ejecutar esta aplicación? 

## Para comenzar:

Crea un nuevo directorio en el ordenador.

Si estás en windows y tienes instalado git, haz clic-derecho y selecciona "Git Bash Here" desde el menú contextual. 

Ya estando en la consola, escribe el siguiente comando: git clone https://github.com/evinyhotmail/fotodam.git

Salir de la consola de Git.

Dentro de tu ordenador ha debido crearse un directorio llamado **fotodam**, entra en él.

Ejecuta: “python manage.py runserver” para iniciar el servidor web de Django.

Para ver la aplicación en ejecución, abre tu navegador y dirígete a la dirección: http://127.0.0.1:8000/

**Nota:** Recuerda que es necesario instalar algunos paquetes de python. Para obtener más información, consulta el archivo: requirements.txt.

Por ejemplo, para este desarrollo se ha utilizado **Pillow**, que es una biblioteca adicional gratuita y de código abierto para el lenguaje de programación Python que agrega soporte para abrir, manipular y guardar muchos formatos de archivo de imagen diferentes.

## Más cosas que te interesan:
Para entrar en la aplicación cuentas con:

3 usuarios que ya están configurados: 
	
	- user1(standard user), password=Zaq12wsx!
	- user2(standard user), password=Zaq12wsx!
	- superman(superuser) , password=Zaq12wsx! (Solo es usado para entrar al admin panel de Django)
  

**Nota**: el código de distribución contiene una información precargada, es decir, para poder probar la gestión de la aplicación ya se tienen algunas categorías predefinidas, algunas imágenes de prueba, etc.

- Imágenes:
Media: file in /media/user_user1/images
Media: file in /media/user_user2/images

- Database: (db.sqlite3) 


**Casos particulares que debes tener en cuenta:**
 - Al momento de añadir una imagen, esta debe por lo menos pertenecer a una tipo de categoría.
 - Cuando estás añadiendo una imagen, todos los campos a llenar son obligatorios, es decir, tanto el título, descripción, clasificación y subida de la imagen son obligatorios.
 - Una imagen puede pertenecer a más de una categoría.
 - El usuario 1 (user1) tiene precargadas 5 imágenes y un fichero tipo pdf.
 - El usuario 2 (user2) tiene precargadas 2 imágenes.
 - Si deseas agregar un usuario o una categoría de imagen, debes hacerlo a través del Panel de administración de Django.

## Entendiendo un poco más: 
El siguiente código es un proyecto realizado en el framework Django llamado: **HATICO** que contiene una sola aplicación llamada **core**, estructurada bajo el estándar de las aplicaciones en Django.

La app **core** primera versión es una aplicación donde se encuentra todo lo relacionado a la autenticación de usuarios, así como también la gestión de imágenes.

## Background:
Lo que motivó la ejecución de este proyecto ha sido la ilusión de poder cumplir el reto de que en menos de 4 días pudiera realizar una aplicación como esta; y más allá de ese reto personal, acercarme más a la posibilidad de formar parte de un proyecto en una empresa con una gran labor social. **Formar a las personas**


## Especificaciones a cubrir:

- Como usuario será necesario poder ver una lista de mis imágenes (imagen y un título)
- Como usuario será necesario poder añadir imágenes a una base de datos
- Como usuario será necesario poder eliminar una imagen
- Como usuario será necesario poder editar una imagen existente. (Editar se refiere a poder modificar el título, por ejemplo).


## Valores agregados (Plus): 
Dado a los requerimientos básicos, se observó que podía hacerse algo más, con la finalidad de entregar un producto más completo y enfocado en el cliente final:
- FotoDAM permite al usuario añadir, tanto un título como también una descripción y una clasificación a la imagen.
- FotoDAM cuenta con un área de búsqueda que permite localizar una imagen fácilmente.
- FotoDAM permite ordenar las imágenes, tanto de manera ascendente como descendente.
- Pese a que era una aplicación pequeña, se ha implementado la parte de autenticación, para así proteger la seguridad de las vistas y accesos a la aplicación.
- Se utilizaron tecnologías como JavaScript, del lado del front-end, para mejorar la experiencia del usuario.


## Ficheros:
- **models.py:** contiene todos los modelos de la APP  (3)
- ImageCategory => Donde se almacenan las diferentes categorías de las imágenes.
- ImageBank => Es donde recide toda la información de las imágenes.

**NOTA**: Existe un tercer modelo llamado: core_imagebank_categories; este modelo es creado automáticamente por django debido a que dentro del modelo:
ImageBank tengo una relación: Many2Many.

Este modelo solo se puede ver, por ejemplo, si abres el fichero: db.sqllite3 utilizando SQLiteStudio.

- **views.py:**  contiene todas las vistas de la APP (6)
- **forms.py:**  contiene todas las formas de la APP (1)

**functions.py:** contiene todas las funciones personalizadas
  functions:
- getImageCategories()=> Retorna todas las categorías de una imagen.
- DeleteFile()=> Realiza la eliminación física de la imagen en el disco.


**Templates:**
- base.html => Usado como fichero base para el layauot de la página de login.
- crud_image.html => un único fichero reusado para hacer toda la gestión con las imágenes, es decir, agregar, modificar y eliminar.
- dashboard.html => Es donde el usuario puede ver todas sus imágenes.
- footer.html => Muestra el pie de página de la aplicación.
- header.html => Muestra la cabecera de la aplicación.
- iferror.html => Otro fichero reutilizado para mostrar cualquier error que surja dentro de la aplicación.
- layout.html => Utilizado para tener el enmaquetado de toda la aplicación; este fichero es reutilizado  por todas los ficheros .html
- login.html => Usada para que el usuario realice la autenticación de la app.
- messages.html => Template reutilizado para mostrar cualquier mensaje que muestre la aplicación.
- modaldanger.html => Muestra una ventana emergente para confirmar la eliminación de la imagen.
- navbar.html => Usada para mostrar la parte superior de la aplicación, por ejemplo, dónde está el logo, y también para salir de la aplicación.
- selectbuild.html => Usado para mostrar los checkboxes de las diferentes categorías de imágenes.
- sidebar.html => Sirve para mostrar un menú en la parte izquierda, pero ahora mismo está en desuso.


## Últimas cosas importantes:
- Tenga en cuenta que utilicé Python 3.8.5 y no se ha probado en versiones superiores ni inferiores.
- La versión del framework django es: 4.0.3 y no ha sido probada en versiones superiores ni inferiores.
- Solo he desarrollo el CRUD para el tratamiento de las imágenes, si deseas crear nuevos usuarios o nuevas categorías, debes utilizar el Panel de administración de Django, que se encuentra en la siguiente url: http://127.0.0.1:8000/admin/
- Para la versión que se descarga del repositorio Git no están las Test (TDD), sin embargo, las mismas fueron llevadas a cabo para probar vistas y también las relaciones entre modelos, ya que estoy utilizando una relación de M2M en el modelo ImageBank.
- Con respecto a los principios SOLID, se mantuvo en todo momento la calidad de la aplicación, así como el enfoque en mantener la reutilización del código; lo  podéis observar en el caso del CRUD de las imágenes, ya que existe un solo fichero utilizado para tal fin. Tal cual lo menciono anteriormente, la aplicación ya está lista para que en un futuro pueda ser escalada sin ningún problema.

