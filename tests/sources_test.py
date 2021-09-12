import  unittest
from  app.models import Sources

class SourcesTest(unittest.TestCase):
    """
    Test class to test the behavior of our source class.
    """

    def setUp(self):
        """
        Set up method that is run before every test.
        """
        self.new_source = Sources('citizen', 'Citizen TV',
                                 'Kenya number TV station', 'general','www.citizentvkenya.co.ke', 'Kenya')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))