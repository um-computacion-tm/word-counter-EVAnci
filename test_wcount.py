#################
#    Imports    #
#################

import unittest
from wcount import word_count

#################
#   Testing     #
#################

class Test_W_Count(unittest.TestCase):
    
    def test_empty_string(self):
        output = word_count('')
        self.assertEqual(output, {})

    def test_easy_string(self):
        input_value = 'hello world hello world xd'
        output = word_count(input_value)
        correct = {
            'hello' : 2,
            'world' : 2,
            'xd' : 1
        }
        self.assertEqual(output, correct)

    def test_medium_string(self):
        input_value = 'Hello world, this is a simple test. This is other sentence.'
        output = word_count(input_value)
        correct = {
            'hello' : 1,
            'world' : 1,
            'this' : 2,
            'is' : 2,
            'a' : 1,
            'simple' : 1,
            'test' : 1,
            'other' : 1,
            'sentence' : 1
        }
        self.assertEqual(output, correct)
    
    def test_difficult_string(self):
        input_value = '''\
        This document is a guide & for installing Arch Linux using the live \
        system booted from an in5stallation medium made from an official \
        insta44llation image. The i0nstallation medium provides accessibility \
        features w##hich are described () on the page Install Arch Linux with \
        accessibility options. ".:; For alternative means of installation, see \
        Category Installation process.'''

        output = word_count(input_value)
        
        result = {
            'this' : 1,
            'document' : 1,
            'is' : 1,
            'a' : 1,
            'guide' : 1,
            'for' : 2,
            'installing' : 1,
            'arch' : 2,
            'linux' : 2,
            'using' : 1,
            'the' : 3,
            'live' : 1,
            'system' : 1,
            'booted' : 1,
            'from' : 2,
            'an' : 2,
            'installation' : 5,
            'medium' : 2,
            'made' : 1,
            'official' : 1,
            'image' : 1,
            'provides' : 1,
            'accessibility' : 2,
            'features' : 1,
            'which' : 1,
            'are' : 1,
            'described' : 1,
            'on' : 1,
            'page' : 1,
            'install' : 1,
            'with' : 1,
            'options' : 1,
            'alternative' : 1,
            'means' : 1,
            'of' : 1,
            'see' : 1,
            'category' : 1,
            'process' : 1
        }
        self.assertEqual(output, result)

if __name__ == '__main__':
    unittest.main()