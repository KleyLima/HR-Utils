from email.mime import base
from pkgutil import ImpImporter
import tkinter as tk
from tkinter import filedialog
from os.path import basename
from pathlib import PurePath
import sys

def main():
    ids = get_ids()
    source = select_source_directory()

def get_ids():
    ids = []

    print("Cole aqui a coluna de matrículas.")
    while True: 
        id = input()
        if id == '' and ids[-1] == '':
            ids.pop()
            break

        ids.append(id.strip()) 

    print(f"Recebido {len(ids)} matrículas.")
    return ids

def select_source_directory():
    print("Selecione um arquivo qualquer da fonte de arquivos de PDF's")
    full_path = filedialog.askopenfilename()
    target_folder = '/'.join(full_path.split('/')[:-1]) if sys.platform == 'linux' else '\\'.join(full_path.split("\\")[:-1])
    print(f"Os arquivos serão gerados a partir dos PDF's em {target_folder}")
    return target_folder



if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    main()
