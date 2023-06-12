import json

import requests
import sqlite3
from by_id_database import *

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://obd.hcraontario.ca/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'Referer': 'https://obd.hcraontario.ca/',
    'Connection': 'keep-alive',
    'TE': 'trailers',
}
cookies = {
    'visid_incap_2269415': 'D9Jm6++GT7mJTTBWSii0xhuCpGEAAAAAQUIPAAAAAAAr35YgIOQbl/mz03Tc9iBd',
    'nlbi_2269415': 'V24SCPBQ4B6Cl08CkG5lugAAAADupUSZeYe9lTkMKnfidRtC',
    'incap_ses_1286_2269415': '8mWhcfhHpXZVkuMFf8rYERuCpGEAAAAAvrXEXLq+rrXOtaETv/vPrg==',
    'incap_ses_1119_2269415': 'WyRiAScPKAI5LYkpAn2HDx2CpGEAAAAATIHCGoAp9SDUwSfN7kSdEg==',
    'nlbi_2269415_2147483646': 'PmxZPQu+/zIUwIt7kG5lugAAAAA242oko3AxMkoqxUNKfodO',
    '_ga_Y07J3B53QP': 'GS1.1.1638171168.1.1.1638171206.22',
    '_ga': 'GA1.2.228661505.1638171169',
    '_gid': 'GA1.2.31054031.1638171170',
    'reese84': '3:yU26bpLb9/7KfIaw9BEE6A==:cJy8eRY3gikUStcETx96PQwED18AAnFQa9VjUnZMFp5d9PG4ha0FdLa3A6cGljQgMrfgLeKVBCTxSETcaf3ump80fWraLLWldILRX83SYNoobM6wp46GEk2KbLnOsa6mhcrARhjqUHJyyyOZTChXlgdj0exmV6IUcfaZehF4TmURsMv3NrVvQvOjorxKQZ5VV6qHP8Wbx3Hn611rWPHUtuTbN8fVX51pyCassmKOmvWBVL21bjVM0HgLktS8+/ClCBAt4G+pmkzcxyaiacV5WD4BqslofKNfRsp9p8BCGpmmzk3gbOUajBXfON64DuhX5j2A3Bt5hhoFNtftVOXJsq5ALRI+oEmL01YnbmqbZ/iv+ddAzE6rtHir2Rnbi2jGNPUcW/bem/qU3oSlailroVZi91jWv1suIgfQMzewp2w7RmmzBGPUXPW9ddH77uu3:Nz1V0usvX8L6K8x0oxaJwM3XPrxMoVNWEdGW7puF2PA=',
    'gig_bootstrap_3_mrQiIl6ov44s2X3j6NGWVZ9SDDtplqV7WgdcyEpGYnYxl7ygDWPQHqQqtpSiUfko': 'gigya-pr_ver4',
    '_fbp': 'fb.1.1638171179526.1068905449',
    '_4c_': 'fVNNa%2BMwEP0rQQs91allW5YcyKEkbAn0ULZd9lgUaZyIOJaQFbvZ0v%2B%2Bo6yTQMuuD0Lz5s3ozYffybCFlsxomQvKKeVVlee3ZAfHjszeiXLx7ONx8A2ZkW0Irpvd3Q3DMPUgm2D9VMm7vXTfegPDvDFduHm2PszLZHnz5K0DH44vRwcP3h7cajmnF%2FQZpFfb6FtphF%2B8bDupgrHtiGU3i4P30KrjfHG%2FJLdEWQ0oglbTapqiHX6jlafxCi2qJM5rvD%2Fcv%2F5cLdHMMlGWlKVseq6vrNDvvNUHFV4DPoOsAdaTTu%2FQoaE3Cl4Ho8M2vpOX5RXdgtlsA8K8FBF1PlLwNphW2%2BFz1IheosoiR%2FRRtpuD3MAY%2Bmg3G9CTFU6A1LLpADFsT29aFSloLeyhDf6IxpPcYXNli%2BAP6IyGNhjZWL%2Bw%2Bz14o2Scj796kLf2dugg6vxuPNT2bVIVCFucLfl10tehiR7ANvt%2FjxdJnQlwyn8GRww35QonJ9j1Y3WNRVExCqLoDk6zvbLJxy15%2B7t6GeOMizTlONOAdYiySOOHDG%2F0uINEK8pqofOEqyJPCiYgESqrElbnKk0LUSseyzvlLFhVcMp5lcckvbnkyJSWnK6TOlN1UpSUJhWjdULTUhfVmjMhGLnoojyrMAdnoy4qzrJcM2akV7JgjMcf6EwuLkW4%2Fgv7VDKyi68la%2Bh2wbqxTf%2BJZZ9jPz7%2BAA%3D%3D',
    'ASP.NET_SessionId': 'pp5gkqa0ibl50ghblfdpfpf5',
    'visid_incap_2271082': 'shr0EhE4TB2NemfVFsGGAUaCpGEAAAAAQUIPAAAAAAA2KRAXW5tAErKJWt4vgYUy',
    'nlbi_2271082': 'auwGe4eHaXq6VjRMcbDG1QAAAADOR1/BbCuOvIvmlbp7ZKGt',
    'incap_ses_1119_2271082': 'k7JkaKsiO1oAqokpAn2HD0eCpGEAAAAANO62bFMKOap67qsSSbEh3A==',
}

conn = sqlite3.connect('hcantario.db')
cursor = conn.cursor()
select_query = "SELECT NAME, ACCOUNTNUMBER FROM Company"
cursor.execute(select_query)
rows = cursor.fetchall()
create_database()
i = 0
for row in rows:
    name, account_number = row
    url = 'https://obd.hcraontario.ca/api/buildersummary?id='+account_number+''
    response = requests.get(url, headers=headers, cookies=cookies)

    if response.status_code == 200:
        data = response.json()
        for obj in data:
            # Add two more fields to each object
            # obj.append({'NAME': name})
            # obj.add({'ACCOUNTNUMBER': account_number})

            obj['NAME'] = name
            obj['ACCOUNTNUMBER'] = account_number
            insert_data(obj)
            i +=1
            print(i)
        # Process the data as needed
    else:
        print('Request failed with status code:', response.status_code)

cursor.close()
conn.close()



