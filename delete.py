import smartsheet

smart = smartsheet.Smartsheet(Bearer token)
smart.Webhooks.delete_webhook(Webhook_ID)
