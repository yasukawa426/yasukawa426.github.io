import os
import datetime
import shutil


if __name__ == "__main__":
    PATH = "./html"
    FOLDER_NAME = "test_folder"
    FILE_NAME = "test_file.html"
    MAX_ITERATIONS = 100

    if os.path.exists(f"{PATH}/{FOLDER_NAME}"):
        shutil.rmtree(f"{PATH}/{FOLDER_NAME}")

    start_time = datetime.datetime.now()

    # Generate html files and folders using MAX_ITERATIONS
    # html
    #  \_ test_file.html
    #   \_test_folder
            #  \_ test_file.html
            #   \_test_folder
            #           ...
    
    i = 0
    while i < MAX_ITERATIONS:
        PATH = PATH + "/" + FOLDER_NAME

        os.mkdir(PATH)

        file = open(PATH + "/" + FILE_NAME, "w")
        file.close()

        i += 1

    end_time = datetime.datetime.now()
    elapsed_time = end_time - start_time
    print(f"Folders generated in: {elapsed_time.total_seconds() * 1000}ms")
