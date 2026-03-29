def load_data(filename):
    with open(filename, "r") as file:
        return file.readlines()