# from pymongo import MongoClient
# MongoClient("mongodb+srv://youtubepy:PARTH%402006@cluster0.yed6xng.mongodb.net/")
# db = client["ytmanager"]
# video_collection = db["videos"]
# print(video_collection)


from pymongo import MongoClient

# Corrected MongoDB URI (assuming your password is 'PARTH@2006')

client = MongoClient("mongodb+srv://youtubepy:PARTH%402006@cluster0.yed6xng.mongodb.net/",tlsAllowInvalidcertificates=True)

# Accessing the 'ytmanager' database
db = client["ytmanager"]

# Accessing the 'videos' collection
video_collection = db["videos"] 

# Confirm the collection object
print(video_collection)

def add_video(name,time):
    video_collection.insert_one({"name":name,"time":time})

def list_videos():
    for video in video_collection.find():
        print(f"ID:{video['_id']},Name:{video['name']} and Time: {video['time']}")

def Update_video(name,time,video_id):
    video_collection.update_one({'_id':video_id},{"$set":{"name":new_name,"time":new_time }})

def delete_video(video_id):
    video_collection.delete_one({"_id":video_id})   

def main():
    while True:
        print("\n Youtube Manager app with db")
        print("1. List all youtube video ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video Details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("enter name: ")
            time = input("enter time: ")
            add_video(name,time)
        elif choice == '3':
            video_id = input("enter video_id: ")
            name = input("enter updated name: ")
            time = input("enter updated time: ")
            Update_video(name,time,video_id) 
        elif choice == '4':
            video_id = input("enter video_id: ")
            delete_video(video_id) 
        elif choice == '5':
            break
        else:
            print("INVALID CHOICE")                   

if __name__ == "__main__":
    main()    
