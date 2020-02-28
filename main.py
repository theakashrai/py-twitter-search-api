import requests
import json
import webbrowser

with open('bt.json','r') as token_file:	
	bearer_json = json.load(token_file)
	tw_access_token = bearer_json['access_token']
user_search_keyword = input("Please input Keyword: ")
query_text = "from:"+ user_search_keyword + " lang:en"

bearer_tk = "Bearer " + tw_access_token
ep = "https://api.twitter.com/1.1/tweets/search/30day/dev.json"
ep_header = {"authorization": bearer_tk, "content-type": "application/json"}
ep_data = {"query":query_text , "maxResults": "100"}

response = requests.post(ep , json=ep_data , headers=ep_header)
if response.status_code==200:
	print('Success')
	
	jsonData = response.json()
	with open('response.json','w') as saveResponse:
		saveResponse.write(json.dumps(jsonData))
	print('Searching for tweets on topic: '+ user_search_keyword)
	htmlData = "<html><head><title>Search results on Twitter:</title></head><body><table>"
	for data in jsonData['results']:
		htmlData += "<tr><td><b>" + data["user"]["name"] + "</b></td></tr>"
		htmlData += "<tr><td>" + data["text"] + "</td></tr>"
		print(data['entities']['media'][0]['media_url'])
		for image_url in data['entities']['media']:
			htmlData += "<tr><td><img src='" + image_url['media_url'] + "'></td></tr>"
		htmlData += "<tr><td><img src='" + "" + "'></td></tr>"
		htmlData += "<tr><td>" + data["created_at"] + "</td></tr>"
	htmlData += "</table></body><html>"
	with open('index.html','w',encoding="utf-8") as saveResponse:
		saveResponse.write(htmlData)
	webbrowser.open('index.html', new=2)

	