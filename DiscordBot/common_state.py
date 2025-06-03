from enum import Enum, auto

class State(Enum):
    REVIEW_START = auto()
    AWAITING_MESSAGE = auto()
    IN_REVIEW_FLOW = auto()
    REVIEW_COMPLETE = auto()
    PSEUDO_BAN_USER = auto()
    REMOVE_MESSAGE = auto()
    ADDING_INFO = auto()

class ReviewFlow:
    def __init__(self, config, start_state):
        self.config = config
        self.state = start_state
    
    def transition_state(self, message):
        for match, transition in self.config[self.state]["choices"]:
            if message.strip() == match:
                self.state = transition
                return True
        return False
    
    def get_current_message(self):
        return self.config[self.state]["message"]

    def in_terminal_state(self):
        return self.config[self.state].get("choices") is None

review_flow_config = {
    "initial_review": {
        "message": """Does the post violate the platform's guidelines on hate speech against LGBTQ+?\n"""
                   """1. Yes\n"""
                   """2. No\n""",
        "choices": [
            ("1", "rank_intensity"),
            ("2", "violate_other_policies"),
        ],
    },
    "rank_intensity": {
        "message": """Please rank the intensity of the violation\n"""
                   """1. Low Intensity\n"""
                   """2. Medium Intensity\n"""
                   """3. High Intensity\n""",
        "choices": [
            ("1", "remove_post_warn_user"),
            ("2", "remove_post_warn_user"),
            ("3", "remove_post_warn_user_high"),
        ]
    },
    "violate_other_policies": {
        "message": """Does this content violate other platform policies?\n"""
                   """1. Yes\n"""
                   """2. No\n""",
        "choices": [
            ("1", "violate_what_policies"),
            ("2", "reported_with_bad_intent"),
            
        ]
    },
    "violate_what_policies": {
        "message": """What platform policy does the content violate?\n"""
                   """1. Bullying or unwanted contact\n"""
                   """2. Suicide, self-injury, or eating disorders\n"""
                   """3. Selling or promoting restricted items\n"""
                   """4. Nudity or sexual activity\n"""
                   """5. Spam, fraud, or scam\n"""
                   """6. False Information""",
        "choices": [
            ("1", "rank_intensity"),
            ("2", "rank_intensity"),
            ("3", "rank_intensity"),
            ("4", "rank_intensity"),
            ("5", "rank_intensity"),
            ("6", "rank_intensity"),
        ]
    },
    "reported_with_bad_intent": {
        "message": """Does this message appear to have reported the message with harmful intent?\n"""
                   """1. Yes\n"""
                   """2. No\n""",
        "choices": [
            ("1", "warn_reporting_user"),
            ("2", "thanks_feedback_low"),
        ]
    },
    "warn_reporting_user": {
        "message": """**Thanks for reviewing this post.**\n"""
                   """The reporting user will be sent a warning \n"""
                   """Thanks for helping us keep Instagram a safe and supportive community.""",
    },
    "thanks_feedback_low":{
        "message": """Thanks for reviewing this post.\n"""
                     """We will continue to monitor this account for guideline violations.\n"""
                   """The necessary action will be taken to ensure community safety.\n"""
    },

    "remove_post_warn_user":{
        "message": """Thanks for reviewing this post\n"""
                     """The post will be removed and the user will receive a direct message warning\n"""
                   
    },

    "remove_post_warn_user_high":{
        "message": """Thanks for reviewing this post\n"""
                     """The post will be removed and the user will receive a direct message warning\n"""
                     """Additionaly, the account will be reviewed for suspension"""
                   
    },

    "remove_post":{
        "message": """Thanks for reviewing this post\n"""
                     """The user's post will be removed\n"""
                   
    }

}