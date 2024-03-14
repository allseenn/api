import requests
import clickhouse_driver
from tokens import CH_API_ID, CH_API_KEY, CH_ORG_ID, CH_SRV_ID

# https://api.clickhouse.cloud/v1/organizations

r = requests.get(
    f'https://api.clickhouse.cloud/v1/organizations/{CH_ORG_ID}/services/{CH_SRV_ID}',
    auth=(CH_API_ID, CH_API_KEY)
)


# r = requests.patch(
#     f'https://api.clickhouse.cloud/v1/organizations/{CH_ORG_ID}/services/{CH_SRV_ID}/state',
#     auth=(CH_API_ID, CH_API_KEY),
#     json={'command': 'start'}
# )


print(r.text)

