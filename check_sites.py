import requests
from datetime import datetime
import time
# from sms import both

sites = [
    {"url": "https://TestSite1.com/", "wp_url": "https://TestSite1.com/login/"},
    {"url": "https://TestSite2.com/", "wp_url": "https://TestSite2.com/login/"},
    {"url": "https://TestSite3.com/", "wp_url": "https://TestSite3.com/login/"},
    {"url": "https://TestSite4.com/", "wp_url": "https://TestSite4.com/login/"},
    {"url": "https://TestSite5.com/", "wp_url": "https://TestSite5.com/wp-login.php"},
]

def notify_error(message): #telegramBot
    TOKEN = 'yourToken'
    CHAT_ID = 'yourChatID'
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    params = {'chat_id': CHAT_ID, 'text': message}
    requests.post(url, params=params)

def save_log(log):
    with open('log.txt', 'a') as log_file:
        log_file.write(log + '\n')
    
def check_sites():
    for site in sites:
        try:
            response = requests.get(site["url"])
            if response.status_code == 200:
                print(f"{site['url']} is OK - {datetime.now()}")
                save_log(f"{site['url']} is OK - {datetime.now()}")
            else:
                print(f"{site['url']} is down! - {datetime.now()}")
                save_log(f"{site['url']} is down! - {datetime.now()}")
                notify_error(f"{site['url']} is down! - {datetime.now()}")
                # both('99999999')
            
            wp_response = requests.get(site["wp_url"])
            if "Remember" in wp_response.text or 'بسپار' in wp_response.text:
                print(f"{site['url']} WordPress is OK - {datetime.now()}")
                save_log(f"{site['url']} WordPress is OK - {datetime.now()}")
            else:
                print(f"{site['url']} WordPress is not loaded properly! - {datetime.now()}")
                save_log(f"{site['url']} WordPress is not loaded properly! - {datetime.now()}")
                notify_error(f"{site['url']} WordPress is not loaded properly! - {datetime.now()}")
                # both('99999999')
                
        except Exception as e:
            print(f"Error checking {site['url']}: {e} - {datetime.now()}")

while True:
    check_sites()
    time.sleep(3600)