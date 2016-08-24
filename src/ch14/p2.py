#!/usr/bin/env python3

from urllib.request import urlopen
import csv
import unittest
from unittest.mock import patch, MagicMock
import io


def dowprices():
    u = urlopen('http://finance.yahoo.com/d/quotes.csv?s=@^DJI&f=sl1')
    lines = (line.decode('utf-8') for line in u)
    rows = (row for row in csv.reader(lines) if len(row) == 2)
    prices = { name:float(price) for name, price in rows}
    return prices


sample_data = io.BytesIO(b'''\
"IBM",91.1\r
"AA",13.25\r
"MSFT",27.72\r
\r
''')

class Tests(unittest.TestCase):
    @patch('__main__.urlopen',return_value=sample_data)
    def test_downprices(self,mock_urlopen):
        p = dowprices()
        self.assertTrue(mock_urlopen.called)
        
        
if __name__ == '__main__':
    unittest.main()
