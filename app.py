print('1 - Add a thought')
print('2 - View thoughts')
print('3 - Quit application')

thoughts = []


def dear_diary():
    while(True):
        selection = input_selection()
        if (selection == 1):
            input_thought()
        elif (selection == 2):
            share_thoughts()    
        
        elif(selection == 3):
            print("Goodbye")
            return


def input_selection():
    selection = input('Please select 1,2, or 3: ')
    return selection
    

    
def input_thought():
    thought = input('Tell me your thought: ')
    thoughts.append(thought)


def share_thoughts():
    for each_thought in thoughts:
        print(each_thought)


dear_diary()
