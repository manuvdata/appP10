#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os


class DefaultConfig:

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "dbd267a0-1141-4087-8cf2-a77bd477d6bc")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "lFN8Q~MYVNwQi5tkHDwgfUMLky4y5uRdwMYYkbDs")
    LUIS_APP_ID = os.environ.get("LuisAppId", "077e5fce-c99c-4e89-909f-dd6bd6807e85")
    #LUIS_API_KEY = os.environ.get("LuisAPIKey", "033c3af6d53b49c7afa2cbe5637d578c")
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "p10evinstance.cognitiveservices.azure.com/")
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get(
        "AppInsightsInstrumentationKey", "ed940d42-dd7b-4ff5-ba82-8c101cf0c538"
    )
    
