import zlib
import zipfile

def compress(file_names):
    print("File Paths:")
    print(file_names)
    # Select the compression mode ZIP_DEFLATED for compression
    # or zipfile.ZIP_STORED to just store the file
    compression = zipfile.ZIP_DEFLATED

    # create the zip file first parameter path/name, second mode
    with zipfile.ZipFile("result.zip", mode="w") as zf:
        for file_name in file_names:
            zf.write('./'+file_name, file_name, compress_type=compression)


file_names= ["champions.csv","championship_count.csv", "club_count.csv","solution.ipynb","functions.py"]
compress(file_names)