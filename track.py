import time
import webbrowser

try:
    import requests
except ImportError:
    print('\033[91m' + 'Error: Library "requests" not installed.' + '\033[0m')
    exit()

try:
    from termcolor import colored
except ImportError:
    print('\033[91m' + 'Error: Library "termcolor" not installed.' + '\033[0m')
    exit()

# Otra api consigue la informacion de la ip
def get_ip_info(ip_address):
    try:
        response = requests.get(f'https://ipinfo.io/{ip_address}')
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# Usa una api para conseguir la ip
def get_hostname(ip_address):
    try:
        response = requests.get(f'https://api.hackertarget.com/hostsearch/?q={ip_address}')
        data = response.text
        lines = data.split('\n')
        if len(lines) > 1:
            hostname = lines[1].split(' ')[-1]
            return hostname
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def print_ascii_art():
    print(colored(r"""
   _______             _    
  |__   __|           | |   
     | |_ __ __ _  ___| | __ 
     | |  __/ _  |/ __| |/ / 
     | | | | (_| | (__|   <  
     |_|_|  \__,_|\___|_|\_\ 
                           By pxtobr
""", 'cyan'))


# Esta es la funcion principal
def main():
    print_ascii_art()
    ip_address = input("Enter the IP address: ")
    print()
    print()
    print(colored("Processing data...", 'green'))
    time.sleep(2)
    print()
    print()
    ip_info = get_ip_info(ip_address)
    if ip_info:
        print(colored(f"IP Address: {ip_info['ip']}", 'green'))
        hostname = get_hostname(ip_info['ip'])
        if hostname:
            print(colored(f"Hostname: {hostname}", 'green'))
        else:
            print(" ")
        print(colored("City:", 'green'), colored(ip_info['city'], 'red'))
        print(colored("Region:", 'green'), colored(ip_info['region'], 'red'))
        print(colored("Country:", 'green'), colored(ip_info['country'], 'red'))
        print(colored("Country Code:", 'green'), colored(ip_info['country'], 'red'))
        print(colored("Postal Code:", 'green'), colored(ip_info['postal'], 'red'))
        print(colored("Timezone:", 'green'), colored(ip_info['timezone'], 'red'))
        lat = ip_info['loc'].split(',')[0]
        lon = ip_info['loc'].split(',')[1]
        url = f'https://www.google.com/maps/search/{lat},{lon}'
        print(colored("Google Maps:", 'green'), colored(url, 'red'))
        webbrowser.open(url)
        print(colored("-- Follow in Instagram :pxtobr", 'green'))
    else:
        print(colored("Error: Unable to retrieve IP information.", 'green'))

if __name__ == "__main__":
    main()