from survey import AnonSurvey
import pytest


@pytest.fixture
def language_survey():
    #Запустите с pytest test_survey.py -v -s, чтобы увидеть вывод print()
    print("\n🔧 СОЗДАЮ ФИКСТУРУ language_survey")
    question = "What language did you learn first?"
    survey = AnonSurvey(question)
    print(f"🔧 СОЗДАН ОБЪЕКТ: {survey}")
    print(f"🔧 ВОЗВРАЩАЮ: {survey}")
    return survey
    

def test_store_responses(language_survey):

    language_survey.store_responses('English')
    assert "English" in language_survey.responses

def test_three_store_responses(language_survey):

    responses = ["a","b", "c"]
    for response in responses:
        language_survey.store_responses(response)
    
    for response in responses:
        assert response in language_survey.responses
