"""Sincroniza | respaldo de archivos"""

import argparse
import sys

from helpers import backup
# from helpers.exclude import Exclude


def parse_arguments():
    """Recibe parámetros de origen y destino"""

    msg = "Backup your stuff :: Respaldo-sincronización de archivos"
    parser = argparse.ArgumentParser(description=msg)

    parser.add_argument("origen", help="Ruta del directoryectorio origen", type=str)
    parser.add_argument("destino", help="Ruta de disco destino", type=str)

    msg = "Ejecuta sin realizar cambios (predeterminado)"
    parser.add_argument("--test", default=True, help=msg, action="store_true")

    msg = "Muestra el progreso"
    parser.add_argument("--verbose", default=False, help=msg, action="store_true")

    msg = "Ejecuta el respaldo aplicando cambios (Anula modo: -test)"
    parser.add_argument("--backup", default=False, help=msg, action="store_true")

    msg = "Aplicar exclusiones durante el respaldo"
    parser.add_argument("--exclude", default=False, help=msg, action="store_true")

    _args = vars(parser.parse_args())

    # all_arguments = list(args.origen, args.destino,
    #                      args.test, args.verbose, args.backup,
    #                      args.exclude)

    return _args


if __name__ == "__main__":

    args = parse_arguments()

    source_path = args["origen"]
    destination_path = args["destino"]
    testing = args["test"]
    verbosity = args["verbose"]
    create_backup = args["backup"]
    excluding = args["exclude"]


    backup.main(args)
