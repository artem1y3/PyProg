import requests
from bs4 import BeautifulSoup
import csv
import zipfile
import os

def get_data(url):
	with open(url) as f:
		y = BeautifulSoup(f, "lxml").find("oos:unfairsupplier").find("oos:fullname").text.strip()
		print(y)
	return y

def write_csv(data):
	with open('names.csv', 'a') as file:
	    writer = csv.writer(file)
	    writer.writerow((data['name'], data['surname'], data['age']))


# def extract_archive(zip, path):
# 	fantasy_zip = zipfile.ZipFile(zip)
# 	fantasy_zip.extractall(path)
# 	fantasy_zip.close()

def main():
	#Пути архива и папки хранения файлов
	zip = 'unfairSupplier_2015091000_2015091100_001.xml.zip'
	path = 'xml/'
	#Распаковка
	#extract_archive(zip,path)
	#Список файлов
	lst_xml = os.listdir(path="./xml")
	for file in lst_xml:
		get_data(path+file)
		



if __name__ == '__main__':
	main()