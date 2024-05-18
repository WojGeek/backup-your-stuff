"""Sincroniza | respaldo de archivos"""

import argparse

from helpers import exclude


def exclude_options():
    """Recibe parámetros de origen y destino"""
    parser = argparse.ArgumentParser(
        description="Exclusiones selectivas de archivos y/o directorios de respaldos"
    )

    parser.add_argument(
        "-list", help="Listar las exclusiones", action="store_true"
    )

    # group = parser.add_mutually_exclusive_group()

    parser.add_argument(
        "-add", help="Agregar la referencia de un archivo o directorio a excluir")
    parser.add_argument("-delete", help="Quitar una referencia de exclusión")

    args = parser.parse_args()

    return args.delete, args.list, args.add


if __name__ == "__main__":

    delete_exclude, list_excludes, add_exclude = exclude_options()

    print("LIST", list_excludes)
    print("ADD", list_excludes)
    print("Delete:", delete_exclude)

    if delete_exclude:
   
        
    if add_exclude:
        # exclude.main(delete_exclude, list_excludes, add_exclude)
        print("Add: ", delete_exclude)
        
