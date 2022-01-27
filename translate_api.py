from googletrans import Translator
import requests, uuid, json
from key import key

class Translate:
	def __init__(self):
		self.subscription_key = key
		self.endpoint = "https://api.cognitive.microsofttranslator.com"

		self.location = "northeurope"
		self.path = '/translate'

		self.constructed_url = self.endpoint + self.path

		self.params = {'api-version': '3.0',
						'from': 'ru',
						'to': 'uk'}

		self.headers = {'Ocp-Apim-Subscription-Key': self.subscription_key,
						'Ocp-Apim-Subscription-Region': self.location,
						'Content-type': 'application/json',
						'X-ClientTraceId': str(uuid.uuid4())}

	# Microsoft translate
	def microsoft_translate(self, origin_text):
		body = [{'text': origin_text}]
		request = requests.post(self.constructed_url, params=self.params, headers=self.headers, json=body)
		response = request.json()

		my_text = json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': '))

		my_txt_tansform = json.loads(my_text)
		txt_translate = my_txt_tansform[0]['translations'][0]['text']

		return txt_translate

	# Google translate
	def google_translate(self, text):
		translator = Translator()
		result = translator.translate(text, src='ru', dest='uk')
		print(result.text)
		return result.text
