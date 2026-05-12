import requests,os
os.makedirs('out/pages',exist_ok=True)
s=requests.Session()
urls={}
# meeting ids
for mid,cid in [(10266,792),(10010,305),(10115,511),(9927,763),(10385,320)]: urls[f'w_{mid}']=f'https://democracy.wandsworth.gov.uk/ieListDocuments.aspx?CId={cid}&MId={mid}'
for mid,cid in [(8402,172),(8405,327),(8249,519),(8178,650),(8403,172),(8320,171)]: urls[f's_{mid}']=f'https://moderngov.southwark.gov.uk/ieListDocuments.aspx?CId={cid}&MId={mid}'
for name,u in urls.items():
 try:
  r=s.get(u,timeout=30)
  open(f'out/pages/{name}.html','wb').write(r.content)
  open(f'out/pages/{name}.url','w').write(r.url)
  print(name,r.status_code,len(r.content),r.url)
 except Exception as e: print(name,e)
