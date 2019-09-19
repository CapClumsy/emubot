class masterclass(object):
    
    def __init__(self):
        self.EMUPRICE = 500
        self.MAXEMUS = 20
        self.MAXDEFENSE = 5
        self.MAXATTACK = 2 * self.MAXDEFENSE
        self.ATTACKCOOLDOWN = 14400.0
    
    def add_stats(self, user_id: int, amount: int, valuetype: str):
        if os.path.isfile("users.json"):
            try:
                with open('users.json', 'r') as fp:
                    users = json.load(fp)
                users[user_id][valuetype] += amount
                with open('users.json', 'w') as fp:
                    json.dump(users, fp, sort_keys=True, indent=4)
            except KeyError:
                with open('users.json', 'r') as fp:
                    users = json.load(fp)
                users[user_id] = {}
                #users[user_id][valuetype] = amount
                for vt in all_value_types:
                    if vt == valuetype:
                        users[user_id][valuetype] = amount
                    else:
                        users[user_id][vt] = 0
                with open('users.json', 'w') as fp:
                    json.dump(users, fp, sort_keys=True, indent=4)
        else:
            users = {user_id: {}}
            users[user_id][valuetype] = amount
            with open('users.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
    
    def get_stats(self, user_id: int, valuetype: str):
        if os.path.isfile('users.json'):
            try:
                with open('users.json', 'r') as fp:
                    users = json.load(fp)
                return users[user_id][valuetype]
            except KeyError:
                with open('users.json', 'r') as fp:
                    users = json.load(fp)
                users[user_id] = {}
                users[user_id][valuetype] = 0
                return 0
        else:
            return 0
