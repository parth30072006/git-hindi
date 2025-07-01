import sqlite3

conn = sqlite3.connect('ypitube_vidios.db')

cursor = conn.cursor()

cursor.execute('''
   CREATE TABLE IF NOT EXISTS videos(
              id INTEGER PRIMARY KEY,
              name  TEXT NOT NULL,
              time TEXT NOT NULL
            ) 
''')
def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name,time):
    cursor.execute("INSERT INTO videos(name,time) VALUES (?,?)",(name,time)) 
    conn.commit() 

def Update_video(video_id,new_name,new_time):
     cursor.execute("UPDATE videos SET name = ?,time = ? WHERE ID = ?",(new_name,new_time,video_id))  
     conn.commit() 

def delete_video(video_id ): 
    cursor.executes("DELETE FROM videos WHERE ID = ?",(video_id,)) 
    conn.commit()       

def main():
    while True:
        print("\n Youtube Manager app with db")
        print("1. List all youtube video ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video Details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")
        print(choice)
        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("enter video name: ") 
            time = input("enter video time: ")   
            add_video(name,time) 
        elif choice == "3":
            video_id=input("Enter video id:")
            name = input("enter video name: ") 
            time = input("enter video time: ")
            Update_video(video_id,name,time)
        elif choice == "4":
            video_id=input("Enter delete video id:")
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("Invalid Exit ")     

    conn.close()                  



if __name__ == "__main__":
    main()