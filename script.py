import requests

url = 'https://docs.google.com/forms/d/e/1FAIpQLSdVwcxOy1qDiEEoNItOvMvwEA851Z0I9uEcxEeWLzLn-6HhSQ/formResponse'

form_data = {'entry.1228452486':'Python',
            'entry.1880669440':'Biblioteca do Taguspark',
            'entry.335142586':'istPython',
            'entry.360213064':'AutorPython',
            'entry.475555996':'PythonTitle',
            'entry.6150132':'python@mail.com'}

headers = {'Referer':'https://docs.google.com/forms/d/e/1FAIpQLSdVwcxOy1qDiEEoNItOvMvwEA851Z0I9uEcxEeWLzLn-6HhSQ/viewform?',
            'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"}

r = requests.post(url, data=form_data, headers=headers)

print('Response status code: ' + str(r.status_code))