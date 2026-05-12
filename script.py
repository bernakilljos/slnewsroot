import requests,os,subprocess,io
from pypdf import PdfReader
os.makedirs('out/text',exist_ok=True)
# selected reports URLs
basew='https://democracy.wandsworth.gov.uk/'
bases='https://moderngov.southwark.gov.uk/'
urls={
'w_fox_cover':basew+'documents/s124875/Cabinet%20report%20FHF.pdf',
'w_fox_review':basew+'documents/s124876/Fox%20House%20fire%20Independent%20Review.pdf',
'w_social_cover':basew+'documents/s124887/26-8%20Cabinet%20cover%20report%20Housing%20TFG.pdf',
'w_social_final':basew+'documents/s124888/26-8%20TF%20Group%20Final%20Report%20final%20version.pdf',
'w_improve':basew+'documents/s124884/Housing%20Improvement%20Plan.pdf',
'w_hra':basew+'documents/s124877/26-7%20-%20HRA%20Rent%20Setting%20Report.pdf',
'w_grant':basew+'documents/s124924/Paper%20No.%2026-18%20Grants%20OSC%20Sub-Committee%20Report%20Round%2031.pdf',
'w_grantapp':basew+'documents/s124925/Appendix%20A%20-%20WGF%20R31%20Summary%20of%20Applications.pdf',
'w_mental':basew+'documents/s124885/Final%20Report.pdf',
'w_mentala':basew+'documents/s124886/OFFICIAL%20Healthy%20Minds%20Action%20Plan.pdf',
'w_sacre_rs':basew+'documents/s124718/Briefing%20Sheet%20for%20Wandsworth.pdf',
'w_sacre_ar':basew+'documents/s125194/SACRE%20annual%20report%202024-25.pdf',
's_toilet':bases+'documents/s131119/Updated%20report%20on%20Access%20to%20Toilets.pdf',
's_meno':bases+'documents/s131118/Local%20Practice%20Menopause%20in%20Southwark.pdf',
's_safe':bases+'documents/s131122/Adult%20Safeguarding%20definition%20review%20scope.pdf',
's_licpol':bases+'documents/s130981/Report%20Licensing%20Act%202003%20Review%20of%20Statement%20of%20Licensing%20Policy%202026%20to%202031.pdf',
's_liccon':bases+'documents/s130983/Appendix%20B%20Licensing%20Policy%20Consultation%20Results.pdf',
's_cia':bases+'documents/s130985/Report%20Licensing%20Act%202003%20Review%20of%20the%20Cumulative%20Impact%20Areas%20in%20Southwark.pdf',
's_levy':bases+'documents/s130989/Report%20Licensing%20Act%202003%20Review%20of%20the%20Late-Night%20Levy.pdf',
's_peck':bases+'documents/s130917/Report%20Licensing%20Act%202003%20Peckham%20Palais%201a%20Rye%20Lane%20London%20SE15%205EW.pdf',
's_kent':bases+'documents/s130924/Report%20Licensing%20Act%202003%20Kent%20Restaurant%20and%20Lounge%20First%20Floor%20516%20Old%20Kent%20Road%20London%20SE1%205.pdf',
's_shrimp':bases+'documents/s130955/Report%20Licensing%20Act%202003%20Shrimp%20and%20Wings%20127%20Queens%20Road%20London%20SE15%202ND.pdf',
}
s=requests.Session()
for n,u in urls.items():
 try:
  r=s.get(u,timeout=45); print(n,r.status_code,len(r.content),r.url); open(f'out/text/{n}.meta','w').write(str(r.status_code)+' '+r.url+' '+str(len(r.content))+' '+r.headers.get('Content-Type','')+'\n'+r.text[:200])
  open('/tmp/x.pdf','wb').write(r.content)
  pdf=PdfReader(io.BytesIO(r.content)); open(f'out/text/{n}.txt','w').write('\n\n'.join((p.extract_text() or '') for p in pdf.pages))
  open(f'out/text/{n}.url','w').write(r.url)
 except Exception as e: open(f'out/text/{n}.err','w').write(str(e)); print(n,e)
