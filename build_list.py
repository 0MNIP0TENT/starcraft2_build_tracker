import json
import os

# Path to the current directory plus the name of the file.
path_to_file = os.getcwd() + '/build_list.json'

# If the json file does not exist this will create it.
def check_if_file_exists():
    if not os.path.isfile(path_to_file):
        with open('build_list.json','w') as file:
            print('json file created.')

while True:
    
    check_if_file_exists()
            
    option = input("""
    Enter a person\'s name to get a list of their known builds. 
    Enter 1 to add a new entry. 
    Enter 2 to add a build to an existing entry. 
    Enter 3 to exit. """)
            
    # Adding a new entry.
    if option == '1':
        name = input('Enter the new person\'s name. ')
        build = input('Now enter their build. ')
        """
        This list comprehension is needed to return a list
        in case the file is empty, but causes nested lists.

        """
        build_list = [json.loads(line) for line in open('build_list.json', 'r')]
        # this block prevents the nested lists.
        if len(build_list) > 0:
            builds = build_list[0]
            builds[name] = [build]
        else:
            # In case file is empty
            builds = { name:[build] }

        with open('build_list.json', 'w') as file:
            json.dump(builds, file)

        print('Entry successfully added.')
        
    # This codes deals with adding a build to a persons build's list.
    elif option == '2':
        
        name = input('Enter the name of the person you want to add a build to. ')
        new_build = input('Now enter their new build to add it to the list. ')

        try:
           with open('build_list.json','r') as file:
               builds = json.load(file)
       
           if name in builds.keys():
            
               # Adding a build to an already existing list.
               print('Name found.')
               builds[name].append(new_build)

               with open('build_list.json','w') as file:
                   json.dump(builds,file)
           else:

               print('name not found try again.')

        except:
            print('The file probably contains no entries. Try again')

            print('Build added.')
            
    # Exits the program.
    elif option == '3':
        break

    # search code
    else:
        try:
            with open('build_list.json','r') as file:
                builds = json.load(file)
            if option in builds.keys():
                print(builds[option])
            else:
                print('Name not found.')
        except:
             print('The file probably contains no entries. Try again.')
    

        

