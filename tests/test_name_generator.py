import unittest
from media.generate_name import generate_name
import re

class TestNameGenerator(unittest.TestCase):

  def test_generation_of_unique_name(self):
    n1 = generate_name('gamma.jpg')
    n2 = generate_name('gamma.jpg')
    regexp = re.compile(r'^uploads\/[0-9a-f-]{36}\/gamma\.jpg$')
    assert n1 != n2
    assert regexp.search(n1)
