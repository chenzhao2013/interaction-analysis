from bs4 import BeautifulSoup
import requests
import os



exclude_applets = []

def firstReq(url):
    headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
            'referer':'https://ifttt.com/smartthings',#伪造一个访问来源 "http://www.mzitu.com/100260/2"
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'cookie': 'browser_session_id=iRyplw9bvALySSK86sE26A; expiring_session_token=mDOfv22pzToVHgaaep_RcA; anon_id=e4629e21eab49887036183e69cf52197; aem_user_login=; aem_user_email=; aem_user_avatar=; aem_user_type=default; timezone=Asia/Shanghai; _applet_service_session=dEtRNGNQSE16ajg5N0JxRm0yKzM5dHFFY2ZxOVAwVkhFVHVlRVpQNUczc3c0WEhXZzNMSHRjUFE3OGVnb2hmeENLdlltME9NOHNYNEF3TWZqWGovNTMxR2lLS0xmZFhxOEZ6R0ZqNzV6aDlyWXE2QmFVcERCK3FqMFlXSFVZTUNlakxvcnZCbUZvY2tXdEZOSkYxZ28zT2ZHbCtsQXU1bkNMRHZKeU9oOWhzU21tNFYxeHJZUEdkUmUrU1hwczNhSngxcERsNWIwYnhQSkVOTXRMeXlOdz09LS1GREgwZk1vbnhKQUJvL2JOOGcxTjhnPT0%3D--5ed6ab2c1ec3483ba19b40fe813545be9ed45372',
            'X-Requested-With': 'XMLHttpRequest'
    }
    content = requests.get(url, headers=headers)
    return content


def analysis():
    url = 'https://ifttt.com/smartthings'
    html = firstReq(url)
    all_rule = BeautifulSoup(html.text, 'lxml').find_all('span', class_='title')#.find_all('a')
    all_id = BeautifulSoup(html.text, 'lxml').find_all('li', class_='web-applet-card', attrs={"data-id": True})
    # for li in all_id:
    #     print(li['data-id'])
    #     exclude_applets.extend(li['data-id'])

    f = open('ifttt-smart.txt', 'a')
    for a in all_rule:
        desc = a.text.replace('\n', '').replace('\r', '').strip()
        print(desc)
        f.write(desc+'\n')
    f.close()


def more(fileName):
    url = 'https://ifttt.com/services/smartthings/more?exclude_applets=[%22NyGhjenq%22,%22dL4peb2W%22,%22vs2NuKkR%22,%22qmrzQGhq%22,%22CKibyjSF%22,%22Cbuk2SUH%22,%22Xe7VTKCr%22,%22480986p%22,%22uhfavDW7%22,%22480982p%22,%22156899p%22]&offset=6&authenticity_token=vEVETnR1vkDWuCYClbytnID0H5s6P9ZWZ0PebrVcm9C%2F07LsTcAgPBTLTXJSuz1UfF8uSb4Gb2Yw8ljsiBNbaQ%3D%3D'
    f = open(fileName, 'r')   
    html = f.read()

    all_rule = BeautifulSoup(html, 'lxml').find_all('span', class_='title')#.find_all('a')
    f = open('ifttt-smart.txt', 'a')
    for a in all_rule:
        desc = a.text.replace('\n', '').replace('\r', '').strip()
        print(desc)
        f.write(desc+'\n')
    f.close()
    # all_id = BeautifulSoup(html.text, 'lxml').find_all('li', class_='web-applet-card', attrs={"data-id": True})
    # for li in all_id:
    #     print(li['data-id'])
    #     exclude_applets.extend(li['data-id'])


