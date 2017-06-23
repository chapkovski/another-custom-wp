from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Philip Chapkovski, UZH''

doc = """
Custom WaitPage to push players based on status of players in previous apps
"""


class Constants(BaseConstants):
    name_in_url = 'app3'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
