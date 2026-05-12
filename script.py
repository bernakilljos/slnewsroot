import requests,os
from urllib.parse import urlencode
os.makedirs('out',exist_ok=True)
hosts=['https://democracy.wandsworth.gov.uk','https://moderngov.lambeth.gov.uk','http://moderngov.lambeth.gov.uk','https://moderngov.southwark.gov.uk','http://moderngov.southwark.gov.uk','https://www.southwark.gov.uk']
paths=['/mgCalendarMonthView.aspx?GL=1&bcr=1&M=1&Y=2026','/mgCalendarMonthView.aspx?GL=1&bcr=1&curmonth=2026-01-01','/mgCalendarMonthView.aspx?GL=1&bcr=1&ctl00_MainContent_month=2026-01-01','/mgCalendarAgendaView.aspx?XXR=0&M=1&DD=2026&CID=0','/mgCalendarWeekView.aspx?CI=0&DD=2026-01-26','/mgCalendarMonthView.aspx?CID=0&year=2026&month=1','/mgCalendarMonthView.aspx?M=1&DD=2026&CID=0','/','/robots.txt']
s=requests.Session()
for hi,h in enumerate(hosts):
 for pi,p in enumerate(paths):
  try:
   r=s.get(h+p,timeout=40)
   fn=f'out/{hi}_{pi}.txt';open(fn,'wb').write((f'URL={r.url}\nSTATUS={r.status_code}\n'.encode()+r.content))
   print(fn,r.status_code,len(r.content),r.url)
  except Exception as e: open(f'out/{hi}_{pi}.txt','w').write(str(e));print(e)
