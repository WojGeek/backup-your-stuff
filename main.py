"""Sincroniza | respaldo de archivos"""

import argparse
import os

from helpers import backup


def accept_params():
    """Recibe parámetros de origen y destino"""
    parser = argparse.ArgumentParser(
        description="Respaldo-sincronización de archivos")

    parser.add_argument("origen", help="Ruta del directorio origen", type=str)
    parser.add_argument("destino", help="Ruta de disco destino", type=str)
    parser.add_argument(
        "-test", default=True, help="Ejecuta sin realizar cambios (predeterminado)", action="store_true"
    )
    parser.add_argument(
        "-verbose", default=False, help="Muestra el progreso", action="store_true"
    )
    parser.add_argument(
        "-backup", default=False, help="Ejecuta el respaldo aplicando cambios (Anula modo: -test)", action="store_true"
    )

    args = parser.parse_args()

    return args.origen, args.destino, args.test, args.verbose, args.backup


if __name__ == "__main__":
    # os.system('clear')
    source_path, destination_path, testing, verbosity, create_backup = accept_params()
    # print(type(source_path))
    # print(type(destination_path))
    # print(type(testing))
    # print(type(verbosity))
    # print(type(create_backup))

    # print(source_path)
    # print(dpestination_path)
    # print(testing)
    # print(verbosity)

    backup.main(source_path, destination_path,
                testing, verbosity, create_backup)
