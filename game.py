# 导入 Pygame 库
import pygame
import random

# 初始化 Pygame
pygame.init()

# 设置屏幕大小
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 设置标题
pygame.display.set_caption("飞机大战")

# 加载玩家飞机图片
player_img = pygame.image.load("player.png")
player_x = screen_width // 2
player_y = screen_height - 100
player_change = 0

# 敌机列表
enemies = []

# 子弹列表
bullets = []

# 游戏循环
running = true
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = false

    # 更新玩家位置
    player_x += player_change

    # 绘制背景
    screen.fill((0, 0, 0))

    # 绘制玩家飞机
    screen.blit(player_img, (player_x, player_y))

    # 绘制敌机
    for enemy in enemies:
        pass

    # 绘制子弹
    for bullet in bullets:
        pass

    # 更新屏幕
    pygame.display.update()