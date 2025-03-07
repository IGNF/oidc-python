from pprint import pprint

from ign_keycloak.KeycloakService import KeycloakService


KEYCLOAK_SERVER_URI = "https://sso.com/"
KEYCLOAK_CLIENT_ID = "client-id"  # <-- Remplacer par le client_id de votre application
KEYCLOAK_CLIENT_SECRET = "client-secret"  # <-- Remplacer par le client_secret de votre application
KEYCLOAK_REALM_NAME = "realm-name"  # <-- Remplacer par le nom de votre realm

# renseigner le proxy si besoin
# PROXY = "http://proxy.com:3128"
# proxies = {"http": PROXY, "https": PROXY}


keycloak_service = KeycloakService(
    KEYCLOAK_SERVER_URI,
    KEYCLOAK_REALM_NAME,
    KEYCLOAK_CLIENT_ID,
    client_secret=KEYCLOAK_CLIENT_SECRET,
    # proxies=proxies,
    ssl_verify=False,
)
# r = keycloak_service.get_well_known_config()
# pprint(r)

r = keycloak_service.get_authorization_code(["email", "profile", "openid", "roles"])
pprint(r)

r = keycloak_service.get_access_token(r["code"][0])
pprint(r)

r = keycloak_service.get_userinfo(r["access_token"])
pprint(r)

keycloak_service.logout()
