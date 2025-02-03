########################### Getting Users names and last login per group ##########################

def getUsersPerGrp(instance, userMail, group_id, token_id):
    
    users_logins = []
    
    url = f"https://{instance}.zendesk.com/api/v2/groups/{group_id}/users"
    
    try:
        res = requests.get(url, auth=(userMail, token_id))
        data = res.json()
        users = data['users']

        for user in users:
            
            last_login = str(user['last_login_at']).split("T")[0]
            name = user['name']
            
            users_logins.append({
                'name': name,
                "email": user['email'],
                "role": user['role'],
                "created_at": user['created_at'].split("T")[0],
                "last login": last_login,
                "Location": user["time_zone"]
            })
            
        sorted_logins = sorted(users_logins, key=lambda x: list(x.values())[0], reverse=True)
        
        return sorted_logins
    
    except requests.exceptions.RequestException as e:
    
        print(f"Error: {e}")


token_id = ''

userMail = ''

logins = getUsersPerGrp('sunkingpaygong', userMail, 24452815, token_id)

output = [{'result': logins}]
