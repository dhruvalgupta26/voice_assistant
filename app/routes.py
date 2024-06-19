from flask import request, jsonify
from app import app
from automation.web_automation import login_to_website, open_tab

@app.route('/command', methods=['POST'])
def command():
    data = request.get_json()
    command = data.get('command', '')

    if 'login' in command:
        username = 'your_username'
        password = 'your_password'
        login_to_website(username, password)
        return jsonify({'status': 'Logged in successfully'})
    
    elif 'open' in command:
        tab_name = command.split('open')[-1].strip()
        open_tab(tab_name)
        return jsonify({'status': f'Opened {tab_name} tab'})

    return jsonify({'status': 'Command not recognized'})
