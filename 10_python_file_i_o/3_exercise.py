# searched for python offline translate pipi to find translate
# pypi.org/project/translate

from translate import Translator

translator = Translator(to_lang="ja")

try:
    with open('./exercise.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
        with open('./test-ja.txt', mode="w") as write_file:
            write_file.write(translation)
except FileNotFoundError as e:
    print('check your file path')
