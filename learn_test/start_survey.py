from survey import AnonSurvey
#first surveu
first_question = "What language did you learn first?"

language_survey = AnonSurvey(first_question) 

language_survey.show_question()

store_resp = input()

language_survey.store_responses(store_resp)

#second survey
second_question = "What are you favorite color?"

color_survey =AnonSurvey(second_question)

color_survey.show_question()

store_resp = input()

color_survey.store_responses(store_resp)

language_survey.show_results()
color_survey.show_results()