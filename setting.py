import pygame
import os
import json

WIDTH, HEIGHT = 1500, 900

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

FPS = 30

TOTAL_ROUND = 9

NPC1 = {
    "screen_x": 0,
    "screen_y": 100,
    "width": 800,
    "height": 1000,
    "pic_path": "NPC1.png",
    "speech_bubble": "NPC1_speech_bubble.png",
    "rotate_angle": 0,
}


NPC2 = {
    "screen_x": 800,
    "screen_y": 0,
    "width": 800,
    "height": 1000,
    "pic_path": "NPC2.png",
    "speech_bubble": "NPC2_speech_bubble.png",
    "rotate_angle": 0,
}

# musics
START_MUSIC = os.path.join("Assets", "start_music.ogg")
GAME_MUSIC = os.path.join("Assets", "game_music.MID")
CUT_SCENE_MUSIC = os.path.join("Assets", "cut_scene_music.WAV")


# create window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

TITLE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Title.png')), (400, 200))

GAME_START_BUTTON1 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Game_start1.jpg')), (200, 100))
GAME_START_BUTTON2 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Game_start2.jpg')), (200, 100))

GAME_QUIT_BUTTON1  = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Quit1.jpg')), (200, 100))
GAME_QUIT_BUTTON2  = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Quit2.jpg')), (200, 100))

BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'background.jpg')), (WIDTH, HEIGHT))

TABLE_HEIGHT = 600
TABLE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'table.png')), (WIDTH, TABLE_HEIGHT))
TABLE_POS = (0, 300)

PAPER_WIDTH, PAPER_HEIGHT = 300, 300
PAPER = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'paper.png')), (PAPER_WIDTH, PAPER_HEIGHT))
PAPER_POS = (550, 600)


STAMP_WIDTH, STAMP_HEIGHT = 150, 240
APPROVE_STAMP = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'approve_stamp.png')), (STAMP_WIDTH, STAMP_HEIGHT))
APPROVE_STAMP_POS = (400, 650)

DISAPPROVE_STAMP = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'disapprove_stamp.png')), (STAMP_WIDTH, STAMP_HEIGHT))
DISAPPROVE_STAMP_POS = (900, 650)


file = open('game_start_text.json', 'r', encoding='utf-8')
GAME_START_TEXT = json.load(file)["text"]
file.close()

file = open('cut_scene_score_text.json', 'r', encoding='utf-8')
CUT_SCENE_SCORE_TEXT = json.load(file)["text"]
file.close()

file = open('end_scene_text.json', 'r', encoding='utf-8')
END_SCENE_TEXT = json.load(file)
file.close()