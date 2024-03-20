import unittest
from app import app


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_admin_route(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)

    def test_mute_user_route(self):
        response = self.app.post("/mute")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Mute user function executed.", response.data)

    def test_unmute_user_route(self):
        response = self.app.post("/unmute")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Unmute user function executed.", response.data)

    def test_kick_user_route(self):
        response = self.app.post("/kick")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Kick user function executed.", response.data)

    def test_ban_user_route(self):
        response = self.app.post("/ban")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Ban user function executed.", response.data)

    def test_unban_user_route(self):
        response = self.app.post("/unban")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Unban user function executed.", response.data)

    def test_edit_user_roles_route(self):
        response = self.app.post("/edit_roles")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Edit user roles function executed.", response.data)

    def test_process_user_route(self):
        response = self.app.post("/process_user", data={"username": "test_user"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Received username: test_user", response.data)


if __name__ == "__main__":
    unittest.main()
