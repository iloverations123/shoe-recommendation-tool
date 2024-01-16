import requests
import json
from colourconverter import ColorConverter

list_of_urls = [
'https://api.nike.com/cic/browse/v2?queryid=products&anonymousId=D0DB784C9A8B487218629163868C5928&country=sg&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(SG)%26filter%3Dlanguage(en-GB)%26filter%3DemployeePrice(true)%26filter%3DattributeIds(0f64ecc7-d624-4e91-b171-b83a03dd8550%2C16633190-45e5-4830-a068-232ac7aea82c%2C193af413-39b0-4d7e-ae34-558821381d3f)%26anchor%3D24%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D24&language=en-GB&localizedRangeStr=%7BlowestPrice%7D%E2%80%94%7BhighestPrice%7D',
'https://api.nike.com/cic/browse/v2?queryid=products&anonymousId=D0DB784C9A8B487218629163868C5928&country=sg&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(SG)%26filter%3Dlanguage(en-GB)%26filter%3DemployeePrice(true)%26filter%3DattributeIds(0f64ecc7-d624-4e91-b171-b83a03dd8550%2C16633190-45e5-4830-a068-232ac7aea82c%2C193af413-39b0-4d7e-ae34-558821381d3f)%26anchor%3D48%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D24&language=en-GB&localizedRangeStr=%7BlowestPrice%7D%E2%80%94%7BhighestPrice%7D',
'https://api.nike.com/cic/browse/v2?queryid=products&anonymousId=D0DB784C9A8B487218629163868C5928&country=sg&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(SG)%26filter%3Dlanguage(en-GB)%26filter%3DemployeePrice(true)%26filter%3DattributeIds(0f64ecc7-d624-4e91-b171-b83a03dd8550%2C16633190-45e5-4830-a068-232ac7aea82c%2C193af413-39b0-4d7e-ae34-558821381d3f)%26anchor%3D72%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D24&language=en-GB&localizedRangeStr=%7BlowestPrice%7D%E2%80%94%7BhighestPrice%7D',
'https://api.nike.com/cic/browse/v2?queryid=products&anonymousId=D0DB784C9A8B487218629163868C5928&country=sg&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(SG)%26filter%3Dlanguage(en-GB)%26filter%3DemployeePrice(true)%26filter%3DattributeIds(0f64ecc7-d624-4e91-b171-b83a03dd8550%2C16633190-45e5-4830-a068-232ac7aea82c%2C193af413-39b0-4d7e-ae34-558821381d3f)%26anchor%3D96%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D24&language=en-GB&localizedRangeStr=%7BlowestPrice%7D%E2%80%94%7BhighestPrice%7D',
'https://api.nike.com/cic/browse/v2?queryid=products&anonymousId=D0DB784C9A8B487218629163868C5928&country=sg&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(SG)%26filter%3Dlanguage(en-GB)%26filter%3DemployeePrice(true)%26filter%3DattributeIds(0f64ecc7-d624-4e91-b171-b83a03dd8550%2C16633190-45e5-4830-a068-232ac7aea82c%2C193af413-39b0-4d7e-ae34-558821381d3f)%26anchor%3D120%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D24&language=en-GB&localizedRangeStr=%7BlowestPrice%7D%E2%80%94%7BhighestPrice%7D',
'https://api.nike.com/cic/browse/v2?queryid=products&anonymousId=D0DB784C9A8B487218629163868C5928&country=sg&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(SG)%26filter%3Dlanguage(en-GB)%26filter%3DemployeePrice(true)%26filter%3DattributeIds(0f64ecc7-d624-4e91-b171-b83a03dd8550%2C16633190-45e5-4830-a068-232ac7aea82c%2C193af413-39b0-4d7e-ae34-558821381d3f)%26anchor%3D144%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D24&language=en-GB&localizedRangeStr=%7BlowestPrice%7D%E2%80%94%7BhighestPrice%7D',
'https://api.nike.com/cic/browse/v2?queryid=products&anonymousId=D0DB784C9A8B487218629163868C5928&country=sg&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(SG)%26filter%3Dlanguage(en-GB)%26filter%3DemployeePrice(true)%26filter%3DattributeIds(0f64ecc7-d624-4e91-b171-b83a03dd8550%2C16633190-45e5-4830-a068-232ac7aea82c%2C193af413-39b0-4d7e-ae34-558821381d3f)%26anchor%3D168%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D24&language=en-GB&localizedRangeStr=%7BlowestPrice%7D%E2%80%94%7BhighestPrice%7D',
'https://api.nike.com/cic/browse/v2?queryid=products&anonymousId=D0DB784C9A8B487218629163868C5928&country=sg&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(SG)%26filter%3Dlanguage(en-GB)%26filter%3DemployeePrice(true)%26filter%3DattributeIds(0f64ecc7-d624-4e91-b171-b83a03dd8550%2C16633190-45e5-4830-a068-232ac7aea82c%2C193af413-39b0-4d7e-ae34-558821381d3f)%26anchor%3D192%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D24&language=en-GB&localizedRangeStr=%7BlowestPrice%7D%E2%80%94%7BhighestPrice%7D',
'https://api.nike.com/cic/browse/v2?queryid=products&anonymousId=D0DB784C9A8B487218629163868C5928&country=sg&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(SG)%26filter%3Dlanguage(en-GB)%26filter%3DemployeePrice(true)%26filter%3DattributeIds(0f64ecc7-d624-4e91-b171-b83a03dd8550%2C16633190-45e5-4830-a068-232ac7aea82c%2C193af413-39b0-4d7e-ae34-558821381d3f)%26anchor%3D216%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D24&language=en-GB&localizedRangeStr=%7BlowestPrice%7D%E2%80%94%7BhighestPrice%7D',
'https://api.nike.com/cic/browse/v2?queryid=products&anonymousId=D0DB784C9A8B487218629163868C5928&country=sg&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(SG)%26filter%3Dlanguage(en-GB)%26filter%3DemployeePrice(true)%26filter%3DattributeIds(0f64ecc7-d624-4e91-b171-b83a03dd8550%2C16633190-45e5-4830-a068-232ac7aea82c%2C193af413-39b0-4d7e-ae34-558821381d3f)%26anchor%3D240%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D24&language=en-GB&localizedRangeStr=%7BlowestPrice%7D%E2%80%94%7BhighestPrice%7D'
]


