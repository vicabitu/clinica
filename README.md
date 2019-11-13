## Aspectos Legales y Profesionales 2019
### Trabajo Practico Nº: 1

Catedra e Integrantes
-----

###### Integrantes de la Cátedra
- Dr. Guillermo R. Cosentino
-  Lic. Bruno Zappellini

###### Integrantes del Grupo
- Abitu Victor Andres

Instalación y Uso
---

El Proyecto se corre con Docker

##### Paso 1: Construir la imagen
    git clone https://github.com/vicabitu/clinica.git
    docker-compose build

##### Paso 2: Ejecutar los contenedores
    docker-compose up -d
    
##### Paso 3: Migrar la base de datos
    docker-compose exec web python manage.py migrate --noinput
    
##### Paso 4: Ir a la pagina de inicio
    http://localhost:8000/
    
##### Como crear un super usuario
    docker-compose exec web python manage.py createsuperuser

##### Como usar una consola bash dentro del contenedor
    docker exec -ti <id_contenedor> /bin/sh