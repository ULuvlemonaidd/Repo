import time
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    clear_screen()
    print("Made by: Lemonaidd")
    print(r"""
   ██████╗ ███████╗██████╗  ██████╗        
   ██╔══██╗██╔════╝██╔══██╗██╔═══██╗       
   ██████╔╝█████╗  ██████╔╝██║   ██║       
   ██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║       
   ██║  ██║███████╗██║     ╚██████╔╝       
   ╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝        
    """)
    print("---Spam Report Bot---")
    print("1. Snapchat  Report")
    print("2. VRChat  Report")
    print("3. TikTok  Report")
    print("4. Instagram  Report")
    print("5. Exit")

def connect_to_proxy():
    print("Connecting to proxy...")
    time.sleep(2)
    proxy_provider = random.choice(["Zyte", "Oxylabs", "Fineproxies", " IPRoyal", "WebShare","SOAX","PCMag","Proxyway","Netnut","Oculus Proxies","ayobyte","Smartproxies","toolip"])
    print(f"Connected to {proxy_provider} !")

def generate_report_id():
    return random.randint(100000, 999999)

def spam_report(platform, username, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        report_id = generate_report_id()
        print(f"Generating Report for '{username}'... ")
        time.sleep(random.uniform(0.1, 1.5))
        if random.choice([True, False]):
            print(f"Report sent! Report ID: {report_id}")
        else:
            print("Failed to send report.")
        time.sleep(1)

def main():
    while True:
        print_menu()
        choice = input("Select an option: ")
        if choice == '5':
            break
        elif choice in ['1', '2', '3','4']:
            platform = ["Snapchat", "VRChat", "TikTok", "Instagram"][int(choice) - 1]
            username = input("Enter username: ")
            duration = int(input("Enter duration in seconds: "))
            connect_to_proxy()
            spam_report(platform, username, duration)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