url = ''
url1 = 'https://ifttt.com/services/smartthings/more?exclude_applets=[%22NyGhjenq%22,%22dL4peb2W%22,%22vs2NuKkR%22,%22qmrzQGhq%22,%22CKibyjSF%22,%22Cbuk2SUH%22,%22Xe7VTKCr%22,%22480986p%22,%22uhfavDW7%22,%22480982p%22,%22156899p%22]&offset=6&authenticity_token=vEVETnR1vkDWuCYClbytnID0H5s6P9ZWZ0PebrVcm9C%2F07LsTcAgPBTLTXJSuz1UfF8uSb4Gb2Yw8ljsiBNbaQ%3D%3D'
url2 = 'https://ifttt.com/services/smartthings/more?exclude_applets=NyGhjenq,dL4peb2W,vs2NuKkR,qmrzQGhq,CKibyjSF,Cbuk2SUH,Xe7VTKCr,480986p,uhfavDW7,480982p,156899p,170044p,RtT8pJak,pu35Hxq9,114080p,im6FqC9y,TwQVj9iB,zr5HiefS,202191p,qmrzQGhq,413209p,114085p,CKibyjSF,125427p,vs2NuKkR,pGRqB9X3,480983p,iGUjZr8W,372977p,yMnbLQh5,349425p,uvwyxW8D,YZrvGLQP,mHEw9K7k,115639p&offset=35&authenticity_token=x6WDlERCgbmGYS2Uc7Fk%2FRnh9pB7EOE7p52cyEi5QB3EM3U2ffcfxUQSRuS0tvQ15UrHQv8pWAvwLBpKdfaApA%3D%3D'
url3 = 'https://ifttt.com/services/smartthings/more?exclude_applets=NyGhjenq,dL4peb2W,vs2NuKkR,qmrzQGhq,CKibyjSF,Cbuk2SUH,Xe7VTKCr,480986p,uhfavDW7,480982p,156899p,170044p,RtT8pJak,pu35Hxq9,114080p,im6FqC9y,TwQVj9iB,zr5HiefS,202191p,qmrzQGhq,413209p,114085p,CKibyjSF,125427p,vs2NuKkR,pGRqB9X3,480983p,iGUjZr8W,372977p,yMnbLQh5,349425p,uvwyxW8D,YZrvGLQP,mHEw9K7k,115639p,297748p,170045p,369465p,282644p,346606p,139772p,yrzyAbnp,374817p,Bcx2b9Uy,437159p,420034p,354274p,365679p,114084p,333387p,bZT5r7Ds,198215p,437163p,115640p,237769p,Mt9Gfqc5,435669p,373750p,aQzk4ry6&offset=59&authenticity_token=x6WDlERCgbmGYS2Uc7Fk%2FRnh9pB7EOE7p52cyEi5QB3EM3U2ffcfxUQSRuS0tvQ15UrHQv8pWAvwLBpKdfaApA%3D%3D'
url4 = 'https://ifttt.com/services/smartthings/more?exclude_applets=NyGhjenq,dL4peb2W,vs2NuKkR,qmrzQGhq,CKibyjSF,Cbuk2SUH,Xe7VTKCr,480986p,uhfavDW7,480982p,156899p,170044p,RtT8pJak,pu35Hxq9,114080p,im6FqC9y,TwQVj9iB,zr5HiefS,202191p,qmrzQGhq,413209p,114085p,CKibyjSF,125427p,vs2NuKkR,pGRqB9X3,480983p,iGUjZr8W,372977p,yMnbLQh5,349425p,uvwyxW8D,YZrvGLQP,mHEw9K7k,115639p,297748p,170045p,369465p,282644p,346606p,139772p,yrzyAbnp,374817p,Bcx2b9Uy,437159p,420034p,354274p,365679p,114084p,333387p,bZT5r7Ds,198215p,437163p,115640p,237769p,Mt9Gfqc5,435669p,373750p,aQzk4ry6,umfL4XaW,147389p,420121p,376197p,144215p,419794p,NKXFCrTA,JNiLfJjC,nmuxNcET,402519p,453102p,193627p,445967p,115669p,467096p,128715p,ZtSKP37Q,268150p,120047p,zpaKXkH8,Xhpg6uLZ,DAzGxi2h,Th2tnF7b,372070p&offset=83&authenticity_token=VzrFFKm6n0u9OuG8LskWGUXnd36DTG1H5l1owYPQy8tUrDO2kA8BN39JiszpzobRuUxGrAd11Hex7O5Dvp8Lcg%3D%3D'
url5 = 'https://ifttt.com/services/smartthings/more?exclude_applets=NyGhjenq,dL4peb2W,vs2NuKkR,qmrzQGhq,CKibyjSF,Cbuk2SUH,Xe7VTKCr,480986p,uhfavDW7,480982p,156899p,170044p,RtT8pJak,pu35Hxq9,114080p,im6FqC9y,TwQVj9iB,zr5HiefS,202191p,qmrzQGhq,413209p,114085p,CKibyjSF,125427p,vs2NuKkR,pGRqB9X3,480983p,iGUjZr8W,372977p,yMnbLQh5,349425p,uvwyxW8D,YZrvGLQP,mHEw9K7k,115639p,297748p,170045p,369465p,282644p,346606p,139772p,yrzyAbnp,374817p,Bcx2b9Uy,437159p,420034p,354274p,365679p,114084p,333387p,bZT5r7Ds,198215p,437163p,115640p,237769p,Mt9Gfqc5,435669p,373750p,aQzk4ry6,umfL4XaW,147389p,420121p,376197p,144215p,419794p,NKXFCrTA,JNiLfJjC,nmuxNcET,402519p,453102p,193627p,445967p,115669p,467096p,128715p,ZtSKP37Q,268150p,120047p,zpaKXkH8,Xhpg6uLZ,DAzGxi2h,Th2tnF7b,372070p,428332p,428329p,383273p,125431p,473774p,BT9nXDWz,xsUN2m4x,BFEB7vRZ,Pv9ZhsVd,u6NikWc8,aTMxtFVm,SsRzZ5Ed,wtGqhucA,nUL3zeBg,zXU6PYHS,p5xi3DNS,eq9WyX8z,hvhTJjUr,sUQnzrM6,LYxCTXr8,HMdVP2ZJ,aLwFYDc4,bidMGsib,j6RtfJTk&offset=107&authenticity_token=VzrFFKm6n0u9OuG8LskWGUXnd36DTG1H5l1owYPQy8tUrDO2kA8BN39JiszpzobRuUxGrAd11Hex7O5Dvp8Lcg%3D%3D'
url6 = 'https://ifttt.com/services/smartthings/more?exclude_applets=NyGhjenq,dL4peb2W,vs2NuKkR,qmrzQGhq,CKibyjSF,Cbuk2SUH,Xe7VTKCr,480986p,uhfavDW7,480982p,156899p,170044p,RtT8pJak,pu35Hxq9,114080p,im6FqC9y,TwQVj9iB,zr5HiefS,202191p,qmrzQGhq,413209p,114085p,CKibyjSF,125427p,vs2NuKkR,pGRqB9X3,480983p,iGUjZr8W,372977p,yMnbLQh5,349425p,uvwyxW8D,YZrvGLQP,mHEw9K7k,115639p,297748p,170045p,369465p,282644p,346606p,139772p,yrzyAbnp,374817p,Bcx2b9Uy,437159p,420034p,354274p,365679p,114084p,333387p,bZT5r7Ds,198215p,437163p,115640p,237769p,Mt9Gfqc5,435669p,373750p,aQzk4ry6,umfL4XaW,147389p,420121p,376197p,144215p,419794p,NKXFCrTA,JNiLfJjC,nmuxNcET,402519p,453102p,193627p,445967p,115669p,467096p,128715p,ZtSKP37Q,268150p,120047p,zpaKXkH8,Xhpg6uLZ,DAzGxi2h,Th2tnF7b,372070p,428332p,428329p,383273p,125431p,473774p,BT9nXDWz,xsUN2m4x,BFEB7vRZ,Pv9ZhsVd,u6NikWc8,aTMxtFVm,SsRzZ5Ed,wtGqhucA,nUL3zeBg,zXU6PYHS,p5xi3DNS,eq9WyX8z,hvhTJjUr,sUQnzrM6,LYxCTXr8,HMdVP2ZJ,aLwFYDc4,bidMGsib,j6RtfJTk,VtJ6qxiY,cCnX2Nid,eaxHREnJ,miLTfu45,Nb3kPiR2,efBcnTPu,e2NTWcGr,cUL67SKi,rDMwc3nk,y6sXqp2m,vpJdsZbX,RDpNynKU,Pub9QDSE,DezapTYA,B7ah8nX6,jNihMXcq,PcwJ9i3X,zxKNdXLy,KQ9v8BzE,hiY94Srg,ZHnUWjVR,w5G2cuiR,eXeyv2KS,A4ubWDkp&offset=131&authenticity_token=VzrFFKm6n0u9OuG8LskWGUXnd36DTG1H5l1owYPQy8tUrDO2kA8BN39JiszpzobRuUxGrAd11Hex7O5Dvp8Lcg%3D%3D'
url7 = 'https://ifttt.com/services/smartthings/more?exclude_applets=NyGhjenq,dL4peb2W,vs2NuKkR,qmrzQGhq,CKibyjSF,Cbuk2SUH,Xe7VTKCr,480986p,uhfavDW7,480982p,156899p,170044p,RtT8pJak,pu35Hxq9,114080p,im6FqC9y,TwQVj9iB,zr5HiefS,202191p,qmrzQGhq,413209p,114085p,CKibyjSF,125427p,vs2NuKkR,pGRqB9X3,480983p,iGUjZr8W,372977p,yMnbLQh5,349425p,uvwyxW8D,YZrvGLQP,mHEw9K7k,115639p,297748p,170045p,369465p,282644p,346606p,139772p,yrzyAbnp,374817p,Bcx2b9Uy,437159p,420034p,354274p,365679p,114084p,333387p,bZT5r7Ds,198215p,437163p,115640p,237769p,Mt9Gfqc5,435669p,373750p,aQzk4ry6,umfL4XaW,147389p,420121p,376197p,144215p,419794p,NKXFCrTA,JNiLfJjC,nmuxNcET,402519p,453102p,193627p,445967p,115669p,467096p,128715p,ZtSKP37Q,268150p,120047p,zpaKXkH8,Xhpg6uLZ,DAzGxi2h,Th2tnF7b,372070p,428332p,428329p,383273p,125431p,473774p,BT9nXDWz,xsUN2m4x,BFEB7vRZ,Pv9ZhsVd,u6NikWc8,aTMxtFVm,SsRzZ5Ed,wtGqhucA,nUL3zeBg,zXU6PYHS,p5xi3DNS,eq9WyX8z,hvhTJjUr,sUQnzrM6,LYxCTXr8,HMdVP2ZJ,aLwFYDc4,bidMGsib,j6RtfJTk,VtJ6qxiY,cCnX2Nid,eaxHREnJ,miLTfu45,Nb3kPiR2,efBcnTPu,e2NTWcGr,cUL67SKi,rDMwc3nk,y6sXqp2m,vpJdsZbX,RDpNynKU,Pub9QDSE,DezapTYA,B7ah8nX6,jNihMXcq,PcwJ9i3X,zxKNdXLy,KQ9v8BzE,hiY94Srg,ZHnUWjVR,w5G2cuiR,eXeyv2KS,A4ubWDkp,zUatymCr,3UMhLxxJ,190798p,GAFhDb2W,QiW7ZLTA,fS2NFLiK,jZTEL9dQ,Lyfg2YER,JFTERe5d,dimWZTFE,FJcwD4uP,L5YnqL7c,jKEjns4S,uuN6caYQ,H6dVq7DG,g5UVn8kK,454598p,EivupxNJ,e9KVcT5F,ufaF9KSr,ZB5yP2Rk,sufJiMZg,115637p,YsugdWM7&offset=155&authenticity_token=VzrFFKm6n0u9OuG8LskWGUXnd36DTG1H5l1owYPQy8tUrDO2kA8BN39JiszpzobRuUxGrAd11Hex7O5Dvp8Lcg%3D%3D'
url8 = 'https://ifttt.com/services/smartthings/more?exclude_applets=NyGhjenq,dL4peb2W,vs2NuKkR,qmrzQGhq,CKibyjSF,Cbuk2SUH,Xe7VTKCr,480986p,uhfavDW7,480982p,156899p,170044p,RtT8pJak,pu35Hxq9,114080p,im6FqC9y,TwQVj9iB,zr5HiefS,202191p,qmrzQGhq,413209p,114085p,CKibyjSF,125427p,vs2NuKkR,pGRqB9X3,480983p,iGUjZr8W,372977p,yMnbLQh5,349425p,uvwyxW8D,YZrvGLQP,mHEw9K7k,115639p,297748p,170045p,369465p,282644p,346606p,139772p,yrzyAbnp,374817p,Bcx2b9Uy,437159p,420034p,354274p,365679p,114084p,333387p,bZT5r7Ds,198215p,437163p,115640p,237769p,Mt9Gfqc5,435669p,373750p,aQzk4ry6,umfL4XaW,147389p,420121p,376197p,144215p,419794p,NKXFCrTA,JNiLfJjC,nmuxNcET,402519p,453102p,193627p,445967p,115669p,467096p,128715p,ZtSKP37Q,268150p,120047p,zpaKXkH8,Xhpg6uLZ,DAzGxi2h,Th2tnF7b,372070p,428332p,428329p,383273p,125431p,473774p,BT9nXDWz,xsUN2m4x,BFEB7vRZ,Pv9ZhsVd,u6NikWc8,aTMxtFVm,SsRzZ5Ed,wtGqhucA,nUL3zeBg,zXU6PYHS,p5xi3DNS,eq9WyX8z,hvhTJjUr,sUQnzrM6,LYxCTXr8,HMdVP2ZJ,aLwFYDc4,bidMGsib,j6RtfJTk,VtJ6qxiY,cCnX2Nid,eaxHREnJ,miLTfu45,Nb3kPiR2,efBcnTPu,e2NTWcGr,cUL67SKi,rDMwc3nk,y6sXqp2m,vpJdsZbX,RDpNynKU,Pub9QDSE,DezapTYA,B7ah8nX6,jNihMXcq,PcwJ9i3X,zxKNdXLy,KQ9v8BzE,hiY94Srg,ZHnUWjVR,w5G2cuiR,eXeyv2KS,A4ubWDkp,zUatymCr,3UMhLxxJ,190798p,GAFhDb2W,QiW7ZLTA,fS2NFLiK,jZTEL9dQ,Lyfg2YER,JFTERe5d,dimWZTFE,FJcwD4uP,L5YnqL7c,jKEjns4S,uuN6caYQ,H6dVq7DG,g5UVn8kK,454598p,EivupxNJ,e9KVcT5F,ufaF9KSr,ZB5yP2Rk,sufJiMZg,115637p,YsugdWM7,RNWJaAXr,zyYGW2HC,X68k2apw,rT8Bmk2j,FkChH73E,m2DqRzxh,vmKf4j5e,KFNzaixe,190960p,X6tWANDS,nzMX8H7n,sVNnf2KD,WziHrSD9,Qg2H6kqh,265255p,EMeVQR9z,F3Vkw4yu,R68vPB4D,y69sXfkn,Cp8WXhGZ,H4pCQbMF,t2pgkEdM,tNC2Jmpz,207926p&offset=179&authenticity_token=VzrFFKm6n0u9OuG8LskWGUXnd36DTG1H5l1owYPQy8tUrDO2kA8BN39JiszpzobRuUxGrAd11Hex7O5Dvp8Lcg%3D%3D'
url9 = 'https://ifttt.com/services/smartthings/more?exclude_applets=NyGhjenq,dL4peb2W,vs2NuKkR,qmrzQGhq,CKibyjSF,Cbuk2SUH,Xe7VTKCr,480986p,uhfavDW7,480982p,156899p,170044p,RtT8pJak,pu35Hxq9,114080p,im6FqC9y,TwQVj9iB,zr5HiefS,202191p,qmrzQGhq,413209p,114085p,CKibyjSF,125427p,vs2NuKkR,pGRqB9X3,480983p,iGUjZr8W,372977p,yMnbLQh5,349425p,uvwyxW8D,YZrvGLQP,mHEw9K7k,115639p,297748p,170045p,369465p,282644p,346606p,139772p,yrzyAbnp,374817p,Bcx2b9Uy,437159p,420034p,354274p,365679p,114084p,333387p,bZT5r7Ds,198215p,437163p,115640p,237769p,Mt9Gfqc5,435669p,373750p,aQzk4ry6,umfL4XaW,147389p,420121p,376197p,144215p,419794p,NKXFCrTA,JNiLfJjC,nmuxNcET,402519p,453102p,193627p,445967p,115669p,467096p,128715p,ZtSKP37Q,268150p,120047p,zpaKXkH8,Xhpg6uLZ,DAzGxi2h,Th2tnF7b,372070p,428332p,428329p,383273p,125431p,473774p,BT9nXDWz,xsUN2m4x,BFEB7vRZ,Pv9ZhsVd,u6NikWc8,aTMxtFVm,SsRzZ5Ed,wtGqhucA,nUL3zeBg,zXU6PYHS,p5xi3DNS,eq9WyX8z,hvhTJjUr,sUQnzrM6,LYxCTXr8,HMdVP2ZJ,aLwFYDc4,bidMGsib,j6RtfJTk,VtJ6qxiY,cCnX2Nid,eaxHREnJ,miLTfu45,Nb3kPiR2,efBcnTPu,e2NTWcGr,cUL67SKi,rDMwc3nk,y6sXqp2m,vpJdsZbX,RDpNynKU,Pub9QDSE,DezapTYA,B7ah8nX6,jNihMXcq,PcwJ9i3X,zxKNdXLy,KQ9v8BzE,hiY94Srg,ZHnUWjVR,w5G2cuiR,eXeyv2KS,A4ubWDkp,zUatymCr,3UMhLxxJ,190798p,GAFhDb2W,QiW7ZLTA,fS2NFLiK,jZTEL9dQ,Lyfg2YER,JFTERe5d,dimWZTFE,FJcwD4uP,L5YnqL7c,jKEjns4S,uuN6caYQ,H6dVq7DG,g5UVn8kK,454598p,EivupxNJ,e9KVcT5F,ufaF9KSr,ZB5yP2Rk,sufJiMZg,115637p,YsugdWM7,RNWJaAXr,zyYGW2HC,X68k2apw,rT8Bmk2j,FkChH73E,m2DqRzxh,vmKf4j5e,KFNzaixe,190960p,X6tWANDS,nzMX8H7n,sVNnf2KD,WziHrSD9,Qg2H6kqh,265255p,EMeVQR9z,F3Vkw4yu,R68vPB4D,y69sXfkn,Cp8WXhGZ,H4pCQbMF,t2pgkEdM,tNC2Jmpz,207926p,441830p,430836p,430835p,cwnJdN7g,P2DNnhpt,444331p,H5X83xLe,UXqU3aTy,285828p,cykY9LwF,vYv7xFnp,yPRQS6T5,x4Ri59aK,170037p,R6xRMdb8,148502p,369418p,guYNT9bH,QfmT9AgP,463121p,197323p,z2eH6aW3,419792p,bTauHJs5&offset=203&authenticity_token=VzrFFKm6n0u9OuG8LskWGUXnd36DTG1H5l1owYPQy8tUrDO2kA8BN39JiszpzobRuUxGrAd11Hex7O5Dvp8Lcg%3D%3D'
url10 = 'https://ifttt.com/services/smartthings/more?exclude_applets=NyGhjenq,dL4peb2W,vs2NuKkR,qmrzQGhq,CKibyjSF,Cbuk2SUH,Xe7VTKCr,480986p,uhfavDW7,480982p,156899p,170044p,RtT8pJak,pu35Hxq9,114080p,im6FqC9y,TwQVj9iB,zr5HiefS,202191p,qmrzQGhq,413209p,114085p,CKibyjSF,125427p,vs2NuKkR,pGRqB9X3,480983p,iGUjZr8W,372977p,yMnbLQh5,349425p,uvwyxW8D,YZrvGLQP,mHEw9K7k,115639p,297748p,170045p,369465p,282644p,346606p,139772p,yrzyAbnp,374817p,Bcx2b9Uy,437159p,420034p,354274p,365679p,114084p,333387p,bZT5r7Ds,198215p,437163p,115640p,237769p,Mt9Gfqc5,435669p,373750p,aQzk4ry6,umfL4XaW,147389p,420121p,376197p,144215p,419794p,NKXFCrTA,JNiLfJjC,nmuxNcET,402519p,453102p,193627p,445967p,115669p,467096p,128715p,ZtSKP37Q,268150p,120047p,zpaKXkH8,Xhpg6uLZ,DAzGxi2h,Th2tnF7b,372070p,428332p,428329p,383273p,125431p,473774p,BT9nXDWz,xsUN2m4x,BFEB7vRZ,Pv9ZhsVd,u6NikWc8,aTMxtFVm,SsRzZ5Ed,wtGqhucA,nUL3zeBg,zXU6PYHS,p5xi3DNS,eq9WyX8z,hvhTJjUr,sUQnzrM6,LYxCTXr8,HMdVP2ZJ,aLwFYDc4,bidMGsib,j6RtfJTk,VtJ6qxiY,cCnX2Nid,eaxHREnJ,miLTfu45,Nb3kPiR2,efBcnTPu,e2NTWcGr,cUL67SKi,rDMwc3nk,y6sXqp2m,vpJdsZbX,RDpNynKU,Pub9QDSE,DezapTYA,B7ah8nX6,jNihMXcq,PcwJ9i3X,zxKNdXLy,KQ9v8BzE,hiY94Srg,ZHnUWjVR,w5G2cuiR,eXeyv2KS,A4ubWDkp,zUatymCr,3UMhLxxJ,190798p,GAFhDb2W,QiW7ZLTA,fS2NFLiK,jZTEL9dQ,Lyfg2YER,JFTERe5d,dimWZTFE,FJcwD4uP,L5YnqL7c,jKEjns4S,uuN6caYQ,H6dVq7DG,g5UVn8kK,454598p,EivupxNJ,e9KVcT5F,ufaF9KSr,ZB5yP2Rk,sufJiMZg,115637p,YsugdWM7,RNWJaAXr,zyYGW2HC,X68k2apw,rT8Bmk2j,FkChH73E,m2DqRzxh,vmKf4j5e,KFNzaixe,190960p,X6tWANDS,nzMX8H7n,sVNnf2KD,WziHrSD9,Qg2H6kqh,265255p,EMeVQR9z,F3Vkw4yu,R68vPB4D,y69sXfkn,Cp8WXhGZ,H4pCQbMF,t2pgkEdM,tNC2Jmpz,207926p,441830p,430836p,430835p,cwnJdN7g,P2DNnhpt,444331p,H5X83xLe,UXqU3aTy,285828p,cykY9LwF,vYv7xFnp,yPRQS6T5,x4Ri59aK,170037p,R6xRMdb8,148502p,369418p,guYNT9bH,QfmT9AgP,463121p,197323p,z2eH6aW3,419792p,bTauHJs5,205033p,115635p,jMnm8VfX,188827p,zcCFy7bH,342285p,260007p,188828p,341896p,399472p,307835p,114089p,350810p,341727p,399473p,203787p,157029p,418634p,119400p,114091p,157030p,139966p,418635p,119401p&offset=227&authenticity_token=VzrFFKm6n0u9OuG8LskWGUXnd36DTG1H5l1owYPQy8tUrDO2kA8BN39JiszpzobRuUxGrAd11Hex7O5Dvp8Lcg%3D%3D'
url11 = 'https://ifttt.com/services/smartthings/more?exclude_applets=NyGhjenq,dL4peb2W,vs2NuKkR,qmrzQGhq,CKibyjSF,Cbuk2SUH,Xe7VTKCr,480986p,uhfavDW7,480982p,156899p,170044p,RtT8pJak,pu35Hxq9,114080p,im6FqC9y,TwQVj9iB,zr5HiefS,202191p,qmrzQGhq,413209p,114085p,CKibyjSF,125427p,vs2NuKkR,pGRqB9X3,480983p,iGUjZr8W,372977p,yMnbLQh5,349425p,uvwyxW8D,YZrvGLQP,mHEw9K7k,115639p,297748p,170045p,369465p,282644p,346606p,139772p,yrzyAbnp,374817p,Bcx2b9Uy,437159p,420034p,354274p,365679p,114084p,333387p,bZT5r7Ds,198215p,437163p,115640p,237769p,Mt9Gfqc5,435669p,373750p,aQzk4ry6,umfL4XaW,147389p,420121p,376197p,144215p,419794p,NKXFCrTA,JNiLfJjC,nmuxNcET,402519p,453102p,193627p,445967p,115669p,467096p,128715p,ZtSKP37Q,268150p,120047p,zpaKXkH8,Xhpg6uLZ,DAzGxi2h,Th2tnF7b,372070p,428332p,428329p,383273p,125431p,473774p,BT9nXDWz,xsUN2m4x,BFEB7vRZ,Pv9ZhsVd,u6NikWc8,aTMxtFVm,SsRzZ5Ed,wtGqhucA,nUL3zeBg,zXU6PYHS,p5xi3DNS,eq9WyX8z,hvhTJjUr,sUQnzrM6,LYxCTXr8,HMdVP2ZJ,aLwFYDc4,bidMGsib,j6RtfJTk,VtJ6qxiY,cCnX2Nid,eaxHREnJ,miLTfu45,Nb3kPiR2,efBcnTPu,e2NTWcGr,cUL67SKi,rDMwc3nk,y6sXqp2m,vpJdsZbX,RDpNynKU,Pub9QDSE,DezapTYA,B7ah8nX6,jNihMXcq,PcwJ9i3X,zxKNdXLy,KQ9v8BzE,hiY94Srg,ZHnUWjVR,w5G2cuiR,eXeyv2KS,A4ubWDkp,zUatymCr,3UMhLxxJ,190798p,GAFhDb2W,QiW7ZLTA,fS2NFLiK,jZTEL9dQ,Lyfg2YER,JFTERe5d,dimWZTFE,FJcwD4uP,L5YnqL7c,jKEjns4S,uuN6caYQ,H6dVq7DG,g5UVn8kK,454598p,EivupxNJ,e9KVcT5F,ufaF9KSr,ZB5yP2Rk,sufJiMZg,115637p,YsugdWM7,RNWJaAXr,zyYGW2HC,X68k2apw,rT8Bmk2j,FkChH73E,m2DqRzxh,vmKf4j5e,KFNzaixe,190960p,X6tWANDS,nzMX8H7n,sVNnf2KD,WziHrSD9,Qg2H6kqh,265255p,EMeVQR9z,F3Vkw4yu,R68vPB4D,y69sXfkn,Cp8WXhGZ,H4pCQbMF,t2pgkEdM,tNC2Jmpz,207926p,441830p,430836p,430835p,cwnJdN7g,P2DNnhpt,444331p,H5X83xLe,UXqU3aTy,285828p,cykY9LwF,vYv7xFnp,yPRQS6T5,x4Ri59aK,170037p,R6xRMdb8,148502p,369418p,guYNT9bH,QfmT9AgP,463121p,197323p,z2eH6aW3,419792p,bTauHJs5,205033p,115635p,jMnm8VfX,188827p,zcCFy7bH,342285p,260007p,188828p,341896p,399472p,307835p,114089p,350810p,341727p,399473p,203787p,157029p,418634p,119400p,114091p,157030p,139966p,418635p,119401p,385941p,398805p,160242p,398806p,117365p,348474p,115673p,328442p,431236p,368576p,234664p,380489p,425910p,141254p,218886p,115693p,141252p,125433p,285843p,149685p,M9ve8gyP,114146p,191812p&offset=250&authenticity_token=VzrFFKm6n0u9OuG8LskWGUXnd36DTG1H5l1owYPQy8tUrDO2kA8BN39JiszpzobRuUxGrAd11Hex7O5Dvp8Lcg%3D%3D'
# analysis()
# more(url1)

# 获取iftt smartthings 规则
# path = './html'
# files= os.listdir(path)
# for file in files:
#   more('./html/'+file)

#去重
# file = open('ifttt-smart.txt')
# s = set()
# count = 0
# for line in file:
#   s.add(line)
#   count += 1
# file.close()


# print('count', count)
# print('len(s)', len(s))
# print('==', count == len(s))

##写入文件
# f = open('ifttt-smartthings-dedump.txt','w')
# f.write(''.join(s))
# f.close()
## 找含有when到规则
file = open('ifttt-smartthings-dedump.txt','r')
f = open('ifttt-smartthings-when.txt', 'w')
s = set()
for line in file:
  if 'when' in line:
    s.add(line)
f.write(''.join(s))
f.close()
file.close()
