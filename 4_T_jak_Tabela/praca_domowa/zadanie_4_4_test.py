import unittest
import urllib.parse

import requests

from file import AppClass


class CodingRoomsUnitTests(unittest.TestCase):
    def setUp(self):
        get_path = urllib.parse.urljoin(AppClass.APP_URL, "/products_extended")
        self._response = requests.get(get_path)
        self._expected_response = {
            "products_extended": [
                {
                    "id": 1,
                    "name": "Chai",
                    "category": "Beverages",
                    "supplier": "Exotic Liquids",
                },
                {
                    "id": 2,
                    "name": "Chang",
                    "category": "Beverages",
                    "supplier": "Exotic Liquids",
                },
                {
                    "id": 3,
                    "name": "Aniseed Syrup",
                    "category": "Condiments",
                    "supplier": "Exotic Liquids",
                },
                {
                    "id": 4,
                    "name": "Chef Anton's Cajun Seasoning",
                    "category": "Condiments",
                    "supplier": "New Orleans Cajun Delights",
                },
                {
                    "id": 5,
                    "name": "Chef Anton's Gumbo Mix",
                    "category": "Condiments",
                    "supplier": "New Orleans Cajun Delights",
                },
                {
                    "id": 6,
                    "name": "Grandma's Boysenberry Spread",
                    "category": "Condiments",
                    "supplier": "Grandma Kelly's Homestead",
                },
                {
                    "id": 7,
                    "name": "Uncle Bob's Organic Dried Pears",
                    "category": "Produce",
                    "supplier": "Grandma Kelly's Homestead",
                },
                {
                    "id": 8,
                    "name": "Northwoods Cranberry Sauce",
                    "category": "Condiments",
                    "supplier": "Grandma Kelly's Homestead",
                },
                {
                    "id": 9,
                    "name": "Mishi Kobe Niku",
                    "category": "Meat/Poultry",
                    "supplier": "Tokyo Traders",
                },
                {
                    "id": 10,
                    "name": "Ikura",
                    "category": "Seafood",
                    "supplier": "Tokyo Traders",
                },
                {
                    "id": 11,
                    "name": "Queso Cabrales",
                    "category": "Dairy Products",
                    "supplier": "Cooperativa de Quesos 'Las Cabras'",
                },
                {
                    "id": 12,
                    "name": "Queso Manchego La Pastora",
                    "category": "Dairy Products",
                    "supplier": "Cooperativa de Quesos 'Las Cabras'",
                },
                {
                    "id": 13,
                    "name": "Konbu",
                    "category": "Seafood",
                    "supplier": "Mayumi's",
                },
                {
                    "id": 14,
                    "name": "Tofu",
                    "category": "Produce",
                    "supplier": "Mayumi's",
                },
                {
                    "id": 15,
                    "name": "Genen Shouyu",
                    "category": "Condiments",
                    "supplier": "Mayumi's",
                },
                {
                    "id": 16,
                    "name": "Pavlova",
                    "category": "Confections",
                    "supplier": "Pavlova, Ltd.",
                },
                {
                    "id": 17,
                    "name": "Alice Mutton",
                    "category": "Meat/Poultry",
                    "supplier": "Pavlova, Ltd.",
                },
                {
                    "id": 18,
                    "name": "Carnarvon Tigers",
                    "category": "Seafood",
                    "supplier": "Pavlova, Ltd.",
                },
                {
                    "id": 19,
                    "name": "Teatime Chocolate Biscuits",
                    "category": "Confections",
                    "supplier": "Specialty Biscuits, Ltd.",
                },
                {
                    "id": 20,
                    "name": "Sir Rodney's Marmalade",
                    "category": "Confections",
                    "supplier": "Specialty Biscuits, Ltd.",
                },
                {
                    "id": 21,
                    "name": "Sir Rodney's Scones",
                    "category": "Confections",
                    "supplier": "Specialty Biscuits, Ltd.",
                },
                {
                    "id": 22,
                    "name": "Gustaf's Knckebrd",
                    "category": "Grains/Cereals",
                    "supplier": "PB Knckebrd AB",
                },
                {
                    "id": 23,
                    "name": "Tunnbrd",
                    "category": "Grains/Cereals",
                    "supplier": "PB Knckebrd AB",
                },
                {
                    "id": 24,
                    "name": "Guaran Fantstica",
                    "category": "Beverages",
                    "supplier": "Refrescos Americanas LTDA",
                },
                {
                    "id": 25,
                    "name": "NuNuCa Nu-Nougat-Creme",
                    "category": "Confections",
                    "supplier": "Heli Swaren GmbH & Co. KG",
                },
                {
                    "id": 26,
                    "name": "Gumbr Gummibrchen",
                    "category": "Confections",
                    "supplier": "Heli Swaren GmbH & Co. KG",
                },
                {
                    "id": 27,
                    "name": "Schoggi Schokolade",
                    "category": "Confections",
                    "supplier": "Heli Swaren GmbH & Co. KG",
                },
                {
                    "id": 28,
                    "name": "Rssle Sauerkraut",
                    "category": "Produce",
                    "supplier": "Plutzer Lebensmittelgromrkte AG",
                },
                {
                    "id": 29,
                    "name": "Thringer Rostbratwurst",
                    "category": "Meat/Poultry",
                    "supplier": "Plutzer Lebensmittelgromrkte AG",
                },
                {
                    "id": 30,
                    "name": "Nord-Ost Matjeshering",
                    "category": "Seafood",
                    "supplier": "Nord-Ost-Fisch Handelsgesellschaft mbH",
                },
                {
                    "id": 31,
                    "name": "Gorgonzola Telino",
                    "category": "Dairy Products",
                    "supplier": "Formaggi Fortini s.r.l.",
                },
                {
                    "id": 32,
                    "name": "Mascarpone Fabioli",
                    "category": "Dairy Products",
                    "supplier": "Formaggi Fortini s.r.l.",
                },
                {
                    "id": 33,
                    "name": "Geitost",
                    "category": "Dairy Products",
                    "supplier": "Norske Meierier",
                },
                {
                    "id": 34,
                    "name": "Sasquatch Ale",
                    "category": "Beverages",
                    "supplier": "Bigfoot Breweries",
                },
                {
                    "id": 35,
                    "name": "Steeleye Stout",
                    "category": "Beverages",
                    "supplier": "Bigfoot Breweries",
                },
                {
                    "id": 36,
                    "name": "Inlagd Sill",
                    "category": "Seafood",
                    "supplier": "Svensk Sjfda AB",
                },
                {
                    "id": 37,
                    "name": "Gravad lax",
                    "category": "Seafood",
                    "supplier": "Svensk Sjfda AB",
                },
                {
                    "id": 38,
                    "name": "Cte de Blaye",
                    "category": "Beverages",
                    "supplier": "Aux joyeux ecclsiastiques",
                },
                {
                    "id": 39,
                    "name": "Chartreuse verte",
                    "category": "Beverages",
                    "supplier": "Aux joyeux ecclsiastiques",
                },
                {
                    "id": 40,
                    "name": "Boston Crab Meat",
                    "category": "Seafood",
                    "supplier": "New England Seafood Cannery",
                },
                {
                    "id": 41,
                    "name": "Jack's New England Clam Chowder",
                    "category": "Seafood",
                    "supplier": "New England Seafood Cannery",
                },
                {
                    "id": 42,
                    "name": "Singaporean Hokkien Fried Mee",
                    "category": "Grains/Cereals",
                    "supplier": "Leka Trading",
                },
                {
                    "id": 43,
                    "name": "Ipoh Coffee",
                    "category": "Beverages",
                    "supplier": "Leka Trading",
                },
                {
                    "id": 44,
                    "name": "Gula Malacca",
                    "category": "Condiments",
                    "supplier": "Leka Trading",
                },
                {
                    "id": 45,
                    "name": "Rogede sild",
                    "category": "Seafood",
                    "supplier": "Lyngbysild",
                },
                {
                    "id": 46,
                    "name": "Spegesild",
                    "category": "Seafood",
                    "supplier": "Lyngbysild",
                },
                {
                    "id": 47,
                    "name": "Zaanse koeken",
                    "category": "Confections",
                    "supplier": "Zaanse Snoepfabriek",
                },
                {
                    "id": 48,
                    "name": "Chocolade",
                    "category": "Confections",
                    "supplier": "Zaanse Snoepfabriek",
                },
                {
                    "id": 49,
                    "name": "Maxilaku",
                    "category": "Confections",
                    "supplier": "Karkki Oy",
                },
                {
                    "id": 50,
                    "name": "Valkoinen suklaa",
                    "category": "Confections",
                    "supplier": "Karkki Oy",
                },
                {
                    "id": 51,
                    "name": "Manjimup Dried Apples",
                    "category": "Produce",
                    "supplier": "G'day, Mate",
                },
                {
                    "id": 52,
                    "name": "Filo Mix",
                    "category": "Grains/Cereals",
                    "supplier": "G'day, Mate",
                },
                {
                    "id": 53,
                    "name": "Perth Pasties",
                    "category": "Meat/Poultry",
                    "supplier": "G'day, Mate",
                },
                {
                    "id": 54,
                    "name": "Tourtire",
                    "category": "Meat/Poultry",
                    "supplier": "Ma Maison",
                },
                {
                    "id": 55,
                    "name": "Pt chinois",
                    "category": "Meat/Poultry",
                    "supplier": "Ma Maison",
                },
                {
                    "id": 56,
                    "name": "Gnocchi di nonna Alice",
                    "category": "Grains/Cereals",
                    "supplier": "Pasta Buttini s.r.l.",
                },
                {
                    "id": 57,
                    "name": "Ravioli Angelo",
                    "category": "Grains/Cereals",
                    "supplier": "Pasta Buttini s.r.l.",
                },
                {
                    "id": 58,
                    "name": "Escargots de Bourgogne",
                    "category": "Seafood",
                    "supplier": "Escargots Nouveaux",
                },
                {
                    "id": 59,
                    "name": "Raclette Courdavault",
                    "category": "Dairy Products",
                    "supplier": "Gai pturage",
                },
                {
                    "id": 60,
                    "name": "Camembert Pierrot",
                    "category": "Dairy Products",
                    "supplier": "Gai pturage",
                },
                {
                    "id": 61,
                    "name": "Sirop d'rable",
                    "category": "Condiments",
                    "supplier": "Forts d'rables",
                },
                {
                    "id": 62,
                    "name": "Tarte au sucre",
                    "category": "Confections",
                    "supplier": "Forts d'rables",
                },
                {
                    "id": 63,
                    "name": "Vegie-spread",
                    "category": "Condiments",
                    "supplier": "Pavlova, Ltd.",
                },
                {
                    "id": 64,
                    "name": "Wimmers gute Semmelkndel",
                    "category": "Grains/Cereals",
                    "supplier": "Plutzer Lebensmittelgromrkte AG",
                },
                {
                    "id": 65,
                    "name": "Louisiana Fiery Hot Pepper Sauce",
                    "category": "Condiments",
                    "supplier": "New Orleans Cajun Delights",
                },
                {
                    "id": 66,
                    "name": "Louisiana Hot Spiced Okra",
                    "category": "Condiments",
                    "supplier": "New Orleans Cajun Delights",
                },
                {
                    "id": 67,
                    "name": "Laughing Lumberjack Lager",
                    "category": "Beverages",
                    "supplier": "Bigfoot Breweries",
                },
                {
                    "id": 68,
                    "name": "Scottish Longbreads",
                    "category": "Confections",
                    "supplier": "Specialty Biscuits, Ltd.",
                },
                {
                    "id": 69,
                    "name": "Gudbrandsdalsost",
                    "category": "Dairy Products",
                    "supplier": "Norske Meierier",
                },
                {
                    "id": 70,
                    "name": "Outback Lager",
                    "category": "Beverages",
                    "supplier": "Pavlova, Ltd.",
                },
                {
                    "id": 71,
                    "name": "Flotemysost",
                    "category": "Dairy Products",
                    "supplier": "Norske Meierier",
                },
                {
                    "id": 72,
                    "name": "Mozzarella di Giovanni",
                    "category": "Dairy Products",
                    "supplier": "Formaggi Fortini s.r.l.",
                },
                {
                    "id": 73,
                    "name": "Rd Kaviar",
                    "category": "Seafood",
                    "supplier": "Svensk Sjfda AB",
                },
                {
                    "id": 74,
                    "name": "Longlife Tofu",
                    "category": "Produce",
                    "supplier": "Tokyo Traders",
                },
                {
                    "id": 75,
                    "name": "Rhnbru Klosterbier",
                    "category": "Beverages",
                    "supplier": "Plutzer Lebensmittelgromrkte AG",
                },
                {
                    "id": 76,
                    "name": "Lakkalikri",
                    "category": "Beverages",
                    "supplier": "Karkki Oy",
                },
                {
                    "id": 77,
                    "name": "Original Frankfurter grne Soe",
                    "category": "Condiments",
                    "supplier": "Plutzer Lebensmittelgromrkte AG",
                },
            ]
        }

    def test_status_code(self):
        self.assertEqual(self._response.status_code, 200)

    def test_response(self):
        self.assertEqual(
            self._response.json(),
            self._expected_response,
        )


if __name__ == "__main__":
    unittest.main()
