import smartsheet

smart = smartsheet.Smartsheet(Bearer token)
Update = smart.Webhooks.update_webhook(
  Webhook_ID,
  smart.models.Webhook({'enabled': True}))
print(Update)
