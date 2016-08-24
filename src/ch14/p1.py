#!/usr/bin/env python3

def urlprint(protocol, hos
             t, domain):
    url = '{}://{}.{}'.format(protocol, host, domain)
    print(url)

from io import StringIO
import unittest
from unittest import TestCase
from unittest.mock import patch

class TestURLPrint(TestCase):
    def test_url_gets_to_stdot(self):
        protocol = 'http'
        host = 'www'
        domain = 'example.com'
        expected_url = '{}://{}.{}\n'.format(protocol, host, domain)
        
        with patch('sys.stdout', new=StringIO()) as fake_out:
            urlprint(protocol, host, domain)
            self.assertEqual(fake_out.getvalue(), expected_url)
        

if __name__ == '__main__':
    unittest.main()
