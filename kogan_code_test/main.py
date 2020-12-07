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
            air_conditioner_dimensions.append(item['size'])

    if res['next']:
        get_air_conditioner_dimensions(res['next'])


def get_cubic_weight():
    """Gets the cubic centimeters of all air conditioners in grams

    Returns:
        List: List of cubic centimeters
    """

    cubic_centimeter = [(x['width'] * x['length'] * x['height']) * 0.25 for x in air_conditioner_dimensions]
    return cubic_centimeter

def get_average_cubic_weight(cubic_weights):
    """Gets the average cubic weight in grams

    Args:
        cubic_weights (list): List of cubic centimeters

    Returns:
        Float: Average cubic weight in grams
    """

    amount_of_aircons = len(air_conditioner_dimensions)
    return sum(cubic_weights) / amount_of_aircons

if __name__ == "__main__":
    air_conditioner_dimensions = []
    page = '/api/products/1'
    get_air_conditioner_dimensions(page)
    cubic_centimeter = get_cubic_weight()
    average_cubic_weight = get_average_cubic_weight(cubic_centimeter)
    print(f'average cubic grams: {average_cubic_weight}\naverage cubic kilograms: {average_cubic_weight / 1000}')
