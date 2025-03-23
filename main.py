import os
import zipfile
import sys

def extract_archive(extract_to):
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)

    archive_path = os.path.join(sys._MEIPASS, "SP-DPI.zip") if hasattr(sys, "_MEIPASS") else "SP-DPI.zip"

    with zipfile.ZipFile(archive_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        print(f'Архив "{archive_path}" распакован в "{extract_to}"')
    return extract_to

def run_program():
    extract_to = os.path.join(os.environ['ProgramFiles'], 'ExtractedFiles')
    dpi_folder = os.path.join(extract_to, 'SP-DPI')
    if not os.path.exists(dpi_folder):
        extracted_folder = extract_archive(extract_to)
    else:
        extracted_folder = extract_to

    path = "SP-DPI\\zapret-winws\\"
    program_path = os.path.join(extracted_folder, path, "preset_russia.cmd")

    if os.path.isfile(program_path):
        os.startfile(program_path)
        print(f'Программа "{program_path}" запущена.')
    else:
        print("Ошибка: Файл не найден. Проверьте путь и попробуйте снова.")

if __name__ == "__main__":
    run_program()