import unittest
from flask.ext.testing import TestCase
from app import app


class AnsibleTests(TestCase):
    render_templates = False

    def create_app(self):
        app.config['TESTING'] = True
        return app

    # def setUp(self):
    #     app.config['TESTING'] = True
    #     self.app = app.test_client()

    def test_see_data_from_table(self):

        tableDictionary = {'ipaddress':'127.0.0.1','hostname':'localhost','proxypath':'localhost.thoughtworks.com'}
        response = self.client.get('/')
        #self.assertEqual(self.get_context_variable('ipaddress'), '127.0.0.1')
        for name in tableDictionary:
            assert name in response.data
            assert tableDictionary[name] in response.data

if __name__ == '__main__':
    unittest.main()



