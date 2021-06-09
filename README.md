# MYSQL - APP

## ¿De qué trata?

En esta aplicación está pensada para mostrar el uso de una base de datos, MySQL en este caso, en python

### Dependencias
Las dependencias se incluyen en el archivo *requirements.txt*, ejecutar el siguiente comando para descargarlas.

```bash
pip install -r requirements.txt
```

Para crear un contenedor mysql, utilizar el siguiente commando

```bash
docker run --name mysql1 -e MYSQL_ROOT_PASSWORD=my_clave_secreta -p 3306:3306 mysql
```

