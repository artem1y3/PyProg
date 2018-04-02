import requests
from bs4 import BeautifulSoup
import csv
import zipfile
import os

def get_json(url):
	r = requests.get(url)
	return r.json()

def get_data(url):
	pass


def main():
	order = ['number','fz','url','dateZakupkaStart','dateZakupkaEnd','zajavkaPrice','zajavkaHavePrice','contractPrice','companyName','companyInn','companyPlace','lots']
	atr = {
		'number':"Номер",
		'fz':"ФЗ",
		'url':"Ссылка",
		'dateZakupkaStart':"Дата начала",
		'dateZakupkaEnd':"Дата окончания",
		'zajavkaPrice':"Цена заявки",
		'zajavkaHavePrice':"Имеющаяся цена",
		'contractPrice':"Цена по контракту",
		'companyName':"Название компании",
		'companyInn':"ИНН компании",
		'companyPlace':"Местоположение компании",
		'lots':"Лоты"
	}
	url = 'http://phpnt.com/zakupki/get?regNumber='

	while True:
		s = input("Введиде номер закупки: ")
		print("===============================================")
		if s == "exit":
			break
		else:
			js = get_json(url+s)
			for o in order:
				print(str(atr[o])+": "+str(js[o]))
			print("===============================================")



if __name__ == '__main__':
	main()