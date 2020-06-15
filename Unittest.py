import unittest

#seperate where the test goes within the function 
#################################

#function testing the string 
class TestStringMethods(unittest.TestCase): 
#testing uppercase strings
    def test_upper(self):
        #in self if the string is uppercase the test will pass
        self.assertEqual('foo'.upper(), 'FOO')
#testing if uppercase is true or false
    def test_isupper(self):
        #condition to test if it is 'FOO', then it's True
        self.assertTrue('FOO'.isupper())
        #condition to test if it is 'Foo', then it's False
        self.assertFalse('Foo'.isupper())

    #test to see if there's a space
    def test_split(self):
        #text string 
        s = 'hello world'
        # conditional statement to test for the split (space) between hello and world
        self.assertEqual(s.split(), ['hello', 'world'])
        #check that s.split fails when the seperator is not a string

        with self.assertRaises(TypeError):
            s.split(2) 

#calling on the main function 
if __name__ == '__main__':
    unittest.main()