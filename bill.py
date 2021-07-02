import json

class Bill:
    def __init__(self, round):
        file = open('cut_scene_text.json', 'r', encoding='utf-8')
        round_data = json.load(file)["round" + str(round+1)]
        file.close()
        self.approve_text = round_data["text_1"]
        self.approve_score = round_data["score_1"]
        self.disapprove_text = round_data["text_2"]
        self.disapprove_score = round_data["score_2"]
