import requests

def getUsersPerGrp(instance, userMail, group_id, token_id):
    users_logins = []
    users = []
    id = 1

    
    try:
        while True:
            url = f"https://{instance}.zendesk.com/api/v2/groups/{group_id}/users.json?page={id}"
            res = requests.get(url, auth=(userMail, token_id))
            data = res.json()
            users.extend(data['users'])

            if not data.get('next_page'):
                break

            id += 1
        
        print(len(users))

        for user in users:
            last_login = str(user.get('last_login_at', '')).split("T")[0]
            name = user.get('name', '')
            
            users_logins.append({
                'name': name,
                'email': user.get('email', ''),
                'role': user.get('role', ''),
                'created_at': str(user.get('created_at', '')).split("T")[0],
                'last_login': last_login,
                'Location': user.get('time_zone', '')
            })
        
        
        sorted_logins = sorted(users_logins, key=lambda x: x.get('name', ''), reverse=False)
        
        return sorted_logins

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

token_id = ''
userMail = ''

logins = getUsersPerGrp('sunkingpaygo', userMail, 24452815, token_id)
print(logins)
