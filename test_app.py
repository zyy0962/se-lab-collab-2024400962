import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        data = response.get_json()
        self.assertEqual(data['message'], 'Hello DevOps!')
        self.assertEqual(data['status'], 'running')

    def test_health_endpoint(self):
        response = self.app.get('/health')
        data = response.get_json()
        self.assertEqual(data['status'], 'healthy')

    def test_404_page(self):
        response = self.app.get('/nonexistent')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
