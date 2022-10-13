import requests
from bs4 import BeautifulSoup

url = requests.get("https://org2fcdeea7.crm2.dynamics.com/")
if(url.status_code == 200):
    print(url.text)
else:
    print("Error al abrir la pagina")

#https://org2fcdeea7.crm2.dynamics.com/main.aspx?appid=8d2ef41a-3de1-ec11-bb3d-000d3a88ad48&etn=cr217_prestador&pagetype=entitylist&viewType=1039&viewid=%7B040373D3-0C43-498B-947E-B925C75496CD%7D