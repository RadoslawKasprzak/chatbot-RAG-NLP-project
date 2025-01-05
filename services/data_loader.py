import ast

class DataLoader:
    """
    Class responsible for loading data from a file.
    """
    def __init__(self, data_file_path: str):
        self.data_file_path = data_file_path

    def load_data(self):
        """
        Reads data from a .txt file and returns it in the form of e.g. a list of tuples.
        """
        with open(self.data_file_path, 'r', encoding='utf-8') as f:
            file_content = f.read().strip()
        # in the file we have a Python literal (a list with tuples),
        # so we can use ast.literal_eval
        data = ast.literal_eval(file_content)
        return data
