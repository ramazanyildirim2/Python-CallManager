from requests import Session
from requests.auth import HTTPBasicAuth
from zeep import Client
from zeep.transports import Transport
from zeep.cache import SqliteCache
import urllib3

WSDL_URI = 'AXLAPI.wsdl'
CUCM_USERNAME = 'AXL_ZKB_DESTEK'
CUCM_PASSWD = 'zkb1234'
CUCM_URL = 'https://10.211.35.10:8443/axl/'

#Connect to CUCM
# disable Insecure Request Warning due to Verify
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

session = Session()
session.verify = False
session.auth = HTTPBasicAuth(CUCM_USERNAME, CUCM_PASSWD)
transport = Transport(session=session, timeout=10, cache=SqliteCache())

client = Client(WSDL_URI, transport=transport)
service = client.create_service("{http://www.cisco.com/AXLAPIService/}AXLAPIBinding", CUCM_URL)

#Verify that you made the connection and can access the APIs

print((service.getCCMVersion()))