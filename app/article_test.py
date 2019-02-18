import unittest
from models import article
Article = article.Article

class ArticleTest(unittest.TestCase):
    

    def setUp(self):
        
        self.new_article = Article('Romain Dillet','Coinbase users can now withdraw Bitcoin SV following BCH fork','If you’re a Coinbase user, you may have seen some new tokens on your account. The Bitcoin Cash chain split into two different chains back in November. It means that if you held Bitcoin Cash on November 15, you became the lucky owner of Bitcoin SV and Bitcoin','http://techcrunch.com/2019/02/15/coinbase-users-can-now-withdraw-bitcoin-sv-following-bch-fork/','"https://techcrunch.com/wp-content/uploads/2017/08/bitcoin-split-2017a.jpg?w=711','2019-02-15T14:53:40Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))


if __name__ == '__main__':
    unittest.main()
