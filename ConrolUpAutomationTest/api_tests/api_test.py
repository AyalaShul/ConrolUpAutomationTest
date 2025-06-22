from api_tests.api_utils import UtilsCli


class TestApi:

    def test_verify_airport_count(self):
        """
        Send a GET request to the endpoint https://airportgap.com/api/airports.
        Verify that the response contains exactly 30 airports
        """
        response = UtilsCli.get_airports()
        assert response.status_code == 200
        count = 0
        for item in response.json()["data"]:
            if item["type"] == "airport":
                count += 1
        assert count == 30

    def test_verify_specific_airports(self):
        """
        Send a GET request to the endpoint https://airportgap.com/api/airports.
        Verify that the response includes the following airports: Akureyri Airport, St. Anthony Airport, CFBBagotville
        """
        airports_names = ["Akureyri Airport", "St. Anthony Airport", "CFB Bagotville"]
        response = UtilsCli.get_airports()
        assert response.status_code == 200
        for item in response.json()["data"]:
            if item["attributes"]["name"] in airports_names:
                airports_names.remove(item["attributes"]["name"])
        assert airports_names.__len__() == 0

    def test_verify_distance_between_airports(self):
        """
        Send a POST request to the endpoint https://airportgap.com/api/airports/distance
        with parameters for the airports KIX and NRT.
        Verify that the calculated distance between these airports is greater than 400 km.
        """
        response = UtilsCli.post_distance("KIX", "NRT")
        assert response.status_code == 200
        response = response.json()
        km = response["data"]["attributes"]["kilometers"]
        assert km > 400