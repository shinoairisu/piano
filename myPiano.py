#导入所需的模块
import sys
import pygame
import configparser

config = configparser.ConfigParser()
config.read('piano.ini')
db_host = config.get('piano', 'midi')

# 使用pygame之前必须初始化
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(db_host)

KeyDown=False
# 设置主屏窗口
screen = pygame.display.set_mode((400,400))

# 设置窗口的标题，即游戏名称
pygame.display.set_caption('乱弹琴')

# 引入字体类型
f = pygame.font.Font('C:/Windows/Fonts/simhei.ttf',50)
# 生成文本信息，第一个参数文本内容；第二个参数，字体是否平滑；
# 第三个参数，RGB模式的字体颜色；第四个参数，RGB模式字体背景颜色；
text = f.render("我在弹琴呢！",True,(255,0,0),(0,0,0))
#获得显示对象的rect区域坐标
textRect =text.get_rect()
# 设置显示对象居中
textRect.center = (200,200)
# 将准备好的文本信息，绘制到主屏幕 Screen 上。
screen.blit(text,textRect)

pygame.mixer.music.play()
pygame.mixer.music.pause()
# 固定代码段，实现点击"X"号退出界面的功能，几乎所有的pygame都会使用该段代码
while True:
    if KeyDown:
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.pause()
    # 循环获取事件，监听事件状态
    for event in pygame.event.get():
        # 判断用户是否点了"X"关闭按钮,并执行if代码段
        if event.type == pygame.QUIT:
            #卸载所有模块
            pygame.quit()
            #终止程序，确保退出程序
            sys.exit()
        if event.type == pygame.KEYDOWN:
            KeyDown=True
            if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                pygame.mixer.music.set_volume(1.0)
            elif event.key == pygame.K_8 or event.key == pygame.K_KP8:
                pygame.mixer.music.set_volume(0.9)
            elif event.key == pygame.K_7 or event.key == pygame.K_KP7:
                pygame.mixer.music.set_volume(0.8)
            elif event.key == pygame.K_6 or event.key == pygame.K_KP6:
                pygame.mixer.music.set_volume(0.7)
            elif event.key == pygame.K_5 or event.key == pygame.K_KP5:
                pygame.mixer.music.set_volume(0.6)
            elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
                pygame.mixer.music.set_volume(0.5)
            elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
                pygame.mixer.music.set_volume(0.4)
            elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                pygame.mixer.music.set_volume(0.3)
            elif event.key == pygame.K_1 or event.key == pygame.K_KP1:
                pygame.mixer.music.set_volume(0.2)
            elif event.key == pygame.K_0 or event.key == pygame.K_KP0:
                pygame.mixer.music.set_volume(0.0)

        if event.type == pygame.KEYUP:
            allKey=pygame.key.get_pressed()
            if True not in allKey:
                KeyDown=False

    pygame.display.flip() #更新屏幕内容