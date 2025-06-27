from pyzabbix import ZabbixAPI

class PatchedZabbixAPI(ZabbixAPI):
    def __init__(self, server_url):
        # No llamar super().__init__ con login
        self.url = server_url
        self.auth = None
        self.id = 0
        self._request_headers = {"Content-Type": "application/json-rpc"}
        self.timeout = 10

    def manual_login(self, username, password):
        self.auth = self.do_request('user.login', {
            "username": username,
            "password": password
        })['result']

# Configuración
ZABBIX_SERVER = "http://4.233.136.213/zabbix"
ZABBIX_USER = "johanbaq"
ZABBIX_PASS = "passwordmax"

# Crear instancia sin login automático
zapi = PatchedZabbixAPI(ZABBIX_SERVER)
zapi.manual_login(ZABBIX_USER, ZABBIX_PASS)

# Probar petición
users = zapi.user.get(output="extend")
for user in users:
    print(f"{user['userid']} - {user['alias']}")
