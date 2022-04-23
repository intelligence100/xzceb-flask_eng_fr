import unittest

from translator import englishToFrench, frenchToEnglish

class TestenglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench("Hello"), "Bonjour") 
       
        self.assertNotEqual(englishToFrench(null), null)  
        

class TestfrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
       
        self.assertNotEqual(frenchToEnglish(null), null) 
        
unittest.main()