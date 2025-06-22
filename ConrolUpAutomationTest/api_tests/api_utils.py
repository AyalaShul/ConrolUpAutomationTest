import requests

BASE_URL = "https://airportgap.com/api"
GET_AIRPORTS = "/airports"

class UtilsCli:

    # @staticmethod
    # def generate_token(email, password):
    #     data = "email=" + email + "&password=" + password
    #     return requests.post(BASE_URL + "/tokens", data).json()["token"]

    @staticmethod
    def get_airports(id_param=""):
        """
        Send GET request https://airportgap.com/api/airports
        :param id_param: optional, if want specific airport
        :return: API response  
        """
        return requests.get(BASE_URL + "/airports", id_param)

    @staticmethod
    def post_distance(from_param, to_param):
        """
        Send POST request https://airportgap.com/api/airports/distance with params: from, to
        :param from_param: source airport name
        :param to_param: destination airport name
        :return: API response
        """
        data = "from=" + from_param + "&" + "to=" + to_param
        return requests.post(BASE_URL + "/airports/distance", data)

