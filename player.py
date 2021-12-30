from bill import Bill

class Player:
    def __init__(self):
        self._total_rounds = 9
        self._cur_round = 1

        self._in_start_scene = True
        self._in_opening_scene = False
        self._in_game = False
        self._in_cut_scene = False
        self._in_end_scene = False

        self.bills = [Bill(x) for x in range(self._total_rounds)]
        self._cur_bill = self.bills[self._cur_round - 1]

        self._making_decision = False
        self._bill_approved = False
        self.score = { # 各項社會指標的分數
            "Economy": 40,
            "Gov_trust": 40,
            "Public_health": 40,
        }

    @property
    def making_decision(self):
        return self._making_decision

    @making_decision.setter
    def making_decision(self, value):
        assert type(value) == bool
        self._making_decision = value

    @property
    def bill_approved(self):
        return self._approve

    @bill_approved.setter
    def bill_approved(self, value):
        assert type(value) == bool
        self._approve = value

    @property
    def current_round(self):
        return self._cur_round

    @property
    def in_start_scene(self):
        return self._in_start_scene   
    @in_start_scene.setter
    def in_start_scene(self, value):
        assert type(value) == bool
        self._in_start_scene = value

    @property
    def in_opening_scene(self):
        return self._in_opening_scene
    @in_opening_scene.setter
    def in_opening_scene(self, value):
        assert type(value) == bool
        self._in_opening_scene = value

    @property
    def in_game(self):
        return self._in_game
    @in_game.setter
    def in_game(self, value):
        assert type(value) == bool
        self._in_game = value
    
    @property
    def in_cut_scene(self):
        return self._in_cut_scene
    @in_cut_scene.setter
    def in_cut_scene(self, value):
        assert type(value) == bool
        self._in_cut_scene = value

    @property
    def in_end_scene(self):
        return self._in_end_scene
    @in_end_scene.setter
    def in_end_scene(self, value):
        assert type(value) == bool
        self._in_end_scene = value

    @property
    def total_rounds(self):
        return self._total_rounds
    

    @property
    def cur_bill(self):
        return self._cur_bill

    # 通過一項議案
    def approve(self):
        # calculate impact
        # print result
        self._cur_round += 1

        self._making_decision = False
        self._in_game = False
        self._in_cut_scene = True
        self._approve = True

    # 否決一項議案
    def disapprove(self):
        # calculate impact
        # print result
        self._cur_round += 1

        self._making_decision = False
        self._in_game = False
        self._in_cut_scene = True
        self._approve = False

    def next_bill(self):
        self._cur_bill = self.bills[self._cur_round - 1]