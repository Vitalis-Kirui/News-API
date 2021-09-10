import  unittest
from  models import sources

Source = sources.Sources

class SourcesTest(unittest.TestCase):
    """
    Test class to test the behavior of our source class.
    """

    def setUp(self):
        """
        Set up method that is run before every test.
        """
        self.new_source = Source('citizen', 'Citizen TV', 'Kenya number TV station', 'www.citizentvkenya.co.ke', 'general', 'Kenya')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))

if __name__ == '__main__':
    unittest.main()