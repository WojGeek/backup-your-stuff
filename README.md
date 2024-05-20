## Backup your stuff

He desarrollado esta herramienta con dos objetivos en mente. El primero y más importante es el ensayo de programación con Python. Aprender más acerca de automatizar cosas y lograr que el trabajo en la consola de comandos sea eficiente y productivo.

El segundo objetivo es contar con una herramienta confiable y eficiente cuando necesite realizar respaldos de mis asuntos. Por otro lado, proveer un soporte técnico a clientes y garantizar la recuperación de la data. 

Otra

### Características

- Manejo de exclusiones.
- Respaldo en modo de prueba para comprobación.
- Visualización simple o ampliada de la salida durante el respaldo.
- Configurable para automatizar respaldos desde un cron de Linux.


#### Antes de usar

Instalar Poetry

> Linux, macOS, Windows (WSL)

```
     $ curl -sSL https://install.python-poetry.org | python3 -

``` 

> Windows Powershell

```
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -

```

Desinstalar Poetry 

```
curl -sSL https://install.python-poetry.org | python3 - --uninstall
curl -sSL https://install.python-poetry.org | POETRY_UNINSTALL=1 python3 -
```

#### Descargar 


```

  $  git clone https://github.com/WojGeek/backup-your-stuff.git


```

#### Exclusiones


```
   $ python exclude.py

```


#### Sincronización de archivos (respaldo)


```
  $ python backup.py


```






