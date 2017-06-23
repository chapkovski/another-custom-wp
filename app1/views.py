from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import channels
import json
# we import this to get the channel name to push status updates to the waiting Page
from otree.common_internal import channels_group_by_arrival_time_group_name as chname
class MyPage(Page):
    def before_next_page(self):
        # we get the list of those players who are not last ones
        not_last_ones = [p for p in self.subsession.get_players() if
            p.last_one == False]
        if len(self.subsession.get_players()) - 1 > len(not_last_ones):
            self.player.last_one = False
        else:
            # if this player is the last one in session...
            self.player.last_one = True
            # we set session level var to True so other players arriving to
            # app3.WaitPage later can go on immediately
            self.session.vars['gofurther'] = True
            # somehow the status is not updated automatically via idmap
            # so do save()
            self.session.save()
            # we get the index of current WaitPage via session.vars
            # (it is set by players arriving to app3.WaitPage)
            cur_wp_index = self.session.vars.get('wp_index')
            # if someone has already arrived the index is set and we
            # can get channel name using index and current session pk
            if cur_wp_index:
                curch = chname(self.session.pk, cur_wp_index)
                channels.Group(curch).send(
                        {'text': json.dumps(
                            {'status': 'ready'})}
                    )



class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    MyPage,
    # ResultsWaitPage,
    # Results
]
