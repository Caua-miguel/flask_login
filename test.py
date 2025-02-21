from project import app
import unittest

class FlaskTestCase(unittest.TestCase):

    # Ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that the login page loads correctly
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Login' in response.data)

    # Ensure login behaves correctly given the corrct credentials
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(username="admin", password="admin"),
            follow_redirects=True)
        self.assertIn(b'Logged in as: admin', response.data)

    # Ensure login behaves correctly given the corrct credentials
    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(username="wrong", password="admin"),
            follow_redirects=True)
        self.assertIn(b'Bad login', response.data)

    # Ensure logout behaves correctly
    def test_logout(self):
        tester = app.test_client(self)
        tester.post(
            '/login',
            data=dict(username="wrong", password="admin"),
            follow_redirects=True)
        response = tester.get('/logout', follow_redirects=True)
        self.assertIn(b'Logged out', response.data)    

if __name__ == '__main__':
    unittest.main()