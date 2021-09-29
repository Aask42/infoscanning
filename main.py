import requests
from creds import api_key

def fetch_report_by_domain(target_domain):
    url2 = 'https://wisquas.lostrabbitlabs.com/api/report'
    data = {'query': str(target_domain) }
    headers = {'X-api-key': api_key}

    try:
        r = requests.post(url2, data=data, headers=headers, allow_redirects=False)
    except Exception as e:
        print(e)
    
    return r

r = fetch_report_by_domain('DOMAIN')
json_var = r.json()
print(json_var)