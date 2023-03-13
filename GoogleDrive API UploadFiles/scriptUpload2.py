from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()
drive = GoogleDrive(gauth)












upload_file_list = ['afideo2.jpg', 'afideo3.jpg']
for upload_file in upload_file_list:
	gfile = drive.CreateFile({'parents': [{'id': '1Lzn6tLnREkbgqlCT3tHNDqCrPoUyYZqN'}]})
	# Read file and set it as the content of this instance.
	gfile.SetContentFile(upload_file)
	gfile.Upload() # Upload the file.



