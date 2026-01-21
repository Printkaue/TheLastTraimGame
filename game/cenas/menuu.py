import pygame

pygame.init()
pygame.font.init()


def draw_menu(screen, font):
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            return "quit"

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RETURN:
                return "game"

    title = font.render("THE LAST TRAIN OF MIDNIGHT", True, (255, 255, 255))
    info = font.render("Pressione ENTER para comecar", True, (180, 180, 180))
    version = font.render("alfa 0.0.1", True, (180, 180, 180))

    screen.blit(title, title.get_rect(center=(400, 200)))
    screen.blit(info, info.get_rect(center=(400, 260)))
    texto = font.render("Alfa 0.0.1", True, (180, 180, 180))
    rect = texto.get_rect()
    rect.bottomleft = (10, screen.get_height() - 10)
    screen.blit(texto, rect)


    return "menu"


