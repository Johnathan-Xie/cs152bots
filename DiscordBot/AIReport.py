from enum import Enum, auto
import discord
import re


    
class AIReport:

    def __init__(self, client, target_message, score):
        self.client = client
        self.target_message = target_message
        certainty_value = None
        self.reporting_user = "AI Bot"
        self.score = score


   

    async def handle_message(self, message):
        '''
        This function makes up the meat of the user-side reporting flow. It defines how we transition between states and what 
        prompts to offer at each of those states. You're welcome to change anything you want; this skeleton is just here to
        get you started and give you a model for working with Discord. 
        '''

        