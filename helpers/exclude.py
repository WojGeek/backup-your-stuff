"""Exclude"""

import sys
import json

file_name = "exclude.json"


def load_json(file_name):
    """Cargar contenido del archivo"""

    try:
        with open(file_name, "r", encoding="utf-8") as json_file:
            datos = json.load(json_file)

    except FileNotFoundError:
        print(f"El archivo {file_name} no existe")
        datos = set()
    return datos


def save_json(datos, file_name):
    """Save JSON"""
    with open(file_name, "w",  encoding="utf-8") as file:
        json.dump(list(datos), file)


def list_files(file_name):
    data = load_json(file_name)

    for i in data:
        print(f"{i}")


def add_exclude(pattern):
    """Exclude files or directory"""

    try:
        data = load_json(file_name)

        new_data = set(data)

        print('Datatype: ', type(new_data))

        new_data.add(pattern)

        save_json(new_data, file_name)

    except ValueError:
        print("Error: Adding a new exclude")


def main(delete_exc, list_exc, exclude_pattern):
    """Gestión de opciones  para exclusiones"""

    # listing
    if list_exc:
        print("-" * 3 + " Listado de exclusiones " + "-" * 3)
        list_files(file_name)

    # adding exclude
    if exclude_pattern != 'None':
        add_exclude(exclude_pattern)
        list_files(file_name)
        
    
    # delete exclude     
    if delete_exc:
        print('Delete exclude: ',delete_exc)

        # print("=" * 3 + " Report " + "=" * 3)

        # print(f"- Elemento agregado: {new_value } ")
        # print('- Elementos en archivos: ', len(new_data))

        # print(data)
