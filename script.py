import requests

url = 'https://docs.google.com/forms/d/e/1FAIpQLSdVwcxOy1qDiEEoNItOvMvwEA851Z0I9uEcxEeWLzLn-6HhSQ/formResponse'

form_data = {'entry.1228452486':'Python',
            'entry.1880669440':'Biblioteca do Taguspark',
            'entry.335142586':'istPython',
            'entry.360213064':'AutorPython',
            'entry.475555996':'PythonTitle',
            'entry.6150132':'python@mail.com'}

headers = {'Referer':'https://docs.google.com/forms/d/e/1FAIpQLSdVwcxOy1qDiEEoNItOvMvwEA851Z0I9uEcxEeWLzLn-6HhSQ/viewform?',
            'User-Agent':'Python BIST-AUTO-RENEW'}

r = requests.post(url, data=form_data, headers=headers)

print('Response status code: ' + str(r.status_code))