import sys, time, random, os, subprocess


choice = ''
answer_a = ['a', 'A']
answer_b = ['b', 'B']
answer_c = ['c', 'C']
answer_yes = ['Y', 'y', 'yes', 'Yes', 'YES']
answer_no = ['N', 'n', 'no', 'No', 'NO']

wrong_abc = 'Please, answer with "A, B or C"\n'
wrong_yn = 'Please, answer "Y or N"\n'

# "Collectables"
wooden_sword = 0
key = 'no'

def clear():
    if os.name in ('nt','dos'):
        subprocess.call("cls")
    elif os.name in ('linux','osx','posix'):
        subprocess.call("clear")
    else:
        print("\n") * 120

def abc(a, b, c):
    print('WHAT DO YOU DO?')
    print('')
    print(f'''    A. {a}\n
    B. {b}\n
    C. {c}\n''')

typing_speed_normal = 500
def normal_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed_normal)
    print ('')

typing_speed_slow = 0.5
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(typing_speed_slow)
    print ('')

def new_item(i):
    space = ('\n') * 10
    print(space)
    normal_type(f'NEW ITEM COLLECTED: {i}')
    print(space)

def cyclope(t):
    print(f''' 
               _......._
           .-'.'.'.'.'.'.`-.
         .'.'.'.'.'.'.'.'.'.`.
        /.'.'               '.|
        |.'    _.--...--._     |
        \    `._.-.....-._.'   /
        |     _..- .-. -.._   |
     .-.'    `.   ((@))  .'   '.-.
    ( ^ \      `--.   .-'     / ^ )
     \  /         .   .       \  /
     /          .'     '.  .-    |
    ( _.\    \ (_`-._.-'_)    /._\)
     `-' \   ' .--.          / `-'       {t}
         |  / /|_| `-._.'\   |
         |   |       |_| |   /-.._
     _..-\   `.--.______.'  |
          \       .....     |
           `.  .'      `.  /
             \           .'
              `-..___..-`
    ''')

def death():
    global wooden_sword, cyclope
    wooden_sword = 0
    
    clear()
    print('''
                          _ _          _ 
                         | (_)        | |
 _   _  ___  _   _     _ | |_  ____ _ | |
| | | |/ _ \| | | |   / || | |/ _  ) || |
| |_| | |_| | |_| |  ( (_| | ( (/ ( (_| |
 \__  |\___/ \____|   \____|_|\____)____|
(____/                                   


''')
    print('Want to play again? Y/n')
    choice = input('>>> ')
    if choice in answer_yes:
        print('OK')
        slow_type('...')
        intro()
    
    elif choice in answer_no:
        slow_type('sure...')
        clear()
        quit()
    
    else:
        print(wrong_yn)
        time.sleep(1)
        death()

def key(t):
    print(f'''
                            {t}
          .---.
         /    |\________________
        ( ( ) | ________   _   _)   
         \    |/        | | | |
          `---'         "-" |_|

    ''')

def intro():
    
    clear()
    normal_type('Your mom called you, she is mad.')
    normal_type('You need to get to her before she explodes in anger. ')
    normal_type('You are in you room playing Call of Duty, currently in the middle of a task. ')
    
    abc('You instanly get of your chair and go attend your mother', 'You keep playing the game', 'You jump out of the window')
    
    choice = input('>>> ')
    if choice in answer_a:
        option_attend()

    elif choice in answer_b:
        normal_type('Are you sure?')
        print('Y/n')
        choice = input('>>> ')
        if choice in answer_yes:
            death()
        elif choice in answer_no:
            intro()
        else:
            print(wrong_abc)
    
    elif choice in answer_c:
        death()
    
    else:
        print(wrong_abc)
        time.sleep(0.5)
        intro()

def option_attend():
    
    global wooden_sword
    
    clear()
    normal_type("You open your room's door and go down the stairs.")
    slow_type('...')
    normal_type('Ouch!')
    normal_type('You have tripped in a cracked wooden sword.')
    
    abc('You keep going like nothing has happened', 'You kick the sword in anger and move on', 'You take the sword and continue your jorney')

    choice = input('>>> ')
    if choice in answer_a or choice in answer_b:
        option_keep_going()
    
    elif choice in answer_c:
        wooden_sword = 1
        option_keep_going()

    else:
        print(wrong_abc)
        time.sleep(1)
        option_attend()

