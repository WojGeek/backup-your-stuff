"""Sincroniza | respaldo de archivos"""

import argparse
import sys

from helpers import backup
from helpers.exclude import Exclude


def accept_params():
    """Recibe parámetros de origen y destino"""

    msg = "Backup your stuff :: Respaldo-sincronización de archivos"
    parser = argparse.ArgumentParser(description=msg)

    parser.add_argument("origen", help="Ruta del directorio origen", type=str)
    parser.add_argument("destino", help="Ruta de disco destino", type=str)

    msg = "Ejecuta sin realizar cambios (predeterminado)"
    parser.add_argument("--test", default=True, help=msg, action="store_true")

    msg = "Muestra el progreso"
    parser.add_argument("--verbose", default=False,
                        help=msg, action="store_true")

    msg = "Ejecuta el respaldo aplicando cambios (Anula modo: -test)"
    parser.add_argument("--backup", default=False,
                        help=msg, action="store_true")

    msg = "Aplicar exclusiones durante el respaldo"
    parser.add_argument("--exclude", default=False,
                        help=msg, action="store_true")

    args = parser.parse_args()

    all_arguments = list(args.origen, args.destino,
                         args.test, args.verbose, args.backup,
                         args.exclude)

    return all_arguments


if __name__ == "__main__":

    source_path, destination_path, testing, verbosity, create_backup, excluding = accept_params()

    # TODO:  declarar var exclude
    # list of excludes
    # FILE_PATH = "exclude.json"
    # excluder = Exclude(FILE_PATH)
    # excludes = excluder.load_items()
    # print(excludes)

    EXCLUDE = Exclude("exclude.json").load_items()

    # TODO:  load all exclude
    # TODO:  enviar exclude as argment

    arguments = (source_path, destination_path, testing,
                 verbosity, create_backup, excluding, EXCLUDE)

    print('EXCLUDE: ', excluding)

    backup.main(arguments)

    # print(excludes)
