import pygame
from setting import *
from player import Player
from character import Character


# draw the window according to the overlapping order


def change_scene(player, start, opening, game, cut_scene, end_scene):
    player.in_start_scene = start
    player.in_opening_scene = opening
    player.in_game = game
    player.in_cut_scene = cut_scene
    player.in_end_scene = end_scene

def fade(): 
    fade = pygame.Surface((WIDTH, HEIGHT))
    fade.fill((0,0,0))

    x = 200

    # fade out
    for alpha in range(0, x):
        fade.set_alpha(alpha)
        WIN.blit(fade, (0,0))
        pygame.display.update()
    
    # fade in
    for alpha in range(0, x):
        fade.set_alpha(x - alpha)
        WIN.blit(fade, (0,0))
        pygame.display.update()

def draw_start_scene(mouse):
    # draw background
    bg = pygame.Surface(WIN.get_size())
    bg = bg.convert()
    bg.fill((150, 150, 150))
    WIN.blit(bg, (0, 0))

    WIN.blit(TITLE, (500, 100))

    # draw buttons
    if (600 <= mouse[0] <= 800) and (350 <= mouse[1] <= 450):
        WIN.blit(GAME_START_BUTTON2, (600, 350))   
    else:
        WIN.blit(GAME_START_BUTTON1, (600, 350))

    if (600 <= mouse[0] <= 800) and (500 <= mouse[1] <= 600):
        WIN.blit(GAME_QUIT_BUTTON2, (600, 500))
    else:
        WIN.blit(GAME_QUIT_BUTTON1, (600, 500))

    pygame.display.update()

def draw_opening_scene(font, current_display_text_row):
    # draw black background
    black_bg = pygame.Surface(WIN.get_size())
    black_bg = black_bg.convert()
    black_bg.fill(BLACK)
    WIN.blit(black_bg, (0, 0))

    text_pos = (100, 0)
    for line in GAME_START_TEXT[:min(current_display_text_row, len(GAME_START_TEXT))]:
        # create surface for line
        line_surface = font.render(line, True, (255, 255, 255))
        line_rect = line_surface.get_rect()
        line_rect.topleft = text_pos

        line_size = line_surface.get_size()
        line_size = (line_size[0] + 5, line_size[1] + 5)

        
        WIN.blit(line_surface, line_rect)

        # next line
        text_pos = (text_pos[0], text_pos[1] + line_size[1])
    
    pygame.display.update()

    # print("game start!\n")

def draw_main_window(NPCs, my_player, mouse):
    
    # draw the background
    WIN.blit(BACKGROUND, (0, 0))

    for npc in NPCs:
        npc.draw_character(WIN)

    # draw table
    WIN.blit(TABLE, TABLE_POS)

    # draw paper
    WIN.blit(PAPER, PAPER_POS)

    for npc in NPCs:
        if npc.is_speaking:
            npc.speak(WIN, my_player.current_round)

    # if player is making_decision
    if my_player.making_decision:
    #if True:
        # draw the stamps
            # if on hover
        if (APPROVE_STAMP_POS[0] <= mouse[0] <= APPROVE_STAMP_POS[0] + STAMP_WIDTH) and (APPROVE_STAMP_POS[1] <= mouse[1] <= APPROVE_STAMP_POS[1] + STAMP_HEIGHT): 
            WIN.blit(APPROVE_STAMP, (APPROVE_STAMP_POS[0], APPROVE_STAMP_POS[1] - 10))
        else: 
            WIN.blit(APPROVE_STAMP, APPROVE_STAMP_POS)

        if (DISAPPROVE_STAMP_POS[0] <= mouse[0] <= DISAPPROVE_STAMP_POS[0] + STAMP_WIDTH) and (DISAPPROVE_STAMP_POS[1] <= mouse[1] <= DISAPPROVE_STAMP_POS[1] + STAMP_HEIGHT):
            WIN.blit(DISAPPROVE_STAMP, (DISAPPROVE_STAMP_POS[0], DISAPPROVE_STAMP_POS[1] - 10))
        else:
            WIN.blit(DISAPPROVE_STAMP, DISAPPROVE_STAMP_POS)
    

    pygame.display.update()

