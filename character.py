# -*-coding:utf-8 -*-
import os
import pygame
import json


class Character(pygame.sprite.Sprite):
    def __init__(self, id, NPC, npc_num):
        pygame.sprite.Sprite.__init__(self)
        # NPC id
        self.id = id

        # info from setting
        self.x = NPC["screen_x"]
        self.y = NPC["screen_y"]
        self.width = NPC["width"]
        self.height = NPC["height"]
        self.pic_path = NPC["pic_path"]
        self.speech_bubble_path = NPC["speech_bubble"]
        self.rotate_angle = NPC["rotate_angle"]

        self._is_speaking = False
        # NPC's speech index, max = len(NPC.speech[round]) - 1
        self.speak_index = -1

        file = open('NPC_text.json', 'r', encoding='utf-8')
        self.speech = json.load(file)["NPC" + npc_num]
        file.close()

        # NPC image and space in window
        self.image = pygame.image.load( os.path.join( 'Assets', self.pic_path ) )
        self.rect = pygame.Rect( self.x, self.y, self.width, self.height )
        self.obj = pygame.transform.rotate( pygame.transform.scale(self.image, ( self.width, self.height) ), self.rotate_angle )

        # NPC's speech bubble
        self.speech_bubble_img = pygame.image.load( os.path.join( 'Assets', self.speech_bubble_path ) )
        self.speech_bubble = pygame.transform.scale( self.speech_bubble_img, (500, 500))

    @property
    def is_speaking(self):
        return self._is_speaking
    
    @is_speaking.setter
    def is_speaking(self, value):
        assert type(value) == bool
        self._is_speaking = value


    # draw the character
    def draw_character(self, WIN):
        WIN.blit(self.obj, ( self.x, self.y ) )
    
    # the character speaks
    def speak(self, WIN, round_num):
        font = pygame.font.Font("Fonts/kaiu.ttf", 28)

        # define text and bubble position
        if self.id == 1:
            text_pos = (self.rect.midtop[0] + 130, self.rect.midtop[1] + 100)
            bubble_pos = (self.rect.midtop[0] + 50, self.rect.midtop[1])
            
            if self.speak_index >=0:
                # display text bubble
                WIN.blit(self.speech_bubble, bubble_pos)
        elif self.id == 2:
            text_pos = (self.rect.midtop[0] - 550, self.rect.midtop[1] + 50)
            bubble_pos = (self.rect.midtop[0] - 600, self.rect.midtop[1] - 50)
            
            if self.speak_index >=0:
                # display text bubble
                WIN.blit(self.speech_bubble, bubble_pos)

        # only speak when we click
        if self.speak_index >=0:
            self.display_multi_line_text(WIN, font, self.speech["round" + str(round_num)][self.speak_index], text_pos)
        

    def display_multi_line_text(self, WIN, font, text, text_pos):

        for line in text:
            # create surface for line
            line_surface = font.render(line, True, (0, 0, 0))
            line_rect = line_surface.get_rect()
            line_rect.topleft = text_pos

            line_size = line_surface.get_size()
            line_size = (line_size[0] + 5, line_size[1] + 5)

            
            WIN.blit(line_surface, line_rect)

            # next line
            text_pos = (text_pos[0], text_pos[1] + line_size[1] + 5)


