class AnonymousSurvey():
    """Collect anonymous survey answer"""

    def __init__(self, question):
        """save a question, prepare for storing answer"""
        self.question = question
        self.responses = []

    def show_question(self):
        """show survey"""
        print(self.question)

    def store_response(self, new_response):
        """store single survey response"""
        self.responses.append(new_response)

    def show_results(self):
        """show all responses"""
        print("Survey results:")
        for response in self.responses:
            print('- ' + response)
