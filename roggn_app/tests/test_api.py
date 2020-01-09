from django.contrib.auth.models import User
from django.test import TestCase
from tastypie.test import ResourceTestCaseMixin
from tastypie.models import ApiKey

# Import models
from roggn_app.models import Song


"""
https://django-tastypie.readthedocs.io/en/latest/testing.html
"""

class SongResourceTest(ResourceTestCaseMixin, TestCase):

    fixtures = ['test_data.json']
    
    def setUp(self):
        super(SongResourceTest, self).setUp()

        # Create a user and get his API-Key
        self.username = 'tobias.rosskopf'
        self.usermail = 'tobirosskopf@gmail.com'
        self.password = 'test_password'
        self.user = User.objects.create_user(self.username, self.usermail, self.password)
        self.api_key = ApiKey.objects.get(user_id=self.user.id).key

        # Fetch Song object for testing
        self.song_1 = Song.objects.get(name='Highway to Hell')
        self.detail_url = '/api/v1/songs/{0}/'.format(self.song_1.pk)

    def get_credentials(self):
        return self.create_apikey(username=self.username, api_key=self.api_key)

    def test_get_list_unauthenticated(self):
        self.assertHttpUnauthorized(self.api_client.get('/api/v1/songs/', format='json'))

    def test_get_list_json(self):
        resp = self.api_client.get('/api/v1/songs/', format='json', authentication=self.get_credentials())
        # Ckeck for valid JSON
        self.assertValidJSONResponse(resp)
        # Check for count of datasets
        self.assertEqual(len(self.deserialize(resp)['objects']), 1)
        # Check for structure
        self.assertEqual(self.deserialize(resp)['objects'][0], {
            'active': True,
            'duration': '0:03:33',
            'interpret': 'AC/DC',
            'name': 'Highway to Hell',
            'resource_uri': '/api/v1/songs/{0}/'.format(self.song_1.pk)
        })
    
    def test_get_detail_xml(self):
        resp = self.api_client.get(self.detail_url, format='xml', authentication=self.get_credentials())
        # Check for valid XML
        self.assertValidXMLResponse(resp)
