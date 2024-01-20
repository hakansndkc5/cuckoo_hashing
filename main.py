import pygame
import time
import sys
import math
import random
n_elements=0
collisions = 0

pygame.init()


screen = pygame.display.set_mode((1000 , 800))
pygame.display.set_caption("Cuckoo Hashing Visualization")

size=input("Please enter the table sizes: ")
if int(size) < 10 or int(size) > 30:
    print("Size can not to be more than 30 and can not be less than 10")
    exit(-1)
else :
    pass




# Create hash functions
def hash1(x):
    return x % len(tables)


def hash2(x):
    A = (math.sqrt(5) - 1) / 2
    return int(((x * A) % 1) * len(tables))


def hash3(x):
    p = 997
    a = random.randint(1, p-1)
    b = random.randint(0, p-1)
    return ((a*x + b) % p) % len(tables)


def hash4(x):
    h = x
    h = (h + 0x7ed55d16) + (h << 12)
    h = (h ^ 0xc761c23c) ^ (h >> 19)
    h = (h + 0x165667b1) + (h << 5)
    h = (h + 0xd3a2646c) ^ (h << 9)
    h = (h + 0xfd7046c5) + (h << 3)
    h = (h ^ 0xb55a4f09) ^ (h >> 16)
    return h % len(tables)



def hash5(x):
    return (x >> 4) % len(tables)




# Insert an element into the tables using the cuckoo hashing method
def insert(x):
    global collisions
    global n_elements
    current_table = 0
    h = hash1(x)
    n_elements+=1
    print("---------------------- After Inserted "+ str(x)+" -------------------------------------------")
    load_factor()

    while current_table < len(tables):
        if tables[current_table][h] is None or tables[current_table][h] == x:
            tables[current_table][h] = x
            print("Total collision = " + str(collisions))
            return collisions

        else:
            collisions += 1
            tables[current_table][h], x = x, tables[current_table][h]
            current_table += 1
            h = hash1(x) if current_table == 0 else globals()[f"hash{current_table+1}"](x)


def load_factor():
    total_slots = sum(len(t) for t in tables)
    print("Load Factor is = " + str(n_elements / total_slots))




def remove(x):
    for table in tables:
        if x in table:
            table[table.index(x)] = None



# Get the number of tables from the user
num_tables = int(input("Enter the number of tables to create: "))
if (num_tables <= 5):
    print("Tables created succesfully.")
else :
    print("Table number must be less than 5")
    exit(-1)

# Create the tables
tables = []
for i in range(num_tables):
    tables.append([None for i in range(int(size))])

# Draw the tables
def draw():
    for k, table in enumerate(tables):
        for i, x in enumerate(table):
            if x is None:
                color = (255, 255, 255)
            else:
                color = (0, 0, 0)
            pygame.draw.rect(screen, (0, 0, 0), (100 + k*100-2, 50-2 + i * 50, 54, 54), 2)
            pygame.draw.rect(screen, color, (100 + k*100, 50 + i * 50, 50, 50))
            if x is not None:
                text = font.render(str(x), True, (255, 255, 255))
                screen.blit(text, (105 + k*100, 55 + i * 50))
        # Add table number text
        table_num = font.render("Table " + str(k+1), True, (0, 0, 0))
        screen.blit(table_num, (100 + k*100, 15))
    pygame.draw.rect(screen, button_color, button_rect)
    button_text_surface = button_font.render(button_text, True, (0, 0, 0))
    button_text_rect = button_text_surface.get_rect(center=button_rect.center)
    screen.blit(button_text_surface, button_text_rect)
    remove_button_rect = pygame.Rect(750, 375, 100, 50)
    remove_button_text = "Remove"
    remove_button_font = pygame.font.Font(None, 30)
    exit_button_rect = pygame.Rect(750, 475, 100, 50)
    exit_button_text = "Exit"
    exit_button_font = pygame.font.Font(None, 30)


    pygame.draw.rect(screen, (255, 0, 0), exit_button_rect)


    exit_button_text_surface = exit_button_font.render(exit_button_text, True, (0, 0, 0))


    exit_button_text_rect = exit_button_text_surface.get_rect(center=exit_button_rect.center)


    screen.blit(exit_button_text_surface, exit_button_text_rect)


    pygame.draw.rect(screen, ('darkmagenta'), remove_button_rect)


    remove_button_text_surface = remove_button_font.render(remove_button_text, True, (0, 0, 0))


    remove_button_text_rect = remove_button_text_surface.get_rect(center=remove_button_rect.center)


    screen.blit(remove_button_text_surface, remove_button_text_rect)

    pygame.draw.rect(screen, text_box_color, text_box_rect)
    pygame.draw.lines(screen, (0, 0, 0),  True, [text_box_rect.topleft, text_box_rect.topright, text_box_rect.bottomright, text_box_rect.bottomleft], 2)

    search_button_rect = pygame.Rect(750, 275, 100, 50)
    search_button_text = "Search"
    search_button_font = pygame.font.Font(None, 30)


    pygame.draw.rect(screen, ('cornflowerblue'), search_button_rect)


    search_button_text_surface = search_button_font.render(search_button_text, True, (0, 0, 0))


    search_button_text_rect = search_button_text_surface.get_rect(center=search_button_rect.center)


    screen.blit(search_button_text_surface, search_button_text_rect)

    value_text_surface = value_font.render(user_input, True, (0, 0, 0))
    value_rect = value_text_surface.get_rect(center=(775, 125))
    screen.blit(value_text_surface, value_rect)

    my_font = pygame.font.SysFont('Times New Roman', 16)
    text_surface=my_font.render('Group Members: Hakan SANDIKÇI / '
                                'Mahmut SALMAN / '
                                'Sueda BİLEN',False,(0,0,0))
    screen.blit(text_surface, (400, 750))
def search(x):
    for i in range(len(tables)):
        h = globals()[f"hash{i+1}"](x)
        if tables[i][h] == x:
            print("Element " + str(x) + f" found in table {i+1} at index {h}")
    return "Element not found in any table"

pygame.display.set_caption("Cuckoo Hashing Visualization")


button_color = ('chartreuse')
button_text = "Insert"
button_font = pygame.font.Font(None, 30)
button_rect = pygame.Rect(750, 175, 100, 50)

remove_button_rect = pygame.Rect(700, 375, 200, 50)

exit_button_rect = pygame.Rect(700, 475, 100, 50)


search_button_rect = pygame.Rect(750, 275, 100, 50)


text_box_color = (255, 255, 255)
text_box_rect = pygame.Rect(700, 100, 200, 50)





font = pygame.font.Font(None, 30)


running = True
value = ""
value_font = pygame.font.Font(None, 30)
user_input=""
scroll_x = 0
scroll_y = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                value = value[:-1]
            elif event.key == pygame.K_RETURN:
                insert(int(value))


            elif event.unicode.isalnum() or event.unicode == ' ':
                value += event.unicode
            if event.unicode.isalnum() or event.unicode == ' ':
                user_input += event.unicode
            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if text_box_rect.collidepoint(pygame.mouse.get_pos()):
                active = True
            else:
                active = False
            if button_rect.collidepoint(pygame.mouse.get_pos()):
                insert(int(value))
            if remove_button_rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0]:
                   remove(int(value))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if search_button_rect.collidepoint(pygame.mouse.get_pos()):
                    search(int(value))


    # Clear the screen
    screen.fill('aquamarine')

    # Draw the tables
    draw()

    # Update the screen
    pygame.display.flip()




print("Exited succesfully.")

pygame.quit()
