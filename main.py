import bs4
import requests

html = requests.get('https://github.com/SamQxd').text
soup = bs4.BeautifulSoup(html, 'lxml')

name = soup.find('h1', class_='vcard-names')
real_name = name.find('span', class_='p-name vcard-fullname d-block overflow-hidden').text.strip()
user_name = name.find('span', class_='p-nickname vcard-username d-block').text.strip()
location = soup.find('span', class_='p-label').text.strip()

profile_picture = soup.find('div', class_='position-relative d-inline-block col-2 col-md-12 mr-3 mr-md-0 flex-shrink-0').img['src']
status = soup.find('div', class_='p-note user-profile-bio mb-3 js-user-profile-bio f4').div.text
follow = soup.find_all('span', class_='text-bold color-fg-default')
follow = [i.text for i in follow]
contributions = soup.find('h2', class_='f4 text-normal mb-2').text.strip().replace('contributions', '').replace('in the last year', '')


info = {
    'Real name': real_name,
    'User name': user_name,
    'Location' : location,
    'Profile picture': profile_picture,
    'Status': status,
    'Followers': follow[0],
    'Following': follow[1],
    'Contributions in the last year': contributions
}

for i in info:
    print(f'{i}: {info[i]}')