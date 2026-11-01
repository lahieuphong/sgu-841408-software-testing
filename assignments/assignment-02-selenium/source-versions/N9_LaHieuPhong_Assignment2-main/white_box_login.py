import requests
import unittest

class TestOpenCartLogin(unittest.TestCase):
    BASE_URL = "http://localhost/demo"

    def setUp(self):
        self.session = requests.Session()

    def test_login_valid_credentials(self):
        """Kiểm thử đăng nhập với thông tin hợp lệ."""
        response = self.session.post(
            f"{self.BASE_URL}/index.php?route=account/login&language=en-gb",
            data={"email": "hieuphong144@gmail.com", "password": "21112003"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("My Account", response.text)

    def test_login_invalid_credentials(self):
        """Kiểm thử đăng nhập với thông tin không hợp lệ."""
        response = self.session.post(
            f"{self.BASE_URL}/index.php?route=account/login&language=en-gb",
            data={"email": "test@example.com", "password": "wrong_password"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("Warning: No match for E-Mail Address and/or Password.", response.text)

    def test_login_empty_fields(self):
        """Kiểm thử đăng nhập với các trường rỗng."""
        response = self.session.post(
            f"{self.BASE_URL}/index.php?route=account/login&language=en-gb",
            data={"email": "", "password": ""}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("Warning: No match for E-Mail Address and/or Password.", response.text)

    def tearDown(self):
        self.session.close()

if __name__ == "__main__":
    unittest.main()