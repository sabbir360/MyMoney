'''
Development server init
'''

__author__ = 'sabbir'
from appcore import APPLICATION
APPLICATION.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
