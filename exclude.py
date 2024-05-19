"""Sincroniza | respaldo de archivos"""

import argparse
import sys

from helpers.exclude import Exclude


def exclude_options():
    """Gestion de exclude para respaldo de archivos"""

    msg = "Exclusiones selectivas de archivos y/o directorios de respaldos"
    parser = argparse.ArgumentParser(description=msg)

    msg = "Listar las exclusiones"
    parser.add_argument("--listing", help=msg, action="store_true")

    group = parser.add_mutually_exclusive_group()

    msg = "Agregar la referencia del archivo o directorio a excluir"
    # parser.add_argument("--exclude", type = str, help = msg)
    group.add_argument("--exclude", type=str, help=msg)

    msg = "Quitar una referencia de exclusión"
    # parser.add_argument("--remove", help = msg)
    group.add_argument("--remove", help=msg)

    args = parser.parse_args()

    if not any(vars(args).values()):
        parser.print_help()
        # parser.print_usage()
        sys.exit(0)

    # try:
    #     args = parser.parse_args()
    # except SystemExit:
    #     parser.print_usage()
    #     sys.exit(0)

    return args.listing, args.exclude, args.remove


if __name__ == "__main__":

    # list_excludes = ''
    # delete_exclude = 'False'
    # add_exclude = ''

    # exclude_options()
    listing, add_pattern, del_pattern = exclude_options()

    # instancia de la clase Exclude

    FILE_PATH = "exclude.json"
    excluder = Exclude(FILE_PATH)

    if add_pattern is not None:
        excluder.exclude(add_pattern)

    if del_pattern is not None:
        excluder.remove(del_pattern)

    if listing:
        excluder.listing()
