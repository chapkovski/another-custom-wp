from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class WP(WaitPage):
    group_by_arrival_time = True
    def get_players_for_group(self, waiting_players):
        # as soon as someone arrives here
        # he or she sets wp_index so the last player in app1 can use it to
        # send the channels. message
        self.session.vars['wp_index'] = self._index_in_pages
        # if the last player sets the gofurther session var, we proceed,
        # otherwise just wait
        if self.session.vars.get('gofurther'):
            return waiting_players

class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    WP,
    ResultsWaitPage,
    Results
]
