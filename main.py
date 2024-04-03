import os
import uuid
import sys
import requests
import json
from concurrent.futures import ThreadPoolExecutor
from PIL import Image
from io import BytesIO
import urllib.parse


def print_stylish_big(name):
    print(name)

def generate_unique_token():
    token = uuid.uuid4().hex
    return token

def download_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BytesIO(response.content)

def download_images(image_urls):
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(download_image, url) for url in image_urls]
        images = [future.result() for future in futures if future.result()]
    return images


def convert_images_to_pdf(images, output_folder):
    pdf_images = []
    for idx, image in enumerate(images):
        img = Image.open(image)
        pdf_images.append(img)
        unique_token = generate_unique_token()
        print(f"Pdf Downlaoding Process.....")
    output_file = os.path.join(output_folder, f"{unique_token}.pdf")
    print(f"Downloaded here : {output_file} ")
    pdf_images[0].save(output_file, save_all=True, append_images=pdf_images[1:])

def downlaod_issuu_pdf(last_part,fourth_part):
    url = f"https://reader3.isu.pub/{fourth_part}/{last_part}/reader3_4.json"

    payload = {}
    headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ru;q=0.8,zh-TW;q=0.7,zh;q=0.6',
    'dnt': '1',
    'origin': 'https://issuu.com',
    'referer': 'https://issuu.com/',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print(f"Response Status:{response.status_code}" )
    if response.status_code == 200:
        data = json.loads(response.text)
        image_urls = [f"https://{page['imageUri']}" for page in data['document']['pages']]  # Add "https://" prefix here
        print(f"Downloaded image URLs: {image_urls}")
        images = download_images(image_urls)
        
        output_folder = "output_folder"
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        convert_images_to_pdf(images, output_folder)


if __name__ == "__main__":
    name ="""
                                                                                                              
                                                                                                          
NNNNNNNN        NNNNNNNXXXXXXX       XXXXXXX     PPPPPPPPPPPPPPPPP  RRRRRRRRRRRRRRRRR       OOOOOOOOO     
N:::::::N       N::::::X:::::X       X:::::X     P::::::::::::::::P R::::::::::::::::R    OO:::::::::OO   
N::::::::N      N::::::X:::::X       X:::::X     P::::::PPPPPP:::::PR::::::RRRRRR:::::R OO:::::::::::::OO 
N:::::::::N     N::::::X::::::X     X::::::X     PP:::::P     P:::::RR:::::R     R:::::O:::::::OOO:::::::O
N::::::::::N    N::::::XXX:::::X   X:::::XXX       P::::P     P:::::P R::::R     R:::::O::::::O   O::::::O
N:::::::::::N   N::::::N  X:::::X X:::::X          P::::P     P:::::P R::::R     R:::::O:::::O     O:::::O
N:::::::N::::N  N::::::N   X:::::X:::::X           P::::PPPPPP:::::P  R::::RRRRRR:::::RO:::::O     O:::::O
N::::::N N::::N N::::::N    X:::::::::X            P:::::::::::::PP   R:::::::::::::RR O:::::O     O:::::O
N::::::N  N::::N:::::::N    X:::::::::X            P::::PPPPPPPPP     R::::RRRRRR:::::RO:::::O     O:::::O
N::::::N   N:::::::::::N   X:::::X:::::X           P::::P             R::::R     R:::::O:::::O     O:::::O
N::::::N    N::::::::::N  X:::::X X:::::X          P::::P             R::::R     R:::::O:::::O     O:::::O
N::::::N     N:::::::::XXX:::::X   X:::::XXX       P::::P             R::::R     R:::::O::::::O   O::::::O
N::::::N      N::::::::X::::::X     X::::::X     PP::::::PP         RR:::::R     R:::::O:::::::OOO:::::::O
N::::::N       N:::::::X:::::X       X:::::X     P::::::::P         R::::::R     R:::::ROO:::::::::::::OO 
N::::::N        N::::::X:::::X       X:::::X     P::::::::P         R::::::R     R:::::R  OO:::::::::OO   
NNNNNNNN         NNNNNNXXXXXXX       XXXXXXX     PPPPPPPPPP         RRRRRRRR     RRRRRRR    OOOOOOOOO     
                                                                                                          
                                                                                                          
                                                                                                          
                                                                                                          
                                                                                                          
                                                                                                          
                                                                                                              
        """
    print_stylish_big(name)
    link = input("Enter the Issuu document link: ")
    print(f"Link Downlaod: {link}")
    print("\033[92m" + link + "\033[0m")
    parts = urllib.parse.urlparse(link)
    last_part = parts.path.split('/')[-1]
    fourth_part = parts.path.split('/')[1]
    downlaod_issuu_pdf(last_part,fourth_part)
    print("\033[92mDownload successful :)\033[0m")
    print("\033[92mDownload in output_folder\033[0m")
