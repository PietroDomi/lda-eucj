import html2text
import os

celexs = os.listdir("data_scraping/data_html")

text_maker = html2text.HTML2Text()
text_maker.ignore_images = True
text_maker.ignore_links = True

for celex in celexs:
    with open("data/converted/"+celex[:-5]+".txt","w", encoding='utf-8') as file:
        file.write(text_maker.handle(open("data_scraping/data_html/"+celex,encoding='utf-8').read()))
        print(celex + " converted")

