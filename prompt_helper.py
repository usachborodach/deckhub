import yaml
import pyperclip

file = open('quotes.yml')
data = yaml.safe_load(file)

prefix = 'Сгенерируй иллюстрацию для китайской идиомы. Формат - вертикальный, для телефона. обязательно оставляй на иллюстрации иероглифы и транскрипцию к ним. Идиома: '

for index, item in enumerate(data):
    print(f'{index + 1} of {len(data)}')
    prompt = prefix + f'{item["text"]}'
    pyperclip.copy(prompt)
    print(f'prompt copied: {prompt}')
    input()
    filename =  item["_id"] + '.jpeg'
    pyperclip.copy(filename)
    print(f'filename copied: {filename}')
    input()