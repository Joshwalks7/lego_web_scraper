import requests
from bs4 import BeautifulSoup
# example sets to test: 10316, 75313, 42146
#Marget only has 10366, Balmart only has 75396, Camazon only has 43251
#sets shared by only two stores: 42182 and 60442, plus 21354
def main():
    balmart_sets_dict = create_dict('https://joshwalks7.github.io/LEGO-My-Wallet/Balmart.html')
    camazon_sets_dict = create_dict('https://joshwalks7.github.io/LEGO-My-Wallet/Camazon.html')
    marget_sets_dict = create_dict('https://joshwalks7.github.io/LEGO-My-Wallet/Marget.html')
    repeat = 'yes'
    while repeat == 'yes':
        lego_set_num = get_lego_set(balmart_sets_dict, camazon_sets_dict, marget_sets_dict)
        lego_set_name = get_lego_name(lego_set_num, balmart_sets_dict, camazon_sets_dict, marget_sets_dict)
        vendor_dict = get_vendor_list(lego_set_num, balmart_sets_dict, camazon_sets_dict, marget_sets_dict)
        print(f'\nShowing results for {lego_set_num} - {lego_set_name} across {len(vendor_dict)} store(s):\n')

        #display the results in cheapest -> most expensive order
        display_prices(vendor_dict)
        repeat = input('\nWould you like to search for a new set? (yes/no) ')
        if repeat.lower() != 'yes':
            print("Good luck hunting for cheap LEGO!")

def create_dict(site_url):
    source = requests.get(site_url).text
    soup = BeautifulSoup(source, 'html.parser')
    cards = soup.find_all('article', class_='card')
    sets_dict = {}
    for card in cards:
        name = card.find('div', class_='set-name').text
        set_num = int(card.find('div', class_='meta-line').text.split('#')[1].split('|')[0].strip())
        price = float(card.find('span', class_='price').text.replace('$', ''))
        sets_dict[set_num] = name, price
    return sets_dict

def get_lego_set(dict1, dict2, dict3):
    inventory = False
    #while loop keeps program stuck until the user inputs a valid set number
    while inventory == False:
        lego_set = int(input('What is the set number for the LEGO you are looking up? '))
        #check to see if the set actually exists across the three sites
        if lego_set in dict1 or lego_set in dict2 or lego_set in dict3:
            inventory = True
            return lego_set
        else:
            print('That set number does not correspond with any set for sale across the sites\n')

def get_lego_name(set, dict1, dict2, dict3):
    #find the name of the set (it must exist in one of the three stores or else the program would have ended earlier)
    if set in dict1:
        return dict1[set][0]
    elif set in dict2:
        return dict2[set][0]
    else:
        return dict3[set][0]

def get_vendor_list(lego_set_num, balmart_sets_dict, camazon_sets_dict, marget_sets_dict):
    #create empty dict to add the stores that actually sell the product
    valid_vendors_dict = {}
    if lego_set_num in balmart_sets_dict:
        valid_vendors_dict['Balmart'] = balmart_sets_dict[lego_set_num][1]
    if lego_set_num in camazon_sets_dict:
        valid_vendors_dict['Camazon'] = camazon_sets_dict[lego_set_num][1]
    if lego_set_num in marget_sets_dict:
        valid_vendors_dict['Marget'] = marget_sets_dict[lego_set_num][1]
        #return a sorted dictionary based on the price of the item
    return dict(sorted(valid_vendors_dict.items(), key=lambda item: item[1]))

def display_prices(vendor_dict):
    #logic to handle if only one store has the set
    count = len(vendor_dict)
    if count == 1:
        for store, price in vendor_dict.items():
            print(f'Only Option: ${price} --- {store}')
        return
    #logic ot handle multiple stores having the same set at different prices
    for i, (store, price) in enumerate(vendor_dict.items()):
        if i == 0:
            print(f'Cheapest Value: ${price} --- {store}')
        elif i == len(vendor_dict) - 1:
            print(f'Most Expensive: ${price} --- {store}')
        else:
            print(f'Moderate Value: ${price} --- {store}')


if __name__ == '__main__':
       main()