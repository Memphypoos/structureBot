# structureBot
Work in Progress...

Install instructions:
You will need to create a 'config.ini' file with the following (note you will need to know your refresh id):

[config]
eve_client: <client>
eve_secret_key: <key>
corporation_id: <corp id>
refresh_token: <refresh token>
slack_token: <slack token>
slack_channel: <slack channel>
scopes: esi-universe.read_structures.v1 esi-corporations.read_structures.v1 esi-characters.read_notifications.v1 esi-corporations.read_starbases.v1

This will pull back the System, Moon and Tower Size of all towers for your Corporation ID.
