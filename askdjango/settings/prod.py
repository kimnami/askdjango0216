from .common import *

DEBUG = False

STATIC_ROOT = os.path.join(BASE_DIR,'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DATABASES = {
	'default' : {
		'ENGINE':'django.db.backends.mysql',
		'HOST':'NamheeKim.mysql.pythonanywhere-services.com',
		'NAME':'NamheeKim$default',
		'USER':'NamheeKim',
		'PASSWORD':'namska!*26',
		OPTIONS:{
			'sql_mode':'traditional',
		},
	},
}
