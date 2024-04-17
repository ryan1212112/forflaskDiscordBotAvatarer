from flask import Flask,request
import requests


app = Flask(__name__)

if __name__ == '__main__':
    app.run()
    
@app.route('/change', methods=['GET'])
def ChangeDiscordBotAvatar():
    TOKEN = request.args.get('TOKEN')
    avatar_url = request.args.get('avatar_URL')
    avatar_data = requests.get(avatar_url).content
    headers = {
    'Authorization': f'Bot {TOKEN}',
    'Content-Type': 'application/json'
    }
    json = {
    'avatar': f'data:image/jpeg;base64,{avatar_data}'
    }
    response = requests.patch('https://discord.com/api/v6/users/@me', headers=headers, json=json)
    return response
