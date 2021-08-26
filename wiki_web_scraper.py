import requests
import re
from bs4 import BeautifulSoup
from tqdm import tqdm


def categorical_scraper(query, save_path, limit=-1,page_per_save=10000,text_into_sentences_param=True,remove_numbers=False,just_title_analysis=False):
		"""
		Wikipedia üzerinden kategorik olarak veri çekmek için kullanılır. 
 
		:param CATEGORY_QUERY: Ayıklanacak kategori sorgusu.
		:type CATEGORY_QUERY: str

		:param save_path: Ayıklanan verinin kaydedileceği yol.
		:type save_path: str

		:param LIMIT: Ayıklanması istenen veri limiti. Verilmediği taktirde tüm verileri çeker.
		:type LIMIT: int

		:param page_per_save: Belirlenen aralıkla ayıklanan kategorik verinin kaydedilmesini sağlar.
		:type page_per_save: int

		:param text_into_sentences_param: Ayıklanan verilerin cümleler halinde mi, yoksa metin halinde mi kaydedileceğini belirler.
		:type text_into_sentences_param: bool

		:param remove_numbers: Ayıklanan verilerden rakamların silinip silinmemesini belirler.
		:type remove_numbers: bool

		:param just_title_analysis: Sadece sayfaların başlık bilgilerinin toplanmasını sağlar.
		:type just_title_analysis: bool
 
		"""

		if limit == -1:
			limit = 9999999

		query = query.replace(" ","_")
		CATEGORY_QUERY = query
		LIMIT = limit
		HEADERS_PARAM = {
				"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}

		return_list = category_scraping_interface(query, limit, HEADERS_PARAM,save_path,page_per_save,remove_numbers,just_title_analysis,text_into_sentences_param)

		if return_list is None:
				return []
		else:
				return return_list


def text_scraper_from_pagelist(page_list_path,save_path,page_per_save=10000,remove_numbers=False,text_into_sentences_param=True,RANGE=None):
	"""

	Wikipedia üzerinden kategorik olarak veri çekmek için kullanılır.

	:param page_list_path: Toplanan sayfaların başlık bilgilerinin çıkartılmasını sağlar
	:type page_list_path: str

	:param save_path: Ayıklanan verinin kaydedileceği yol.
	:type save_path: str

	:param page_per_save: Belirlenen aralıkla ayıklanan kategorik verinin kaydedilmesini sağlar.
	:type page_per_save: int

	:param text_into_sentences_param: Ayıklanan verilerin cümleler halinde mi, yoksa metin halinde mi kaydedileceğini belirler.
	:type text_into_sentences_param: bool

	:param remove_numbers: Ayıklanan verilerden rakamların silinip silinmemesini belirler.
	:type remove_numbers: bool

	:param RANGE: Ayıklnacak verilerin aralığını belirler. "RANGE = [500,1000]" şeklinde kullanılır. Verilmediği zaman tüm veri ayıklanır.
	:type RANGE: list

	"""  

	page_list = []
	text_list = []

	HEADERS_PARAM = {
				"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}

	with open(page_list_path, 'r') as f:
		page_list = [line.strip() for line in f]

	if RANGE is not None:
		page_list = page_list[RANGE[0]:RANGE[1]]

	temp_range = 0
	loop_counter = 0

	for i in range(page_per_save,len(page_list)+page_per_save,page_per_save):
		
		if loop_counter == (len(page_list) // page_per_save):
			PATH = save_path + "/" + "scraped_page" + "_" + str(temp_range) + " - " + str(len(page_list)) + ".txt"
			temp_text_list = text_into_sentences(text_scraper(page_list[temp_range:i], (len(page_list) % page_per_save), HEADERS_PARAM,True),remove_numbers,text_into_sentences_param)
		else:
			PATH = save_path + "/" + "scraped_page" + "_" + str(temp_range) + " - " + str(i) + ".txt"
			temp_text_list = text_into_sentences(text_scraper(page_list[temp_range:i], page_per_save, HEADERS_PARAM,True),remove_numbers,text_into_sentences_param)

		text_list += temp_text_list

		save_to_csv(PATH,temp_text_list)
		temp_range = i
		loop_counter += 1

	print("\n\"" + page_list_path + "\" konumundaki " +str(len(page_list)) + " adet sayfa içerisinden " + str(len(text_list)) + " satır metin ayrıştırıldı.")
	return text_list


def page_scraper(page_soup, LIMIT):
	"""

	Gönderilen wikipedia SOUP objesinin içerisindeki kategorik içerik sayfaları döndürür.

	:param page_soup: Wikipedia kategori sayfasının SOUP objesidir.
	
	:param LIMIT: Ayıklanacaj sayfa limitini belirler.
	:type LIMIT: int

	"""
	page_list = []

	try:
			pages = page_soup.find("div", attrs={"id": "mw-pages"}).find_all("a")
			for page in pages[1:]:
					if len(page_list) == LIMIT:
							break
					else:
							page_list.append([page.text, page["href"]])
			return page_list
	except:
		pass


def sub_category_scraper(sub_soup):
	"""

	Gönderilen wikipedia SOUP objesinin içerisindeki alt kategorileri döndürür.

	:param sub_soup: Alt kategori sayfasının SOUP objesidir.

	"""
	sub_list = []

	try:
			sub_categories = sub_soup.find_all("div", attrs={"class": "CategoryTreeItem"})
			for sub in sub_categories[1:]:
					sub_list.append([sub.a.text, sub.a["href"]])

			return sub_list
	except:
			 print("Aranan kategori için yeterli sayfa bulunamadı")


def sub_scraper(sub, HEADERS_PARAM):
	
	"""

	Fonksiyona gelen wikipedia kategori/alt kategorisinin SOUP objesini döndürür.

	:param sub: Alt kategori sayfasının linkini içerir.

	"""

	try:
			req = requests.get("https://tr.wikipedia.org" + str(sub[1]), headers=HEADERS_PARAM)
			soup = BeautifulSoup(req.content, "lxml")
			return soup

	except:
			print("\nAlt kategori kalmadı")
			return False


def text_scraper(page_list, LIMIT, HEADERS_PARAM,IS_FROM_TXT=False):
		"""
 
		Önceden ayıklanmış sayfa listesini içerisindeki sayfaları ayıklayarak içerisindeki metin listesini döndürür.

		:param page_list: Sayfa listesini içerir.

		:parama LIMIT: Ayıklanacaj sayfa limitini belirler.
		:type LIMIT: int

		:param IS_FROM_TXT: Ayıklanacak sayfanın listeleden mi olup olmadığını kontrol eder.
 
		"""
		text_list = []
		
		with tqdm(total=LIMIT, desc="Sayfa Ayrıştırılıyor") as pbar:
			for page in page_list:

					if len(text_list) == LIMIT:
							break
					if IS_FROM_TXT is False:
						req = requests.get("https://tr.wikipedia.org" + str(page[1]), headers=HEADERS_PARAM)
					else:
						req = requests.get("https://tr.wikipedia.org" + str(page), headers=HEADERS_PARAM)
					soup = BeautifulSoup(req.content, "lxml")
					page_text = soup.find_all("p")
					temp_text = ""

					for i in page_text[1:]:
							temp_text = temp_text + i.text

					text_list.append(temp_text)
					pbar.update(1)

		return text_list


def first_variable(CATEGORY_QUERY, LIMIT, HEADERS_PARAM):
		"""
 
		Sorguda verilen kategorinin doğruluğunu kontrol eder ve eğer sorgu doğru ise ilk değerleri ayıklar.

		:param CATEGORY_QUERY: Ayıklanacak kategori sorgusu.
		:type CATEGORY_QUERY: str

		:param LIMIT: Ayıklanması istenen veri limiti. Verilmediği taktirde tüm verileri çeker.
		:type LIMIT: int
 
		"""

		first_req = requests.get("https://tr.wikipedia.org/wiki/Kategori:" + CATEGORY_QUERY, headers=HEADERS_PARAM)
		first_soup = BeautifulSoup(first_req.content, "lxml")
		page_list = page_scraper(first_soup, LIMIT)
		sub_list = sub_category_scraper(first_soup)

		return page_list, sub_list


def text_into_sentences(texts,remove_numbers,text_into_sentences_param):
		"""
 
		Metin verilerini cümlelerine ayıklar.

		:param texts: Düzlenecek metin verisi.

		:param remove_numbers: Sayıların temizlenip temizlenmeyeceğini kontrol eder.

		:param text_into_sentences_param: Metinlerin cümlelere çevrilip çevrilmeyeceğini kontrol eder.
 
		"""
	flatlist = []   
	sent_list = []

	texts = sentence_cleaning(texts,remove_numbers)
	
	if text_into_sentences_param is True:
		for line in texts:
			temp_line = re.split(r'(?<![IVX0-9]\S)(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', line)
			for i in temp_line:
				if len(i.split(" ")) > 3:
					sent_list.append(i)
	else:
		sent_list = texts

	flatlist = list(dict.fromkeys(flat(sent_list,flatlist)))

	return flatlist


def flat(sl,fl):

		"""
 
		Metinler, cümlelerine ayırıldıktan sonra listenin düzlenmesine yarar.

		:param sl: Yollanan listle.

		:param fl: Düzlemem liste.
 
		"""                    
		for e in sl:                
				if type(e) == list:     
						flat(e,fl)             
				elif len(e.split(" "))>3:
					fl.append(e)  
		return fl


def sentence_cleaning(sentences,remove_numbers):
		"""
 
		Ayıklanan wikipedia verilerinin temizlenmesi bu fonksiyonda gerçekleşir.

		:param sentences: Temizlenmek için gelen veri seti.
		
		:param remove_numbers: Sayıların temizlenip temizlenmeyeceğini kontrol eder.
 
		"""
		return_list = []

		if remove_numbers is False:
			removing_func = '[^[a-zA-ZğüışöçĞÜIİŞÖÇ0-9.,!:;`?%&\-\'" ]'
		else:
			removing_func = '[^[a-zA-ZğüışöçĞÜIİŞÖÇ.,!:;`?%&\-\'" ]'

		for input_text in sentences:
				try:            
						input_text = re.sub(r'(\[.*?\])', '', input_text)
						input_text = re.sub(r'(\(.*?\))', '', input_text)
						input_text = re.sub(r'(\{.*?\})', '', input_text)
						input_text = re.sub(removing_func, '', input_text)
						input_text = re.sub("(=+(\s|.)*)", "", input_text)
						input_text = re.sub("(\s{2,})", "", input_text)
						input_text = input_text.replace("''", "")
						input_text = input_text.replace("\n", "")            
						return_list.append(input_text)
				except:
						pass
		
		return return_list


def save_to_csv(PATH,data,is_just_title_analysis=False):
		"""
 
		Verilerin 'csv' formatında kaydedilmesini bu fonksiyonda gerçekleşir.

		:param PATH: Kaydedilecek yol.

		:param data: Kaydedilecek veri.

		:param is_just_title_analysis: Sadece analiz yapılıp yapılmadığını kontrol eder.
 
		"""

	if is_just_title_analysis is False:
		with open(PATH, "w") as output:
			for i in data:
				output.write(i+"\n")
	else:
		temp_data = []
		for i in data:
			temp_data.append(i[1])
		with open(PATH, "w") as output:
			for i in temp_data:
				output.write(i+"\n")


def category_scraping_interface(CATEGORY_QUERY, LIMIT, HEADERS_PARAM,SAVE_PATH,PAGE_PER_SAVE,REMOVE_NUMBERS,JUST_TITLE_ANALYSIS,TEXT_INTO_SENTENCES_PARAM):
			"""
		
		Kategorik verilerin ayıklanma işlemleri bu fonksiyonda yönetilir.
		
		:param CATEGORY_QUERY: Ayıklanacak kategori sorgusu.
		:type CATEGORY_QUERY: str

		:param SAVE_PATH: Ayıklanan verinin kaydedileceği yol.
		:type SAVE_PATH: str

		:param LIMIT: Ayıklanması istenen veri limiti. Verilmediği taktirde tüm verileri çeker.
		:type LIMIT: int

		:param PAGE_PER_SAVE: Belirlenen aralıkla ayıklanan kategorik verinin kaydedilmesini sağlar.
		:type PAGE_PER_SAVE: int

		:param TEXT_INTO_SENTENCES_PARAM: Ayıklanan verilerin cümleler halinde mi, yoksa metin halinde mi kaydedileceğini belirler.
		:type TEXT_INTO_SENTENCES_PARAM: bool

		:param REMOVE_NUMBERS: Ayıklanan verilerden rakamların silinip silinmemesini belirler.
		:type REMOVE_NUMBERS: bool

		:param JUST_TITLE_ANALYSIS: Sadece sayfaların başlık bilgilerinin toplanmasını sağlar.
		:type JUST_TITLE_ANALYSIS: bool
		
		"""

		sub_list = []
		page_list = []
		text_list = []

		page_list, sub_list = first_variable(CATEGORY_QUERY, (LIMIT - len(text_list)), HEADERS_PARAM)
		fv = True
				
		if page_list and sub_list is not None:        
			with tqdm(total=LIMIT, desc="Sayfa Taranıyor") as pbar:
				while len(page_list) < LIMIT:

					if fv is True:
						pbar.update(len(page_list))
						fv = False 
					
					temp_soup = ""

					if len(sub_list) == 0:
						break
				
					temp_soup = sub_scraper(sub_list[0], HEADERS_PARAM)    

					if (temp_soup == False):
						break   

					del sub_list[0]   

					sub_list = sub_list + sub_category_scraper(temp_soup)

					temp_page_scraper = page_scraper(temp_soup, (LIMIT - len(page_list)))  

					if temp_page_scraper is not None:
						for i in temp_page_scraper:
							if i not in page_list:
								page_list.append(i)
								pbar.update(1)            

					if len(sub_list) == 0:
						sub_list = sub_list + sub_category_scraper(temp_soup)

			temp_range = 0
			loop_counter = 0

			if JUST_TITLE_ANALYSIS is False: 
				for i in range(PAGE_PER_SAVE,len(page_list)+PAGE_PER_SAVE,PAGE_PER_SAVE):

					if loop_counter == (len(page_list) // PAGE_PER_SAVE):
						PATH = SAVE_PATH + "/" + CATEGORY_QUERY + "_" + str(temp_range) + " - " + str(len(page_list)) + ".txt"
						temp_text_list = text_into_sentences(text_scraper(page_list[temp_range:i], (len(page_list) % PAGE_PER_SAVE), HEADERS_PARAM),REMOVE_NUMBERS,TEXT_INTO_SENTENCES_PARAM)
					else:
						PATH = SAVE_PATH + "/" + CATEGORY_QUERY + "_" + str(temp_range) + " - " + str(i) + ".txt"
						temp_text_list = text_into_sentences(text_scraper(page_list[temp_range:i], PAGE_PER_SAVE, HEADERS_PARAM),REMOVE_NUMBERS,TEXT_INTO_SENTENCES_PARAM)
											
					text_list += temp_text_list

					save_to_csv(PATH,temp_text_list)         
					temp_range = i
					loop_counter += 1

				print("\n\n"+str(len(page_list)) + " adet sayfa bulundu ve içerisinden " + str(len(text_list)) + " satır farklı metin ayrıştırıldı.")
				return text_list

			else:
				PATH = SAVE_PATH + "/" + CATEGORY_QUERY + "_" + str(len(page_list)) + "_page_links" + ".txt"
				save_to_csv(PATH,page_list,JUST_TITLE_ANALYSIS)
				print("\n\n"+str(len(page_list)) + " adet sayfa bulundu ve sayfaların adresleri \"" + PATH + "\" konumunda kaydedildi.")
				return page_list

		else:
				print("Aranan kategori bulunamadı.")
