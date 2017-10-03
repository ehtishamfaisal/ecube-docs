import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
urls = {
	'scope': 'https://www.googleapis.com/auth/drive',
	'storage': dir_path + '/storage.json',	
	'client_id': dir_path + '/client_id.json',
	'mimeType': 'application/vnd.google-apps.',
	
	}

