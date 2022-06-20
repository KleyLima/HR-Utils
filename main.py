import tkinter as tk
from tkinter import filedialog
from os import listdir, mkdir
import sys
from shutil import copyfile

def main():
    ids = get_ids()
    source = select_source_directory()
    files = get_files_to_rename(source)
    output = create_output_folder(source)
    rename_files(files, output, ids)

def get_ids():
    ids = []

    print("Cole aqui a coluna de matrículas.")
    print("Aperte ENTER duas vezes quando acabar.")
    while True: 
        id = input()
        if id == '' and ids[-1] == '':
            ids.pop()
            break

        ids.append(id.strip()) 

    print(f"Recebido {len(ids)} matrículas.")
    return ids

def linux_windows(linux, windows):
    return linux if sys.platform == "linux" else windows

def select_source_directory():
    print("Selecione um arquivo qualquer da fonte de arquivos de PDF's")
    full_path = filedialog.askopenfilename()
    print(full_path)
    target_folder = '/'.join(full_path.split('/')[:-1])
    print(f"Os arquivos serão gerados a partir dos PDF's em {target_folder}")
    return target_folder

def get_files_to_rename(path):
    files = sorted(listdir(path)) 
    return [linux_windows(f"{path}/{pdf}", f"{path}\\{pdf}") for pdf in files]

def create_output_folder(base_path):
    new_dir = linux_windows(f"{base_path}/output/", f"{base_path}\\output\\")
    mkdir(new_dir)
    return new_dir

def rename_files(files, target, ids):
    validate(ids, files)
    for pdf, id in zip(files, ids):
        new_name = target + f"{id}_VT.pdf"
        copyfile(pdf, new_name)
        print(f"{new_name} salvo")
    input("Operação finalizada.")

def validate(ids, files):
    qtd_ids = len(ids)
    qtd_files = len(files)
    if qtd_ids != qtd_files:
        raise Exception(f"O número de matrículas deve ser igual o número de arquivos. Matrículas: {qtd_ids}. Arquivos: {qtd_files}")

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    main()
