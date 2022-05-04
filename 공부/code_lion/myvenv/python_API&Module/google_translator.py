from random import seed
from googletrans import Translator

translator = Translator()
sentence = "좋은 아침입니다"

result = translator.translate(text=sentence, dest="en")
detect = translator.detect(sentence)

print(result.origin)
print(result.text)