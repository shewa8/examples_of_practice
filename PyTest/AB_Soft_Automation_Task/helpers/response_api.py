import requests
import json


def get_api_response():
    resp = []
    links = ['https://aws.random.cat/meow', 'https://random.dog/woof.json', 'https://randomfox.ca/floof/']
    for iteration in links:
        response = requests.get(iteration)
        json_dict = json.loads(response.text)
        if 'file' in json_dict:
            first_request = json_dict['file']
            resp.append(first_request)
        elif 'url' in json_dict:
            second_request = json_dict['url']
            resp.append(second_request)
        elif 'image' in json_dict:
            third_request = json_dict['image']
            resp.append(third_request)
    return resp
