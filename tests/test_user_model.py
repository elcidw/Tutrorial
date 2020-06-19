from module.user import Users
from app import db
from tests.base import BaseTestCase
import unittest


class test_decode_auth_token(BaseTestCase):
    def test_decode_auth_token(self):
        user = Users(
            email='test@test.com',
            password='test',
            username='test',
            name='test',
        )
        db.session.add(user)
        db.session.commit()
        auth_token = user.encode_auth_token(user.id)
        # print(auth_token)
        self.assertTrue(isinstance(auth_token, bytes))
        self.assertGreater(Users.decode_auth_token(auth_token), 1)


if __name__ == '__main__':
    unittest.main()