" ok why use image detection? insert multiple photos and find common colour scheme + convenience of not inputting what are ur favourite colours"
"ok wait this is how iw my code to work: the user puts in an image of a shoe and the code gives back 3 recommendations"
"if the user doesnt like the choices, can choose to reroll so dont give them a whole list of shoes "
"sort out all the shoes on nike to their colour schemes "


# things to do:

"see if i can get more shoes rescrape the api and then use the get_updated function"

# for the colour schemes, use the ones listed by chatgpt but go search up what it means for the colours to belong there. do this first
"monochormatic --> involves only one colour but different shades of it"
"complementary --> colours that go well together"
"pastel --> colours that are bright and have no black / darkness"



# rescrape nikes website to see if i get more results possibly

# for the shoe colour analyser, make it detect more general colour combinations -> cause we can then use combinations() to classify the colours into their respective colour schemes


# image cropper to identify the shoe instead of the background

nike_dict = {}
def process_multiple_urls(urls):
    nike_dicts = []  # use a temporary list to store all the shoes found from url
    nike_dicts_2 = []

    for url in urls:
        html = requests.get(url=url)
        output = json.loads(html.text)
       # get a list of urls for the pictures 


        
        

        for product in output['data']['products']['products']: # product here refers to the 0-23 shoes and it iterates through every item
            colours_list = [] # list should be here so it resets the colours of a shoe
            shoes_url_link = []
           
            

            if "Men's" in product['subtitle']:
                current_dict_list = [{"Shoe Name": product['title'], "Colour": colours_list, "Shoe Urls": shoes_url_link}]
                nike_dicts.extend(current_dict_list)

                for colours in product['colorways']: # this essentially gathers all the colours that the shoe offer like if there are colours -> accesses colours1 and colours2
                    shoes_url_link.append(colours['images']['portraitURL']) # redo the api link list
                    colors = ColorConverter(colours['images']['portraitURL'])
                    all_colors = colors.get_all_colours()
                    colours_list.append(all_colors)
                     
                # prints only when one shoe of all colour variations is completed refer to colourconverter.py
                # ok nice now it works
            
                


            elif "Women" in product['subtitle']:
                current_dict_list_2 = [{"Shoe Name": product['title'], "Colour": colours_list, "Type of shoe": product['subtitle']}]
                nike_dicts_2.extend(current_dict_list_2)

                for colours in product['colorways']: # this essentially gathers all the colours that the shoe offer like if there are colours -> accesses colours1 and colours2
                    colours_list.append(colours['colorDescription'])

            else:
                pass
                

        # this gets all the dictionary-like inputs and puts them in a list. 
        
    final_dict = {index: current_dict for index, current_dict in enumerate(nike_dicts)} # this is for the men
    final_dict_2 = {index1: current_dict1 for index1, current_dict1 in enumerate(nike_dicts_2)} # this is for the women
    # this essentially uses enumerate function in this manner e.g. (0, {shoe name:, colour:,})
    
    print(final_dict)

  

# Call the function
process_multiple_urls(list_of_urls)


