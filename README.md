
## Roblox Open Cloud API in Python

Roblox Open Cloud is an addition to the roblox developer workspace that allows automation of workflows to improve the efficiency of content creation and adds support for your needs to develop games on Roblox.

Open Cloud allows you to build your own tools and applications to access your roblox resources through web apis. Open Cloud is accessed through API keys or OAuth applications, and permissions can be set on api keys and authentications to determine the accessibility level of those authenticated applications and utilized api keys.

Additionally, webhooks can also be utilized to receive real-time notifications on third-party tools or custom endpoints.

## Installation

To install with pip, simply run the **one** of the following in a command prompt:

``pip install roblox-cloud-api``  
``pip3 install roblox-cloud-api``  

or if those do not work, **one** of the following;  

``py -m pip install roblox-cloud-api``  
``python -m pip install roblox-cloud-api``  
``py3 -m pip install roblox-cloud-api``  
``python3 -m pip install roblox-cloud-api``  

*covers the scenarios where the command prompt python keyword differs*

You can then import the package via
```py
import roblox_open_cloud
```

## Usage

**Use python's autocomplete to see what endpoints allow both or either USER_ACCOUNTs and API_KEYs.**

### Importing essentials
```py
from roblox_open_cloud import (
	API_KEY, # api keys
	USER_ACCOUNT, # roblox accounts
	KeyAPI, # validate api keys
	UserAPI, # validate roblox accounts
	OpenCloudAPI # open cloud api
)
```

#### Utilizing API Keys

```py
# Create an api key instance.
# Used to access resources.
api_key = API_KEY(
	api_key="", # api key credential
	creator_id="", # userId / groupId that owns the api key
)

# check if the api key is valid, only need to do once.
try:
	is_key_valid = KeyAPI.is_api_key_valid( api_key )
except Exception as e:
	print("Failed to check API_KEY validity with KeyAPI.")
	raise e # if the request itself failed, tell us why

if not is_key_valid:
	raise Exception("API Key is invalid.")

# now the key has been validated, we can do stuff with it.

# request to the MessagingService api and post a message
# raises an Exception if failed
try:
	OpenCloudAPI.MessagingService.publish_async(
		api_key, # api_key
		000000, # universe id
		"topic", # topic
		"message" # message
	)
	print("Published message using API Key!")
except Exception as e:
	print("Failed MessagingService message publish!")
	print(e)
```

#### Utilizing Roblox Accounts

```py
# Create an api key instance.
# Used to access resources.
account = USER_ACCOUNT(
	cookie="", # cookie
	user_id="", # userId
)

# check if the account is valid, only need to do once.
try:
	is_account_valid = UserAPI.is_user_account_valid( account )
except Exception as e:
	print("Failed to check USER_ACCOUNT validity with UserAPI.")
	raise e # if the request itself failed, tell us why

if not is_account_valid:
	raise Exception(f"User Account is invalid.")

# now the account has been validated, we can do stuff with it.

# request to the MessagingService api and post a message
# raises an Exception if failed
try:
	OpenCloudAPI.MessagingService.publish_async(
		account, # api_key
		000000, # universe id
		"topic", # topic
		"message" # message
	)
	print("Published message using API Key!")
except Exception as e:
	print("Failed MessagingService message publish!")
	print(e) # tells us the reason (Exceptions are raised based on webpoint responses.)
```

## Links

- Roblox Open Cloud Credentials Page:  
https://create.roblox.com/dashboard/credentials

- Roblox Open Cloud Overview Page:  
https://create.roblox.com/docs/cloud/open-cloud

- Roblox Open Cloud OAuth Page:  
https://create.roblox.com/docs/cloud/open-cloud/oauth2-overview

- Roblox Open Cloud Webhooks Page:  
https://create.roblox.com/docs/cloud/webhooks/webhook-notifications

- **TEST** PyPi Package Page  
https://test.pypi.org/project/roblox-cloud-api/

- **LIVE** PyPi Package Page  
https://www.pypi.org/project/roblox-cloud-api/

## Credits

**Package by SPOOK_EXE**  
https://github.com/SPOOKEXE  
https://www.roblox.com/users/1041213550/profile  

**Anamius - 'rbxmk' for parsing roblox files**  
https://github.com/Anaminus/rbxmk

## TODO
- Asset File API
- Asset Delivery API
- Decal ID to Image ID API
- Mesh Model to Mesh ID API
>
- Open Cloud Messaging API
- Open Cloud Datastore API
- Open Cloud Place Publishing API
>
- Open Cloud Operation IDs API
- Open Cloud Asset Upload API
>
- Update README.md with examples
- Update tests to cover each API (if possible)
