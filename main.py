from project1 import Spotifun as sp

mySpoti = sp()

while True:
    cmd = input(">>> ").strip().split()
    
    if not cmd:
        continue
    
    command = cmd[0].lower()
    
    #==========ADDS==========
    if command == "adds":
        artist_id = int(cmd[1])
        artist_name = " ".join(cmd[2:])
        mySpoti.adds(artist_id,artist_name)
        print("added successfully")
     
    #==========ADDMS==========  
    elif command == "addms":
        music_name = cmd[1]
        artist_name = input("> ")
        year = int(input("> "))
        rating = int(input("> "))
        contents = {}
        i = 1
        while True:
            content = input("> ")
            if content == "$end":
                break
            contents[i] = content
            i += 1
        mySpoti.addms(music_name,artist_name,year,rating,contents)
            
    #==========ADDP==========      
    elif command == "addp":
        playlist_id = int(cmd[1])
        playlist_name = cmd[2]
        mySpoti.addp(playlist_id,playlist_name)  
    
    #==========ADDMP=========    
    elif command == "addmp":
        music_id = int(cmd[1])
        playlist_id = int(cmd[2])
        mySpoti.addmp(music_id,playlist_id)
    
    #=========SEARCHP========
    elif command == "searchp":
        playlist_id = int(cmd[1])
        mySpoti.searchp(playlist_id)
    
    #=========SEARCHW========   
    elif command == "searchw":
        artist_id = int(cmd[1])
        music_id = int(cmd[2])
        word = cmd[3]
        mySpoti.searchw(artist_id,music_id,word)
    
    #========SEARCHMP========    
    elif command == "searchmp":
        playlist_id = int(cmd[1])
        music_id = int(cmd[2])
        mySpoti.searchmp(playlist_id,music_id)
     
    #=========COUNTW=========    
    elif command == "countw":
        artist_id = int(cmd[1])
        music_id = int(cmd[2])
        word = cmd[3]
        mySpoti.countw(artist_id,music_id,word)
    
    #==========DELS==========    
    elif command == "dels":
        artist_id = int(cmd[1])
        mySpoti.dels(artist_id)
        print("removed successfully")
        
    #==========DELMS=========    
    elif command == "delmp":
        playlist_id = int(cmd[1])
        music_id = int(cmd[2])
        mySpoti.delmp(playlist_id,music_id)
    
    #==========showp==========    
    elif command == "showp":
        playlist_id = int(cmd[1])
        mySpoti.showp(playlist_id)
    
    
    elif command == "playm":
        artist_id = int(cmd[1])
        music_id = int(cmd[2])
        mySpoti.playm(artist_id,music_id)
    
        
    elif command == "undo_playm":
        mySpoti.undo_playm()
       
    #==========get_max_rated==========
    elif command == "get_max_rated":
        mySpoti.get_max_rated()
    
    #==========get_min_rated==========
    elif command == "get_min_rated":
        mySpoti.get_min_rated()
        
    #==========FINDS==========
    elif command == "finds":
        artist_id = int(cmd[1])
        mySpoti.finds(artist_id)
    
    #=========FINDMS=========
    elif command == "findms":
        music_name = cmd[1]
        mySpoti.findms(music_name)
    
    #=========PRINTS=========    
    elif command == "prints":
        mySpoti.prints()
    
    #==========CLS===========    
    elif command == "cls":
        mySpoti.cls()
        print("all the information were deleted")
    
    #==========EXIT==========
    elif command == "exit":
        break
    
    else:
        print("Unknown command")