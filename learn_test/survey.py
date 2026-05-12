class AnonSurvey:

    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_responses(self, new_response):
        self.responses.append(new_response)
        

    def show_results(self):
        
        for response in self.responses:
            print(f"{self.question} - {self.responses}")

    