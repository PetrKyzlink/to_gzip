import gzip
import shutil
import os

# Připojení umístění souborů
read_folder = os.path.join("var", "log", "")

# Procházení souborů ve složce umístění cyklem for
for file_input in os.listdir(read_folder):
    if not file_input.endswith(".gz"):   # Podmínka pro vynechání již
                                         # zabalených souborů
        with open(read_folder + file_input, mode="rb") as f_in:
            with gzip.open(read_folder + file_input + ".gz", mode='wb',
                           compresslevel=9) as f_out:
                shutil.copyfileobj(f_in, f_out)
                os.remove(read_folder + file_input)  # odstranění původních
                                                     # souborů
