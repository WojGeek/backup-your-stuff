# Backup your stuff

He desarrollado esta herramienta con dos objetivos en mente. 

El primero lugar y de mucha importancia para mi formación como DevOps, es proseguir con los  ensayos de programación con Python a fin de mejorar mis conocimientos en desarrollar aplicaciones y de automatizar tareas en servidores. 

El segundo objetivo fue optimizar la herramienta que había  utilizado para proveer a mis clientes, respaldo y  recuperación de sus datos. 

## ¿Qué ofrece esta herramienta?

**Realizar copias de seguridad de manera  eficiente y confiable.**  Porque fue desarrollada con componentes actualizados del  lenguaje Python, y una interfaz minimalista y amigable. Además, he comprobado que los resultados  de la copias en la consola de comandos son consistentes y más rápido en comparación a una interfaz gráfica.

## Características

- Manejo de exclusiones.
- Respaldo en modo de prueba para comprobación.
- Copiado de archivos a una nueva carpeta en la misma computadora.
- Copiado a un almacenamiento externo, por ejemplo: una unidad USB.
- Copiado en un segundo disco para copias de seguridad.
- Respaldo en almacenamientos conectados a la red.
- Visualización simple o ampliada de la salida durante el respaldo.
- Configurable para automatizar respaldos desde un cron de Linux.


## Requerimientos para Windows 10/11

### 1. Instalar Python

```
   https://www.python.org/downloads/windows/ 
```


<image src="/img/pywin0.png" alt="Step 1 install" border="5px solid green" width="551">

<image src="/img/pywin1.png" alt="Step 2 install" border="5px solid green" width="551">
<image src="/img/pywin2.png" alt="Step 3 install" border="5px solid green" width="551">


### 2. Instalar Git Bash

```
   https://git-scm.com/download/win
```

### 3. Instalar Poetry


#### Descargar 

```
```

  git clone https://github.com/WojGeek/backup-your-stuff.git


```

#### Exclusiones

   - Para agregar los EXCLUDE que evitarán el respaldo de directorios innecesarios.

```
   $ python exclude.py

```


#### Sincronización de archivos (respaldo)

#####  > Let the party begins  ;)

   -  Ejecutar la aplicación de respaldo

```
  $ python backup.py


```

