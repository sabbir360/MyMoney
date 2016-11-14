'''
#!/usr/bin/env python
__author__ = 'Sabbir'

import os
from appcore import application

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    application.run('0.0.0.0', port)
'''