def draw_cut_scene(font, text, score, player_score, current_display_text_row):
    # draw black background
    black_bg = pygame.Surface(WIN.get_size())
    black_bg = black_bg.convert()
    black_bg.fill(BLACK)
    WIN.blit(black_bg, (0, 0))

    text_pos = (100, 100)
    
    for line in text[:min(current_display_text_row, len(text))]:
        # create surface for line
        line_surface = font.render(line, True, (255, 255, 255))
        line_rect = line_surface.get_rect()
        line_rect.topleft = text_pos

        line_size = line_surface.get_size()
        line_size = (line_size[0] + 5, line_size[1] + 5)

        
        WIN.blit(line_surface, line_rect)
        # next line
        text_pos = (text_pos[0], text_pos[1] + line_size[1] + 20)
    
    if current_display_text_row == len(text) + 1:
        text_pos = (100, 500)
        for x in range(4):
            if x == 0:
                line_surface = font.render(CUT_SCENE_SCORE_TEXT[x], True, (255, 255, 255))
            elif x == 1:
                line_surface = font.render(CUT_SCENE_SCORE_TEXT[x] + str(player_score["Economy"]) + "  =>  " +
                                str(max(player_score["Economy"] + score["Economy"], 0)),
                                True, (255, 255, 255))
            elif x == 2:
                line_surface = font.render(CUT_SCENE_SCORE_TEXT[x] + str(player_score["Gov_trust"]) + "  =>  " +
                                str(max(player_score["Gov_trust"] + score["Gov_trust"], 0)),
                                True, (255, 255, 255))
            elif x == 3:
                line_surface = font.render(CUT_SCENE_SCORE_TEXT[x] + str(player_score["Public_health"]) + "  =>  " +
                                str(max(player_score["Public_health"] + score["Public_health"], 0)),
                                True, (255, 255, 255))

            line_rect = line_surface.get_rect()
            line_rect.topleft = text_pos

            line_size = line_surface.get_size()
            line_size = (line_size[0] + 5, line_size[1] + 5)
            
            WIN.blit(line_surface, line_rect)

            # next line
            text_pos = (text_pos[0], text_pos[1] + line_size[1] + 20)

    pygame.display.update()

def draw_end_scene(font, text, current_display_text_row):

    # draw black background
    black_bg = pygame.Surface(WIN.get_size())
    black_bg = black_bg.convert()
    black_bg.fill(BLACK)
    WIN.blit(black_bg, (0, 0))

    text_pos = (200, 200)
    for line in text[:min(current_display_text_row, len(text))]:
        # create surface for line
        line_surface = font.render(line, True, (255, 255, 255))
        line_rect = line_surface.get_rect()
        line_rect.topleft = text_pos

        line_size = line_surface.get_size()
        line_size = (line_size[0] + 5, line_size[1] + 5)

        
        WIN.blit(line_surface, line_rect)

        # next line
        text_pos = (text_pos[0], text_pos[1] + line_size[1])
    
    pygame.display.update()

