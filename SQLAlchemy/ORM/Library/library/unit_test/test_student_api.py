import json
import unittest
import requests

#Positive testcase
class TestBookAPI(unittest.TestCase):
    URL_GET_ALL_STUDENT = "http://127.0.0.1:5000/student-management/students"
    URL_STUDENT = "http://127.0.0.1:5000/student-management/student"
    student = {
        "birth_date": "09-08-1986",
        "class_name": "10A4",
        "gender": "Male",
        "name": "Ronaldo"
    }
    def test_get_all_student(self):
        response = requests.get(self.URL_GET_ALL_STUDENT)
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.json()), 0)
    
    def test_get_student_byid(self):
        response = requests.get(self.URL_STUDENT + "/1")
        self.assertEqual(response.status_code, 200)
    
    def test_add_student(self):
        response = requests.post(self.URL_STUDENT, json = self.student)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Add success!")
    
    def test_update_student(self):
        response = requests.put(self.URL_STUDENT + "/4", json= {"name": "Ronaldo", "class_name": "12a4"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Updated Student!")
    
    def test_delete_student(self):
        response = requests.delete(self.URL_STUDENT + "/5")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Deleted Student!")

if __name__ == '__main__':
    test = unittest.main()
   