import json
import os
import unittest
import requests

#Positive testcase
class TestBorrowAPI(unittest.TestCase):
    URL_GET_ALL_BORROW = "http://127.0.0.1:5000/borrow-management/all-borrow"
    URL_BORROW = "http://127.0.0.1:5000/borrow-management/borrow"
    borrow = {  
        "book_id": 7,
        "borrow_date": "02-09-2021",
        "return_date": "24-09-2021",
        "student_id": 4
    }
    def test_get_all_borrow(self):
        response = requests.get(self.URL_GET_ALL_BORROW)
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.json()), 0)
    
    def test_get_borrow_byid(self):
        response = requests.get(self.URL_BORROW + "/1")
        self.assertEqual(response.status_code, 200)

    def test_add_borrow(self):
        response = requests.post(self.URL_BORROW, json = self.borrow)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Add success!")
    
    def test_delete_borrow(self):
        response = requests.delete(self.URL_BORROW + "/5")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Deleted Borrow!")

if __name__ == '__main__':
    test = unittest.main()