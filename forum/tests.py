from django.test import TestCase
import forum.models as models

# Create your tests here.


class TopicModelsTests(TestCase):

    def setUp(self):
        TestCase.setUp(self)
        self.category = models.Category(name='UnitTest')
        self.category.save()
        title = 'This is a Unit Test'
        self.topic = models.Topic(
            category=self.category, title=title, content='')
        self.topic.save()
        self.slug = self.topic.slug

    def tearDown(self):
        TestCase.tearDown(self)
        self.topic.delete()
        self.topic = None
        self.category.delete()
        self.category = None

    def test_get_topic_error(self):
        """Test the error case of the get_topic method"""
        self.assertIsNone(
            models.Topic.get_topic('THIS-IS-AN-INEXISTANT-SLUG-BECAUSE-OF-UPPERCASE'))

    def test_get_topic(self):
        """Test a normal use of the get_topic method"""
        # This should work, because the setUp method has been called before,
        # so a topic exist with the slug equal to self.slug
        self.assertIsNotNone(models.Topic.get_topic(self.slug))