def change_music(music_path, volume):
    assert 0.0 <= volume <= 1.0
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(-1)

    
def main():
    clock = pygame.time.Clock()

    # init text and sound process
    pygame.font.init()
    pygame.mixer.init()
    change_music(START_MUSIC, 0.1)

    my_player = Player()

    NPCs = []
    NPCs.append(Character(1, NPC1, '1'))
    NPCs.append(Character(2, NPC2, '2'))

    
    pygame.display.set_caption("GESC2060 Project Game!")

    start_time = pygame.time.get_ticks()
    
    font = pygame.font.Font(os.path.join("Fonts", "kaiu.ttf"), 38)
    # wait for 1s until game starts
    # pygame.time.wait(1000)

    # used to count sequential text display
    current_display_text_row = 1

    run = True
    while run:
        while my_player.in_start_scene:
            clock.tick(FPS)
            # get mouse position
            mouse = pygame.mouse.get_pos()

            draw_start_scene(mouse)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    change_scene(my_player, False, False, False, False, False)
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # if left click
                    if event.button == 1:
                        if (600 <= mouse[0] <= 800) and (350 <= mouse[1] <= 450):
                            # if click on start_game
                            change_scene(my_player, False, True, False, False, False)
                            change_music(CUT_SCENE_MUSIC, 0.05)
                            
                        elif (600 <= mouse[0] <= 800) and (500 <= mouse[1] <= 600):
                            # else if click on quit
                            change_scene(my_player, False, False, False, False, False)
                            run = False

        while my_player.in_opening_scene:
            #print("in game start loop")
            clock.tick(FPS)
            # pygame.time.wait(1000)
            start_text_length = len(GAME_START_TEXT)
            draw_opening_scene(font, current_display_text_row)
            
            if pygame.time.get_ticks() - start_time >= 3000:
            # if pygame.time.get_ticks() - start_time >= 100:
                if current_display_text_row + 1 <= start_text_length + 1:
                    current_display_text_row += 1
                start_time = pygame.time.get_ticks()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    change_scene(my_player, False, False, False, False, False)
                    run = False

            if current_display_text_row == start_text_length + 1:
                change_scene(my_player, False, False, True, False, False)
                change_music(GAME_MUSIC, 0.5)
                NPCs[0].is_speaking = True
                run = True
                fade()
                            
        while my_player.in_game:
            clock.tick(FPS)
            
            # get mouse position
            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    my_player.in_game = False
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # if left click
                    if event.button == 1:
                        # print(NPCs[0].is_speaking)
                        # if clicking period > 2s -> no clicking too fast issue 
                        if pygame.time.get_ticks() - start_time >= 2000:
                        # if pygame.time.get_ticks() - start_time >= 0:
                            if my_player.making_decision:
        
                                # if player click on approved button (mouse pos is within button)
                                if (APPROVE_STAMP_POS[0] <= mouse[0] <= APPROVE_STAMP_POS[0] + STAMP_WIDTH) and \
                                (APPROVE_STAMP_POS[1] <= mouse[1] <= APPROVE_STAMP_POS[1] + STAMP_HEIGHT):
                                    
                                    my_player.approve()
                                    # fade out
                                    fade()
                                    current_display_text_row = 1
                                    change_music(CUT_SCENE_MUSIC, 0.05)

                                elif (DISAPPROVE_STAMP_POS[0] <= mouse[0] <= DISAPPROVE_STAMP_POS[0] + STAMP_WIDTH) and \
                                    (DISAPPROVE_STAMP_POS[1] <= mouse[1] <= DISAPPROVE_STAMP_POS[1] + STAMP_HEIGHT):

                                    my_player.disapprove()
                                    # fade out
                                    fade()
                                    current_display_text_row = 1
                                    change_music(CUT_SCENE_MUSIC, 0.05)

                            start_time = pygame.time.get_ticks()
                            for npc in NPCs:
                                # if npc is speaking, assume player has finished reading and want to proceed
                                if npc.is_speaking:
                                    # increase speak_index by 1 so npc will speak next sentence
                                    npc.speak_index += 1
                                    # if this npc finishes speaking all sentences in this round
                                    if npc.speak_index == len(npc.speech["round" + str(my_player.current_round)]):
                                        # if it is NPC1 speaking
                                        if npc.id == 1:
                                            # stop speaking, and reset speak_index
                                            npc.is_speaking = False
                                            npc.speak_index = -1

                                            # let NPC2 speak
                                            NPCs[1].is_speaking = True

                                        # if it is NPC2 speaking
                                        elif npc.id == 2:
                                            # stop speaking, and reset speak_index
                                            npc.is_speaking = False
                                            npc.speak_index = -1

                                            """ ... both npcs have finished, let player to do decision, to be implemented"""
                                            my_player.making_decision = True


            draw_main_window(NPCs, my_player, mouse)

        while my_player.in_cut_scene:
            clock.tick(FPS)

            if my_player.bill_approved == True:
                text_len = len(my_player.cur_bill.approve_text)
                new_score = my_player.cur_bill.approve_score
                new_text = my_player.cur_bill.approve_text
            else:
                text_len = len(my_player.cur_bill.disapprove_text)
                new_score = my_player.cur_bill.disapprove_score
                new_text = my_player.cur_bill.disapprove_text

            draw_cut_scene(font, new_text, new_score, 
                           my_player.score, current_display_text_row)

            if pygame.time.get_ticks() - start_time >= 3000:
            # if pygame.time.get_ticks() - start_time >= 1000:
                if current_display_text_row + 1 <= text_len + 2:
                    current_display_text_row += 1
                start_time = pygame.time.get_ticks()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    change_scene(my_player, False, False, False, False, False)
                    run = False
            
            if current_display_text_row == text_len + 2:
                change_scene(my_player, False, False, True, False, False)
                change_music(GAME_MUSIC, 0.5)
                current_display_text_row = 1
                NPCs[0].is_speaking = True
                run = True

                # update score
                my_player.score["Economy"]       = max(my_player.score["Economy"]       + new_score["Economy"]      , 0)
                my_player.score["Gov_trust"]     = max(my_player.score["Gov_trust"]     + new_score["Gov_trust"]    , 0)
                my_player.score["Public_health"] = max(my_player.score["Public_health"] + new_score["Public_health"], 0)

                # go to next bill or end game if already 9 rounds
                if my_player.current_round <= my_player.total_rounds:
                    my_player.next_bill()
                    current_display_text_row = 1

                    # if any situation too bad
                    if (my_player.score["Economy"]       <= 15   and my_player.score["Gov_trust"] <= 25) or \
                       (my_player.score["Public_health"] <= 15   and my_player.score["Gov_trust"] <= 25):


                        change_scene(my_player, False, False, False, False, True)
                        change_music(CUT_SCENE_MUSIC, 0.1)

                else:
                    change_scene(my_player, False, False, False, False, True)
                    change_music(CUT_SCENE_MUSIC, 0.1)

                # just to avoid accident
                new_score = {"Economy": 0,
                            "Gov_trust": 0,
                            "Public_health": 0} 

                fade()
        
        while my_player.in_end_scene:
            clock.tick(FPS)

            if my_player.score["Economy"] >= 70 and my_player.score["Gov_trust"] >= 70 and my_player.score["Public_health"] >= 70:
                text = END_SCENE_TEXT["good_end"]

            elif my_player.score["Public_health"] <= 15   and my_player.score["Gov_trust"] <= 25:
                text = END_SCENE_TEXT["bad_end_health_trust"]

            elif my_player.score["Economy"]       <= 15   and my_player.score["Gov_trust"] <= 25:
                text = END_SCENE_TEXT["bad_end_economy_trust"]

            else:
                text = END_SCENE_TEXT["normal_end"]

            draw_end_scene(font, text, current_display_text_row)

            if pygame.time.get_ticks() - start_time >= 3000:
            # if pygame.time.get_ticks() - start_time >= 1000:
                if current_display_text_row + 1 <= len(text) + 1:
                    current_display_text_row += 1
                start_time = pygame.time.get_ticks()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    change_scene(my_player, False, False, False, False, False)
            
            
            if current_display_text_row == len(text) + 1:
                change_scene(my_player, True, False, False, False, False)

                # reset everything
                current_display_text_row = 1
                my_player.cur_round = 1
                my_player.score = { # 各項社會指標的分數
                    "Economy": 40,
                    "Gov_trust": 40,
                    "Public_health": 40,
                }
                change_music(START_MUSIC, 0.1)

                fade()

    pygame.quit()



if __name__ == '__main__':
    main()