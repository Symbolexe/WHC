# Creator : Yasin Saffari ( Symbolexe )
# Date :  2024/04/16
import requests
import schedule
import time
from telegram import Bot

def check_website(url, log_file, bot_info):
    try:
        response = requests.get(url, allow_redirects=True)
        if response.status_code == 200:
            log_status(log_file, url, "Alive")
        else:
            log_status(log_file, url, "Dead")
            if bot_info:
                send_telegram_message(bot_info['token'], bot_info['chat_id'], f"{url} is dead")
    except requests.exceptions.RequestException as e:
        log_status(log_file, url, "Error")
        if bot_info:
            send_telegram_message(bot_info['token'], bot_info['chat_id'], f"Error checking {url}: {e}")

def log_status(log_file, url, status):
    current_time = time.strftime("%H:%M")
    with open(log_file, "a") as f:
        f.write(f"{current_time} | [{url}] | {status}\n")

def send_telegram_message(bot_token, chat_id, message):
    bot = Bot(token=bot_token)
    bot.send_message(chat_id=chat_id, text=message)

def main():
    bot_info = None

    # Check if the user wants to use Telegram for notifications
    print("Do you want to use Telegram for notifications? (yes/no): ", end="")
    use_telegram = input().lower()
    if use_telegram == 'yes':
        print("Enter your bot token: ", end="")
        bot_token = input()
        print("Enter your chat ID: ", end="")
        chat_id = input()
        bot_info = {'token': bot_token, 'chat_id': chat_id}

    websites = []
    log_file = "website_status.log"

    # Ask the user whether they have a list of hosts or want to enter them manually
    print("Do you have a list of hosts or want to enter them manually? (list/manual): ", end="")
    input_method = input().lower()
    if input_method == 'list':
        print("Enter the name of the file containing website URLs: ", end="")
        file_name = input()
        try:
            with open(file_name, 'r') as f:
                websites.extend(f.read().splitlines())
        except FileNotFoundError:
            print("File not found. Please make sure the file exists and try again.")
            return
    elif input_method == 'manual':
        print("Please enter websites with the protocol prefix (http:// or https://)")
        while True:
            print("Enter website URL (leave empty to finish): ", end="")
            url = input()
            if not url:
                break
            websites.append(url)
    else:
        print("Invalid input. Please choose 'list' or 'manual'.")
        return

    # Inform the user about the default checking interval if not specified
    print("Enter the time interval for checking the websites in minutes (leave empty for default 5 minutes): ", end="")
    time_interval = input()
    if not time_interval:
        print("Okay, websites will be checked every 5 minutes by default.")
        schedule_interval = 5
    else:
        schedule_interval = int(time_interval)

    # Schedule checking according to the specified time interval
    for website in websites:
        check_website(website, log_file, bot_info)
        schedule.every(schedule_interval).minutes.do(check_website, website, log_file, bot_info)

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Goodbye")

if __name__ == "__main__":
    main()
