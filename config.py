#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os


class DefaultConfig:
    """Configuration for the bot."""

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    #LUIS_APP_ID = os.environ.get("LuisAppId", "")
    #LUIS_API_KEY = os.environ.get("LuisAPIKey", "")
    # LUIS endpoint host name, ie "westus.api.cognitive.microsoft.com"
    #LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "")
    #APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get("AppInsightsInstrumentationKey", "")
    LUIS_API_KEY = '033c3af6d53b49c7afa2cbe5637d578c'
    LUIS_API_HOST_NAME = 'p10evinstance.cognitiveservices.azure.com/'
    LUIS_APP_ID = '077e5fce-c99c-4e89-909f-dd6bd6807e85'
    APPINSIGHTS_INSTRUMENTATION_KEY = '32311f47-6b7f-436b-beef-96e2d72c5f07'
    


