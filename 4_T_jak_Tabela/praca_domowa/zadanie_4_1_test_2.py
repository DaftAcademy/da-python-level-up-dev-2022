import unittest
import urllib.parse

import requests

from file import AppClass


class CodingRoomsUnitTests(unittest.TestCase):
    def setUp(self):
        get_path = urllib.parse.urljoin(AppClass.APP_URL, "/customers")
        self._response = requests.get(get_path)
        self._expected_response = {
            "customers": [
                {
                    "id": "ALFKI",
                    "name": "Alfreds Futterkiste",
                    "full_address": "Obere Str. 57 12209 Berlin Germany",
                },
                {
                    "id": "ANATR",
                    "name": "Ana Trujillo Emparedados y helados",
                    "full_address": "Avda. de la Constitucin 2222 05021 Mxico D.F. Mexico",
                },
                {
                    "id": "ANTON",
                    "name": "Antonio Moreno Taquera",
                    "full_address": "Mataderos  2312 05023 Mxico D.F. Mexico",
                },
                {
                    "id": "AROUT",
                    "name": "Around the Horn",
                    "full_address": "120 Hanover Sq. WA1 1DP London UK",
                },
                {
                    "id": "BERGS",
                    "name": "Berglunds snabbkp",
                    "full_address": "Berguvsvgen  8 S-958 22 Lule Sweden",
                },
                {
                    "id": "BLAUS",
                    "name": "Blauer See Delikatessen",
                    "full_address": "Forsterstr. 57 68306 Mannheim Germany",
                },
                {
                    "id": "BLONP",
                    "name": "Blondesddsl pre et fils",
                    "full_address": "24, place Klber 67000 Strasbourg France",
                },
                {
                    "id": "BOLID",
                    "name": "Blido Comidas preparadas",
                    "full_address": "C/ Araquil, 67 28023 Madrid Spain",
                },
                {
                    "id": "BONAP",
                    "name": "Bon app'",
                    "full_address": "12, rue des Bouchers 13008 Marseille France",
                },
                {
                    "id": "BOTTM",
                    "name": "Bottom-Dollar Markets",
                    "full_address": "23 Tsawassen Blvd. T2F 8M4 Tsawassen Canada",
                },
                {
                    "id": "BSBEV",
                    "name": "B's Beverages",
                    "full_address": "Fauntleroy Circus EC2 5NT London UK",
                },
                {
                    "id": "CACTU",
                    "name": "Cactus Comidas para llevar",
                    "full_address": "Cerrito 333 1010 Buenos Aires Argentina",
                },
                {
                    "id": "CENTC",
                    "name": "Centro comercial Moctezuma",
                    "full_address": "Sierras de Granada 9993 05022 Mxico D.F. Mexico",
                },
                {
                    "id": "CHOPS",
                    "name": "Chop-suey Chinese",
                    "full_address": "Hauptstr. 29 3012 Bern Switzerland",
                },
                {
                    "id": "COMMI",
                    "name": "Comrcio Mineiro",
                    "full_address": "Av. dos Lusadas, 23 05432-043 Sao Paulo Brazil",
                },
                {
                    "id": "CONSH",
                    "name": "Consolidated Holdings",
                    "full_address": "Berkeley Gardens 12  Brewery WX1 6LT London UK",
                },
                {
                    "id": "DRACD",
                    "name": "Drachenblut Delikatessen",
                    "full_address": "Walserweg 21 52066 Aachen Germany",
                },
                {
                    "id": "DUMON",
                    "name": "Du monde entier",
                    "full_address": "67, rue des Cinquante Otages 44000 Nantes France",
                },
                {
                    "id": "EASTC",
                    "name": "Eastern Connection",
                    "full_address": "35 King George WX3 6FW London UK",
                },
                {
                    "id": "ERNSH",
                    "name": "Ernst Handel",
                    "full_address": "Kirchgasse 6 8010 Graz Austria",
                },
                {
                    "id": "FAMIA",
                    "name": "Familia Arquibaldo",
                    "full_address": "Rua Ors, 92 05442-030 Sao Paulo Brazil",
                },
                {
                    "id": "FISSA",
                    "name": "FISSA Fabrica Inter. Salchichas S.A.",
                    "full_address": "C/ Moralzarzal, 86 28034 Madrid Spain",
                },
                {
                    "id": "FOLIG",
                    "name": "Folies gourmandes",
                    "full_address": "184, chausse de Tournai 59000 Lille France",
                },
                {
                    "id": "FOLKO",
                    "name": "Folk och f HB",
                    "full_address": "kergatan 24 S-844 67 Brcke Sweden",
                },
                {
                    "id": "FRANK",
                    "name": "Frankenversand",
                    "full_address": "Berliner Platz 43 80805 Mnchen Germany",
                },
                {
                    "id": "FRANR",
                    "name": "France restauration",
                    "full_address": "54, rue Royale 44000 Nantes France",
                },
                {
                    "id": "FRANS",
                    "name": "Franchi S.p.A.",
                    "full_address": "Via Monte Bianco 34 10100 Torino Italy",
                },
                {
                    "id": "FURIB",
                    "name": "Furia Bacalhau e Frutos do Mar",
                    "full_address": "Jardim das rosas n. 32 1675 Lisboa Portugal",
                },
                {
                    "id": "GALED",
                    "name": "Galera del gastrnomo",
                    "full_address": "Rambla de Catalua, 23 08022 Barcelona Spain",
                },
                {
                    "id": "GODOS",
                    "name": "Godos Cocina Tpica",
                    "full_address": "C/ Romero, 33 41101 Sevilla Spain",
                },
                {
                    "id": "GOURL",
                    "name": "Gourmet Lanchonetes",
                    "full_address": "Av. Brasil, 442 04876-786 Campinas Brazil",
                },
                {
                    "id": "GREAL",
                    "name": "Great Lakes Food Market",
                    "full_address": "2732 Baker Blvd. 97403 Eugene USA",
                },
                {
                    "id": "GROSR",
                    "name": "GROSELLA-Restaurante",
                    "full_address": "5 Ave. Los Palos Grandes 1081 Caracas Venezuela",
                },
                {
                    "id": "HANAR",
                    "name": "Hanari Carnes",
                    "full_address": "Rua do Pao, 67 05454-876 Rio de Janeiro Brazil",
                },
                {
                    "id": "HILAA",
                    "name": "HILARION-Abastos",
                    "full_address": "Carrera 22 con Ave. Carlos Soublette #8-35 5022 San Cristbal Venezuela",
                },
                {
                    "id": "HUNGC",
                    "name": "Hungry Coyote Import Store",
                    "full_address": "City Center Plaza 516 Main St. 97827 Elgin USA",
                },
                {
                    "id": "HUNGO",
                    "name": "Hungry Owl All-Night Grocers",
                    "full_address": None,
                },
                {
                    "id": "ISLAT",
                    "name": "Island Trading",
                    "full_address": "Garden House Crowther Way PO31 7PJ Cowes UK",
                },
                {
                    "id": "KOENE",
                    "name": "Kniglich Essen",
                    "full_address": "Maubelstr. 90 14776 Brandenburg Germany",
                },
                {
                    "id": "LACOR",
                    "name": "La corne d'abondance",
                    "full_address": "67, avenue de l'Europe 78000 Versailles France",
                },
                {
                    "id": "LAMAI",
                    "name": "La maison d'Asie",
                    "full_address": "1 rue Alsace-Lorraine 31000 Toulouse France",
                },
                {
                    "id": "LAUGB",
                    "name": "Laughing Bacchus Wine Cellars",
                    "full_address": "1900 Oak St. V3F 2K1 Vancouver Canada",
                },
                {
                    "id": "LAZYK",
                    "name": "Lazy K Kountry Store",
                    "full_address": "12 Orchestra Terrace 99362 Walla Walla USA",
                },
                {
                    "id": "LEHMS",
                    "name": "Lehmanns Marktstand",
                    "full_address": "Magazinweg 7 60528 Frankfurt a.M. Germany",
                },
                {
                    "id": "LETSS",
                    "name": "Let's Stop N Shop",
                    "full_address": "87 Polk St. Suite 5 94117 San Francisco USA",
                },
                {
                    "id": "LILAS",
                    "name": "LILA-Supermercado",
                    "full_address": "Carrera 52 con Ave. Bolvar #65-98 Llano Largo 3508 Barquisimeto Venezuela",
                },
                {
                    "id": "LINOD",
                    "name": "LINO-Delicateses",
                    "full_address": "Ave. 5 de Mayo Porlamar 4980 I. de Margarita Venezuela",
                },
                {
                    "id": "LONEP",
                    "name": "Lonesome Pine Restaurant",
                    "full_address": "89 Chiaroscuro Rd. 97219 Portland USA",
                },
                {
                    "id": "MAGAA",
                    "name": "Magazzini Alimentari Riuniti",
                    "full_address": "Via Ludovico il Moro 22 24100 Bergamo Italy",
                },
                {
                    "id": "MAISD",
                    "name": "Maison Dewey",
                    "full_address": "Rue Joseph-Bens 532 B-1180 Bruxelles Belgium",
                },
                {
                    "id": "MEREP",
                    "name": "Mre Paillarde",
                    "full_address": "43 rue St. Laurent H1J 1C3 Montral Canada",
                },
                {
                    "id": "MORGK",
                    "name": "Morgenstern Gesundkost",
                    "full_address": "Heerstr. 22 04179 Leipzig Germany",
                },
                {
                    "id": "NORTS",
                    "name": "North/South",
                    "full_address": "South House 300 Queensbridge SW7 1RZ London UK",
                },
                {
                    "id": "OCEAN",
                    "name": "Ocano Atlntico Ltda.",
                    "full_address": "Ing. Gustavo Moncada 8585 Piso 20-A 1010 Buenos Aires Argentina",
                },
                {
                    "id": "OLDWO",
                    "name": "Old World Delicatessen",
                    "full_address": "2743 Bering St. 99508 Anchorage USA",
                },
                {
                    "id": "OTTIK",
                    "name": "Ottilies Kseladen",
                    "full_address": "Mehrheimerstr. 369 50739 Kln Germany",
                },
                {
                    "id": "PARIS",
                    "name": "Paris spcialits",
                    "full_address": "265, boulevard Charonne 75012 Paris France",
                },
                {
                    "id": "PERIC",
                    "name": "Pericles Comidas clsicas",
                    "full_address": "Calle Dr. Jorge Cash 321 05033 Mxico D.F. Mexico",
                },
                {
                    "id": "PICCO",
                    "name": "Piccolo und mehr",
                    "full_address": "Geislweg 14 5020 Salzburg Austria",
                },
                {
                    "id": "PRINI",
                    "name": "Princesa Isabel Vinhos",
                    "full_address": "Estrada da sade n. 58 1756 Lisboa Portugal",
                },
                {
                    "id": "QUEDE",
                    "name": "Que Delcia",
                    "full_address": "Rua da Panificadora, 12 02389-673 Rio de Janeiro Brazil",
                },
                {
                    "id": "QUEEN",
                    "name": "Queen Cozinha",
                    "full_address": "Alameda dos Canrios, 891 05487-020 Sao Paulo Brazil",
                },
                {
                    "id": "QUICK",
                    "name": "QUICK-Stop",
                    "full_address": "Taucherstrae 10 01307 Cunewalde Germany",
                },
                {
                    "id": "RANCH",
                    "name": "Rancho grande",
                    "full_address": "Av. del Libertador 900 1010 Buenos Aires Argentina",
                },
                {
                    "id": "RATTC",
                    "name": "Rattlesnake Canyon Grocery",
                    "full_address": "2817 Milton Dr. 87110 Albuquerque USA",
                },
                {
                    "id": "REGGC",
                    "name": "Reggiani Caseifici",
                    "full_address": "Strada Provinciale 124 42100 Reggio Emilia Italy",
                },
                {
                    "id": "RICAR",
                    "name": "Ricardo Adocicados",
                    "full_address": "Av. Copacabana, 267 02389-890 Rio de Janeiro Brazil",
                },
                {
                    "id": "RICSU",
                    "name": "Richter Supermarkt",
                    "full_address": "Grenzacherweg 237 1203 Genve Switzerland",
                },
                {
                    "id": "ROMEY",
                    "name": "Romero y tomillo",
                    "full_address": "Gran Va, 1 28001 Madrid Spain",
                },
                {
                    "id": "SANTG",
                    "name": "Sant Gourmet",
                    "full_address": "Erling Skakkes gate 78 4110 Stavern Norway",
                },
                {
                    "id": "SAVEA",
                    "name": "Save-a-lot Markets",
                    "full_address": "187 Suffolk Ln. 83720 Boise USA",
                },
                {
                    "id": "SEVES",
                    "name": "Seven Seas Imports",
                    "full_address": "90 Wadhurst Rd. OX15 4NB London UK",
                },
                {
                    "id": "SIMOB",
                    "name": "Simons bistro",
                    "full_address": "Vinbltet 34 1734 Kobenhavn Denmark",
                },
                {
                    "id": "SPECD",
                    "name": "Spcialits du monde",
                    "full_address": "25, rue Lauriston 75016 Paris France",
                },
                {
                    "id": "SPLIR",
                    "name": "Split Rail Beer & Ale",
                    "full_address": "P.O. Box 555 82520 Lander USA",
                },
                {
                    "id": "SUPRD",
                    "name": "Suprmes dlices",
                    "full_address": "Boulevard Tirou, 255 B-6000 Charleroi Belgium",
                },
                {
                    "id": "THEBI",
                    "name": "The Big Cheese",
                    "full_address": "89 Jefferson Way Suite 2 97201 Portland USA",
                },
                {
                    "id": "THECR",
                    "name": "The Cracker Box",
                    "full_address": "55 Grizzly Peak Rd. 59801 Butte USA",
                },
                {
                    "id": "TOMSP",
                    "name": "Toms Spezialitten",
                    "full_address": "Luisenstr. 48 44087 Mnster Germany",
                },
                {
                    "id": "TORTU",
                    "name": "Tortuga Restaurante",
                    "full_address": "Avda. Azteca 123 05033 Mxico D.F. Mexico",
                },
                {
                    "id": "TRADH",
                    "name": "Tradio Hipermercados",
                    "full_address": "Av. Ins de Castro, 414 05634-030 Sao Paulo Brazil",
                },
                {
                    "id": "TRAIH",
                    "name": "Trail's Head Gourmet Provisioners",
                    "full_address": "722 DaVinci Blvd. 98034 Kirkland USA",
                },
                {
                    "id": "VAFFE",
                    "name": "Vaffeljernet",
                    "full_address": "Smagsloget 45 8200 rhus Denmark",
                },
                {"id": "Val2 ", "name": "IT", "full_address": None},
                {"id": "VALON", "name": "IT", "full_address": None},
                {
                    "id": "VICTE",
                    "name": "Victuailles en stock",
                    "full_address": "2, rue du Commerce 69004 Lyon France",
                },
                {
                    "id": "VINET",
                    "name": "Vins et alcools Chevalier",
                    "full_address": "59 rue de l'Abbaye 51100 Reims France",
                },
                {
                    "id": "WANDK",
                    "name": "Die Wandernde Kuh",
                    "full_address": "Adenauerallee 900 70563 Stuttgart Germany",
                },
                {
                    "id": "WARTH",
                    "name": "Wartian Herkku",
                    "full_address": "Torikatu 38 90110 Oulu Finland",
                },
                {
                    "id": "WELLI",
                    "name": "Wellington Importadora",
                    "full_address": "Rua do Mercado, 12 08737-363 Resende Brazil",
                },
                {
                    "id": "WHITC",
                    "name": "White Clover Markets",
                    "full_address": "305 - 14th Ave. S. Suite 3B 98128 Seattle USA",
                },
                {
                    "id": "WILMK",
                    "name": "Wilman Kala",
                    "full_address": "Keskuskatu 45 21240 Helsinki Finland",
                },
                {
                    "id": "WOLZA",
                    "name": "Wolski  Zajazd",
                    "full_address": "ul. Filtrowa 68 01-012 Warszawa Poland",
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
