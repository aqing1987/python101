import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """test for class Anonymoussurvey"""

    def setUp(self):
        """
        create a Anonymoussurvey object, and responses used for test methods
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Japnese']

    def test_store_single_response(self):
        """test if single response can be stored"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn('English', self.my_survey.responses)

    def test_store_tree_responses(self):
        """test if three responses can be stored"""
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


unittest.main()
