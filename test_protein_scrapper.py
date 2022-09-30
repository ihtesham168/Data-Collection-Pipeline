import unittest
from unittest import mock
from unittest.mock import patch, Mock, call

from myprotein_scrap import Protein

class TestProtein(unittest.TestCase):
        

    def setUp(self):
        self.obj_scrapper = Protein()
    
    @patch('Protein_scrap.Protein.close_ad')
    def test_close_ad(self, mock_close_ad):
        self.obj_scrapper.close_ad()
        mock_close_ad.assert_called_once()

    @patch('Protein_scrap.Protein.accept_cookies')
    def test_cookies(self, mock_cookies:Mock):
        self.obj_scrapper.accept_cookies()
        mock_cookies.assert_called_once()

    @patch('Protein_scrap.Protein.click_search_bar')
    def test_search_bar(self, mock_search_bar:Mock):
        self.obj_scrapper.click_search_bar()
        mock_search_bar.assert_called_once()
        
    @patch('Protein_scrap.Protein.find_protein')
    def test_find_protein(self, mock_find_protein:Mock):
        self.obj_scrapper.find_protein()
        mock_find_protein.assert_called_once()

    @patch('Protein_scrap.Protein.click_start_search')
    def test_start_search(self, mock_start_search:Mock):
        self.obj_scrapper.click_start_search()
        mock_start_search.assert_called_once()
        

    @patch('Protein_scrap.Protein.protein_link_list')
    def test_link_list(self, mock_protein_links:Mock):
        self.obj_scrapper.protein_link_list()
        mock_protein_links.assert_called_once()
    

    @patch('Protein_scrap.Protein.removing_link_list_duplicates')
    def test_Duplicate_links(self, mock_duplicates:Mock):
        self.obj_scrapper.removing_link_list_duplicates()
        mock_duplicates.assert_called_once()

    @patch('Protein_scrap.Protein.protein_info')
    def test_protein_info(self, mock_info:Mock):
        self.obj_scrapper.protein_info()
        mock_info.assert_called_once()
        


    def tearDown(self):
        self.obj_scrapper.driver.quit()
        del self.obj_scrapper

if __name__=="__main__":
    unittest.main(argv=[''], verbosity=3, exit=False)