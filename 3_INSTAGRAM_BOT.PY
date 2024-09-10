from instabot import Bot
bot = Bot()
bot.login(username="here you have to give username" password = "Here password has to be provided")
bot.follow("Username")
bot.upload_photo("URL of the pic from the device by making the orientation of the slashes in the opposite direction", caption="Your caption")
bot.send_message("Your message",["username1","username2"])
followers = bot.get_user_followers("username")
for follower in followers:
    print(bot.get_user_info(follower))

following = bot.get_user_following("username")
for follower in following:
    print(bot.get_user_info(follower))
