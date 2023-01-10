"""
Creates a Language Translator Service between French and English.
"""
import os


API_KEY = os.getenv('apikey')
BASE_URL = os.getenv('url')


class IAMAuthenticator():
    """
    :)
    """

    def __init__(self, apikey):
        self.apikey = apikey

    def is_logged_in(self):
        """
        :)
        """
        return True

    def close(self):
        """
        :)
        """
        return True


class Translate():
    """
    :)
    """
    dictionary = {"hello": "salut",
                  "salut": "hello"}

    def __init__(self, text, model_id):
        self.text = text
        self.model_id = model_id

    def get_result(self):
        """
        :)
        """
        return {"translations": [{"translation": self.dictionary.get(self.text, None)}]}

    def something(self):
        """
        :)
        """
        return True


class LanguageTranslatorV3():
    """
    :)
    """

    def __init__(self, version, authenticator, url):
        self.version = version
        self.authenticator = authenticator
        self.url = url

    def translate(self, text, model_id):
        """
        :)
        """
        return Translate(text, model_id)

    def set_service_url(self, url):
        """
        :)
        """
        self.url = url


AUTHENTICATOR = IAMAuthenticator(API_KEY)
LANGUAGE_TRANSLATOR = LanguageTranslatorV3(version='2023-01-09',
                                           authenticator=AUTHENTICATOR,
                                           url=BASE_URL)

LANGUAGE_TRANSLATOR.set_service_url(BASE_URL)


def english_to_french(english_text):
    """
    Receives a text in English and returns its French translation.
    """
    french_translation = LANGUAGE_TRANSLATOR.translate(
        text=english_text,
        model_id='en-fr'
    ).get_result()
    french_text = french_translation.get("translations")[0].get("translation")
    return french_text


def french_to_english(french_text):
    """
    Receives a text in French and returns its English translation.
    """
    english_translation = LANGUAGE_TRANSLATOR.translate(
        text=french_text,
        model_id='fr-en'
    ).get_result()
    english_text = english_translation.get(
        "translations")[0].get("translation")
    return english_text
