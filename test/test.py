import unittest
import numpy as np
import pandas as pd
from DataPrepKit import read_data, data_summary, handle_missing_values, encode_categorical_data

class TestDataProcessing(unittest.TestCase):

    def test_read_csv(self):
        file_path = 'sample_data.csv'
        data = read_data(file_path)
        self.assertIsInstance(data, pd.DataFrame)

    def test_read_excel(self):
        file_path = 'sample_data.xlsx'
        data = read_data(file_path)
        self.assertIsInstance(data, pd.DataFrame)

    def test_read_json(self):
        file_path = 'sample_data.json'
        data = read_data(file_path)
        self.assertIsInstance(data, pd.DataFrame)

    def test_unsupported_format(self):
        with self.assertRaises(ValueError):
            read_data('sample_data.txt')

    def test_data_summary(self):
        data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        summary = data_summary(data)
        self.assertIsInstance(summary, pd.DataFrame)

    def test_handle_missing_values(self):
        data = pd.DataFrame({'A': [1, 2, np.nan], 'B': [4, np.nan, 6]})
        filled_data = handle_missing_values(data, strategy='mean')
        self.assertIsInstance(filled_data, pd.DataFrame)

    def test_encode_categorical_data(self):
        data = pd.DataFrame({'Category': ['A', 'B', 'A'], 'Value': [1, 2, 3]})
        encoded_data = encode_categorical_data(data, columns=['Category'])
        self.assertIsInstance(encoded_data, pd.DataFrame)

if __name__ == '__main__':
    unittest.main()