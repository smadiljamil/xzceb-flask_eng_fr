"""Translator FR_EN"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ['version']

authenticator = IAMAuthenticator(f'{apikey}')
language_translator = LanguageTranslatorV3(
    version=f'{version}',
    authenticator=authenticator
)

language_translator.set_service_url(f'{url}')

def english_to_french(english_text):
    """
    English to french
    """
    if english_text is None:
        return None
    response = language_translator.translate(text=english_text,model_id="en-fr").get_result()
    translation = response['translations'][0]['translation']
    return translation



def french_to_english(french_text):
    """
    French to english
    """
    if french_text is None:
        return None
    response = language_translator.translate(text=french_text,model_id="fr-en").get_result()
    translation = response['translations'][0]['translation']
    return translation
