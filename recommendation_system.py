import os 
import telebot  
from rembg import remove
from colourconverter import File_ColorConverter
from ktrees import similiar_shoes
from config import bot_key


bot = telebot.TeleBot(bot_key)

def process_single_image(input_image):
    output_data = remove(input_image)

    return output_data
    
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I'm YourNikeShoe and I'll recommend other shoes that look just like me! Please insert a picture of any shoe.")


@bot.message_handler(content_types=['photo'])
def handle_image(message):  
    bot.reply_to(message, "Thanks for inserting a picture of your shoe! Give me a while to find you shoes you might like... " )
    photo = message.photo[-1]
    bot.reply_to(message, "this works")
    file_id = photo.file_id

    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    
    processed_image = process_single_image(downloaded_file)
    
    file_converter = File_ColorConverter(processed_image)
    colours = file_converter.get_most_prevalent_colors()
    shoes = similiar_shoes(colours)

    

    for shoe in shoes:
        shoe_name, shoe_link = shoe
        message_text = f"Shoe Name: {shoe_name}\nShoe Link: {shoe_link}"
        bot.reply_to(message, message_text)

    # Send the processed image back to the user

    # rework background remover   
      
bot.infinity_polling()


# need to add a case whereby colours repeat -> ['Outer Space', 'Mercury', 'Quick Silver', 'Quick Silver'] green shoes
# pwoershell to activate this go look chatgpt

#RUN THIS FIRST! 
#$env:BOT_TOKEN = "6710869427:AAEFSNYrbp4iNJ5nLHBDoRS6FFm4EqbzhbE"
