import requests

def get_air_conditioner_dimensions(page):
    """Gets the dimensions for all air conditioners from from the API

    Args:
        page (string): the page the api should point to
    """
    x = requests.get(f'http://wp8m3he1wt.s3-website-ap-southeast-2.amazonaws.com{page}')
    res = x.json()

    for item in res['objects']:
        if  'Air Conditioners' in item['category']:
            air_conditioners.append(item['size'])

    if res['next']:
        get_air_conditioner_dimensions(res['next'])





if __name__ == "__main__":
    air_conditioners = []
    page = '/api/products/1'
    get_air_conditioner_dimensions(page)

