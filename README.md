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


<image src="/img/pywin0.png" alt="Step 1 install" border="5px solid green" width="560">

<image src="/img/pywin1.png" alt="Step 2 install" border="5px solid green" width="560">
<image src="/img/pywin2.png" alt="Step 3 install" border="5px solid green" width="560">


### 2. Instalar Git Bash

```
   https://git-scm.com/download/win
```

### 3. Instalar Poetry

   De antemano abrir una terminal con Git Bash

```
   pip install poetry 
```

## Uso en Linux, Windows 10/11, WSL

## Descargar la aplicación

```
  git clone https://github.com/WojGeek/backup-your-stuff.git

```

## Instalar componentes

```
   cd backup-your-stuff/
   poetry shell
   poetry update
```
<image src="/img/poetry-update.png" alt="update-components" border="7px solid green" width="560">


## Agregar Exclusiones

> La aplicación ya viene con las pilas cargadas. Hay una lista de exclusiones precargadas que contribuyen a obtener una transferencia de datos limpia y segura. Lográndose menos espacio de disco para completar una copia de seguridad.

### ¿Qué se excluye?

>Elementos no deseados, aplicaciones y directorios temporales que no tiene utilidad y ocupan muchísimo espacio de disco.


```
   python exclude.py

```
## Screenshot de la aplicación 'exclude.py'
<image src="/img/exclude.png" alt="exclude" border="7px solid green" width="560">

## Inciar una copia de resguardo

> La aplicación se ejecuta de manera predeterminada en modo TEST. De manera,  que no realiza cambios, hasta que el usuario se familiarice con su uso antes de realizar una copia real.


```
  python backup.py

```
## Screenshot de backup.py
<image src="/img/backup.png" alt="backup" border="7px solid green" width="560">


> Espero sea de utilidad!

 Comentarios a: ppwj@yahoo.com

> Toma un café y dale play..!  ;)