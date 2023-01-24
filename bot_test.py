import sys
import os
import json
import aiounittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from booking_details import BookingDetails
from config import DefaultConfig
from dialogs import BookingDialog, MainDialog
from flight_booking_recognizer import FlightBookingRecognizer
from helpers.luis_helper import LuisHelper, Intent

from botbuilder.dialogs.prompts import TextPrompt

from botbuilder.core import (
    TurnContext, 
    ConversationState, 
    MemoryStorage
)

from botbuilder.dialogs import DialogSet, DialogTurnStatus
from botbuilder.core.adapters import TestAdapter

class LuisTest(aiounittest.AsyncTestCase):

    # Test la requête vers Luis et la réponse obtenue avec ai
    async def test_luis_query(self):

        CONFIG = DefaultConfig()
        RECOGNIZER = FlightBookingRecognizer(CONFIG)

        async def exec_test(turn_context: TurnContext):

            intent, result = await LuisHelper.execute_luis_query(RECOGNIZER, turn_context)

            await turn_context.send_activity(
                json.dumps(
                    {
                        "intent": intent,
                        "booking_details": None if not hasattr(result, "__dict__") else result.__dict__,
                    }
                )
            )

        adapter = TestAdapter(exec_test)
        '''

        await adapter.test(
            "Hello",
            json.dumps(
                {
                    "intent": Intent.NONE_INTENT.value,
                    "booking_details": None,
                }
            ),
        )

        await adapter.test(
            "Hello, I want to go to Paris",
            json.dumps(
                {
                    "intent": Intent.BOOK_FLIGHT.value,
                    "booking_details": BookingDetails(
                        destination="Paris"
                    ).__dict__,
                }
            ),
        )
'''
        await adapter.test(
            "I want to book a flight from Berlin. My budget is 300$. I will leave the 20 december 2022 and coming back the 2 january 2023.",
            json.dumps(
                {
                    "intent": Intent.BOOK_FLIGHT.value,
                    "booking_details": BookingDetails(
                        origin = "Berlin",
                        start_date = "2022-12-20",
                        end_date = "2023-01-02",
                        budget = 300
                    ).__dict__,
                }
            ),
        )
