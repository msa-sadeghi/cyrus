import requests  

token = '674217a76d54a'  # کلید API خود را اینجا قرار دهید  
city = 'Tehran'  
 
url = f'https://one-api.ir/weather/?token={token}&action=current&city={city}'  

response = requests.get(url)  
data = response.json()  

if response.status_code == 200:  
    print(f"Current temperature in {city}: {data['main']['temp']}°C")  
else:  
    print("City not found!")