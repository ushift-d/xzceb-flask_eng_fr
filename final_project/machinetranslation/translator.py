'''Translation module using IBM Watson'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ['version']

authenticator = IAMAuthenticator(apikey)
'''Initialize languange translator instance'''
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
 )
language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(False)
def english_to_french(french_text=''):
    '''Function to translate english to french'''
    if french_text == '':
        return None
    french_text = language_translator.translate(
         text= french_text,
         model_id='en-fr').get_result().get('translations')[0].get('translation')
    return french_text
def french_to_english(french_text=''):
    '''Function to translate french to english'''
    if french_text =='':
        return None
    french_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result().get('translations')[0].get('translation')
    return french_text
