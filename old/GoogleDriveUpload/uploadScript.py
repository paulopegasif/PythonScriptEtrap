# Google drive backup

# Upload files to google drive
# List files in google drive
# Download files from google drive

# pip install pydrive
import re
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

#Bibliotecas para barra de progresso
from tqdm import tqdm
from time import sleep



gauth = GoogleAuth()
#gauth.credentials = creds
drive = GoogleDrive(gauth)




folder_cropped = '1V_2FZw5X9T828xQedEOvb5l9lsr6Zoac'
folder = '1Lzn6tLnREkbgqlCT3tHNDqCrPoUyYZqN'

# Upload files

directory = os.path.abspath("../img")
cont = 1

busca = re.compile('.*cropped.*')




	
for f in tqdm(os.listdir(directory), desc="Uploading", unit="files"):

	#print("Fazendo Upload de: " + str(cont) + " imagens")
	cont+=1  #incrementando de 1 em 1
	filename = os.path.join(directory, f)

	if busca.match(filename): #Se tiver cropped no nome
		print("Cropped")
		gfile = drive.CreateFile({'parents' : [{'id' : folder_cropped}], 'title' : f})
		gfile.SetContentFile(filename)
		gfile.Upload()
		sleep(0.1)

	else:
		print("Originals")
		gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : f})
		gfile.SetContentFile(filename)
		gfile.Upload()
		sleep(0.1)

print()
print("Upload de imagens concluído com sucesso! ;)")




"""
# Download files
file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
for index, file in enumerate(file_list):
	print(index+1, 'file downloaded : ', file['title'])
	file.GetContentFile(file['title'])
"""