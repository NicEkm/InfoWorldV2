import requests                     
from io import BytesIO 


main_api = 'https://restcountries.eu/rest/v2/name/'
flag_api = 'https://www.countryflags.io/'

class Infoworld:
    def __init__(self):
        pass

    def get_country_information(self, country):
        country_info, country_code = self.get_data(country)
        return country_info, country_code
    
    def get_data(self, country):
        try:
            url = main_api + country
            json_data = requests.get(url).json()
            response = json_data
        except Exception as e:
            message =  e
            full_dict = {
                'error':message
            }
            country_code = ''
            return full_dict, country_code
        try:
            name = (response[0]['name'])
            capital = (response[0]['capital'])
            currency_name = (response[0]['currencies'][0]['name'])
            currency_symbol = (response[0]['currencies'][0]['symbol'])
            borders = (response[0]['borders'])
            country_code = (response[0]['alpha2Code']) 
            borderlist = [] 
            borderlist2 = [] 
            borderlist3 = []

            population = (response[0]['population']) 
             
            for x in borders:
                borderlist.append(x)

            if 11 > len(borderlist) >= 9:
                border_length = str(len(borderlist))
                borderlist2 = borderlist[:5].copy()
                borderlist3 = borderlist[5:].copy()
                borderlist2 = ', '.join(map(str, borderlist2)) 
                borderlist3 = ', '.join(map(str, borderlist3)) 
    

            if 13 > len(borderlist) > 11:
                border_length = str(len(borderlist))
                borderlist2 = borderlist[:6].copy()
                borderlist3 = borderlist[6:].copy()
                borderlist2 = ', '.join(map(str, borderlist2)) #
                borderlist3 = ', '.join(map(str, borderlist3)) #
            
            
            if 20 > len(borderlist) > 13:
                border_length = str(len(borderlist))
                borderlist2 = borderlist[:7].copy()
                borderlist3 = borderlist[7:].copy()
                borderlist2 = ', '.join(map(str, borderlist2)) #
                borderlist3 = ', '.join(map(str, borderlist3)) #
            
                    
            if len(borderlist) <= 8:
                border_length = str(len(borderlist))
                borderlist2 = borderlist[:8].copy()
                borderlist2 = ', '.join(map(str, borderlist)) #
                borderlist3 = '' 
                
            full_dict = {
                'name':name,
                'capital':capital,
                'population':population,
                'currency_name':currency_name,
                'currency_symbol':currency_symbol,
                'border_length':border_length,
                'few_borders':borderlist2,
                'many_borders':borderlist3,
                'error':'',
            } 
        
        except Exception as e: 
            message = e
            full_dict = {
                'error':message
            }
            country_code = ''
            return full_dict, country_code
    
        return full_dict, country_code 

    
    