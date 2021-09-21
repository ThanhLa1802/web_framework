import json
import os
import unittest
import requests

#Positive Testcase - Require: Start server
class TestBookAPI(unittest.TestCase):
    URL_GET_ALL_BOOKS = "http://127.0.0.1:5000/book-management/books"
    URL_BOOK = "http://127.0.0.1:5000/book-management/book"
    book = {
    "author_id": 1,
    "category_id": 6,
    "name": "Test book",
    "page_count": 200
    }
    def test_get_all_book(self):
        response = requests.get(self.URL_GET_ALL_BOOKS)
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.json()), 0)
    
    def test_get_book_byid(self):
        response = requests.get(self.URL_BOOK + "/1")
        self.assertEqual(response.status_code, 200)
    
    def test_add_book(self):
        response = requests.post(self.URL_BOOK, json = self.book)
        self.assertEqual(response.status_code, 200)

    def test_delete_book(self):
        response = requests.delete(self.URL_BOOK + "/16")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Deleted Book!")

if __name__ == '__main__':
    test = unittest.main()
   