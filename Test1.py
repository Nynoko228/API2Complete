# Чтобы GLUT установился надо удалить PyOpenGL и accelerate (pip uninstall PyOpenGL PyOpenGL_accelerat)
# после удаления запускаем cmd от админа, заходим в папку через cd и пишем вот эти 2 строчки в данном порядке:
# 1 - pip install PyOpenGL-3.1.6-cp311-cp311-win_amd64.whl --force-reinstall
# 2 - pip install PyOpenGL_accelerate-3.1.6-cp311-cp311-win_amd64.whl --force-reinstall


import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

# Инициализация PyGame
pygame.init()

# Размер окна
window_width = 800
window_height = 600

# Цвета
white = (1.0, 1.0, 1.0)
black = (0.0, 0.0, 0.0)
orange = (1.0, 0.5, 0.0)

# Инициализация PyGame окна
display = (window_width, window_height)
screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
displayCenter = [screen.get_size()[i] // 2 for i in range(2)]
pygame.mouse.set_pos(displayCenter)

# Настройка OpenGL
glClearColor(0.1, 0.2, 0.2, 1)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)
glEnable(GL_DEPTH_TEST)
# glEnable(GL_LIGHTING)
# glShadeModel(GL_SMOOTH)


# Функция для отрисовки снеговика
def draw_snowman():
    glutInit()
    glColor3fv(white)
    glTranslatef(0.0, -1.0, 0.0)
    glutSolidSphere(1, 32, 32)  # Тело снеговика

    glColor3fv(white)
    glTranslatef(0.0, 1.25, 0.0)
    glutSolidSphere(0.5, 32, 32)  # Голова снеговика

    glColor3fv(black)
    glTranslatef(-0.25, 0.25, 0.45)
    glutSolidSphere(0.1, 32, 32)  # Левый глаз

    glTranslatef(0.5, 0.0, 0.0)
    glutSolidSphere(0.1, 32, 32)  # Правый глаз

    glColor3fv(orange)
    glTranslatef(-0.25, -0.3, 0.1)
    glutSolidSphere(0.1, 32, 32)  # Нос

    # glColor3fv(black)
    # glTranslatef(0.0, -0.3, 0.2)
    # glRotatef(90, 1, 0, 0)
    # glutSolidCone(0.1, 0.5, 32, 32)  # галстук
    glColor3fv(white)

# Функция для создания снежинок
def create_snowflakes():
    snowflakes = []
    for i in range(400):
        x = random.uniform(-10, 10)
        y = random.uniform(-2, 4)
        z = random.uniform(-10, 10)
        snowflakes.append([x, y, z])
    return snowflakes

# Главный цикл
def main():
    snowflakes = create_snowflakes()
    mouseMove = [0, 0]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE)):
                pygame.quit()
                quit()
            # if event.type == pygame.MOUSEMOTION:
            #     mouseMove = [event.pos[i] - displayCenter[i] for i in range(2)]
            #     pygame.mouse.set_pos(displayCenter)

        # Умправление камерой использую мышку
        # mouseMove = pygame.mouse.get_rel()
        mouseMove = pygame.mouse.get_rel()
        glRotatef(mouseMove[0] * 0.1, 0.0, 1.0, 0.0)
        # glRotatef(mouseMove[0] * 0.1, 0.0, 1.0, 0.0)


        keypress = pygame.key.get_pressed()

        #glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Отрисовка снеговика
        glPushMatrix()
        draw_snowman()
        glPopMatrix()

        # Движение
        if keypress[pygame.K_w]:
            glTranslatef(0, 0, 0.1)
        if keypress[pygame.K_s]:
            glTranslatef(0, 0, -0.1)
        if keypress[pygame.K_d]:
            glTranslatef(-0.1, 0, 0)
        if keypress[pygame.K_a]:
            glTranslatef(0.1, 0, 0)
        if keypress[pygame.K_q]:
            glTranslatef(0, 0.1, 0)
        if keypress[pygame.K_e]:
            glTranslatef(0, -0.1, 0)

        # Отрисовка снежинок
        for snowflake in snowflakes:
            glPushMatrix()
            glTranslate(snowflake[0], snowflake[1], snowflake[2])
            glutSolidSphere(0.05, 10, 10)
            glColor3fv(white)
            snowflake[1] -= 0.01
            if snowflake[1] < -2:
                snowflake[1] = 2
            glPopMatrix()


        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()