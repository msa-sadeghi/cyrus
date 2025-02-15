import os

files_names = os.listdir("./images")
for f_n in files_names:
    os.rename(f"./images/{f_n}", f"./images/{f_n}".replace(" ", "").replace("(", "").replace(")", ""))
    