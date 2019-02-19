import unittest
from models import source
Source = source.Source

class SourceTest(unittest.TestCase):
    

    def setUp(self):
        
        self.new_source = Source('abc-news','ABC News','Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.',' "https://abcnews.go.com','general','https://techcrunch.com/wp-content/uploads/2017/08/bitcoin-split-2017a.jpg?w=711','en','us')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))


if __name__ == '__main__':
    unittest.main()
    
    