def option_keep_going():
    
    clear()
    normal_type("You are walking through a hallway, it's hard to see.")
    normal_type('You hear something.')
    normal_type('You keep walking.')
    normal_type("The hallway leads to a room... A big room. So big that you can't even see the roof.")
    normal_type('You hear something.')
    normal_type("It's getting louder.")
    normal_type('You look back and see a 7 feet tall shadow coming at you.')
    
    abc('You run as fast as you can', 'You try hidding', 'You fight the shadow')

    choice = input('>>> ')
    if choice in answer_c:
        if wooden_sword == 1:
            clear()
            normal_type("While it's getting closer, you pull out your sword and slice the air with it.")
            normal_type('You hit the thing with your sword, that you find out being an orkish looking man.')
            normal_type('You were not able to cut the green beast, but were strong enought to black it out.')
            time.sleep(1)
            option_scaped()

        elif wooden_sword == 0:
            option_kidnap() 
    
    if choice in answer_b:
        if wooden_sword == 1:
            clear()
            normal_type('You hide from the creature in the dark, but it finds you.')
            normal_type('Do you want to fight the creature?: Y/n')
            
            choice = input('>>> ')
            if choice in answer_yes:
                clear()
                normal_type("While it's getting closer, you pull out your sword and slice the air with it.")
                normal_type('You hit the thing with your sword, that you find out being an orkish looking man.')
                normal_type('You were not able to cut the green beast, but were strong enought to black it out.')
                slow_type('...')
                option_scaped()
            
            elif choice in answer_no:
                option_kidnap()
            
            else:
                print(wrong_yn)
                time.sleep(1)
                option_keep_going()

        
        elif wooden_sword == 0:
            clear()
            time.sleep(1)
            normal_type('You try hidding, but it finds you and you have nothing to defend yourself.')
            time.sleep(1)
            option_kidnap()

    if choice in answer_a:
        option_scaped()

    else:
        print(wrong_abc)
        time.sleep(1)
        option_keep_going()

def option_scaped():

    clear()
    normal_type('It worked out, you have scaped.')    
    normal_type("You continue your jorney through the florest. It's a shiny day.")
    normal_type('There are almost no clouds in the sky and you can hear lots of birds.')
    normal_type('You are very hungry, but have nothing to eat.')
    normal_type('You can see a village and a lake in the far.')
    scaped_save()
    
def scaped_save():    
    abc('Village', 'Lake', 'You try going back home')

    choice = input('>>> ')
    if choice in answer_a:
        village()

    if choice in answer_b:
        option_lake()
    
    if choice in answer_c:
        
        clear()
        normal_type('You try going back but you have no idea where you came from, ')
        normal_type('everything is jungle.')
        time.sleep(0.5)
        clear()
        scaped_save()

def option_kidnap():
    global key

    clear()
    slow_type('...')
    normal_type('You blacked out.')
    normal_type('You are in a small dark room.')
    normal_type("It's cold.")
    slow_type('...')
    clear()
    cyclope('BE QUIET!')
    time.sleep(3)
    clear()
    cyclope('ME HUNT MEAT. YOU STAY STILL!')
    time.sleep(5)
    clear()
    slow_type('...')
    normal_type('The beast left the cave.')
    normal_type('You are alone now.')
    
    abc('You run.', 'You run really fast.', 'You stay and obbey the beast.')
    
    choice = input('>>> ')
    if choice in answer_a or choice in answer_b:
        clear()
        slow_type('...')
        option_scaped()

    elif choice in answer_c:
        clear()
        normal_type('You stay in the cave like the cyclope asked you to')
        slow_type('...')
        clear()
        slow_type('"TWO HOURS LATER"')
        time.sleep(1)
        cyclope('OH, YOU HERE!')
        time.sleep(5)
        clear()
        cyclope('ME HAVE SOMETHING FOR YOU!!!')
        time.sleep(5)
        clear()
        cyclope('ME FIND KEY.')
        time.sleep(5)
        clear()
        key('"THERE IT IS."')
        time.sleep(5)
        clear()
        cyclope('TAKE IT.')
        time.sleep(3)
        clear()
        new_item('MYSTERIOUS KEY!')
        time.sleep(3)
        clear()
        cyclope('NOW LEAVE. RUN.')
        time.sleep(3)
        key = 'yes'
        option_scaped()

def village():
    print('oi')

intro()
