

api_key = "asdasdasdasda5465as4d6a5s4d65as";
server_url = "https://pawanvikasitha.pythonanywhere.com/";


#setting up the webhook - place this code under the def main()-> none
updater.start_webhook(listen="0.0.0.0",
                      port=int(PORT),
                      url_path=api_key)
updater.bot.setWebhook(server_url_with_https,api_key)
