import smartsheet

smart = smartsheet.Smartsheet(Bearer token)
Webhook = smart.Webhooks.create_webhook(
  smartsheet.models.Webhook({
    'name': Webhook_name,
    'callbackUrl': Callback URL,
    'scope': 'sheet',
    'scopeObjectId': Sheet ID,
    'events': ['*.*'],
    'version': 1}))
print(Webhook.data.id)
