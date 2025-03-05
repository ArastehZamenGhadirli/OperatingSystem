import re
import hashlib
import os

class File:
    def __init__(self, name, data=None, password_hash=None):
        self.data = data if data else []
        self.name = name
        self._password_hash = password_hash

    def hash_password(self, password):

        return hashlib.sha256(password.encode()).hexdigest()

    def is_encrypted(self):
        if self.name.startswith("."):
            return True
        else:
            False

    def read(self):
        if self.is_encrypted():
            password = input(f"please enter a password for {self.name} : ")
            if self.hash_password(password) != self._password_hash:
                return "Incorrect Password"
        return self.data

    def write(self, new_data):
        return self.data.append(new_data)

    def to_dict():
        pass







class Folder:
    def __init__(self, name, parent=None):
        self.name = name
        self.contents = []
        self.parent = parent

    def add_item(self, item):
        self.contents.append(item)

    def remove_item(self, item_name):
        for item in self.contents:
            if item.name == item_name:
                self.contents.remove(item)
            else:
                return f"{item_name} not found !!"

    def search_item(self, item_name):
        for item in self.contents:
            if item.name == item_name:
                return item
            else:
                return None

    def list_contents(self):
        return [item.name for item in self.contents]




class FileMangment:
    def __init__(self):

        
        self.root = Folder("/")
        self.current_folder = self.root

    # def execute(self,cmd):
    #    parts = cmd.strip().split()
    #    command = parts[0]
    #    args = parts[:1]
    #    if command == "cd":
    #        self.cd(args)
    #    elif command == "mkdir":
    #        self.mkdir(args)
    # def cd(self,args):
    #    path = args[0]
    #    if path == "/":
    #        self.current_folder = self.path
    #    else:
    #        self.current_folder =
    def cd(self, path: str):
        if len(path) == 0:
            self.current_folder = self.root

        folders = path.strip("/").split("/")
        if path[0] != "/":
            destination = self.current_folder
        else:
            destination = self.root

        for folder_name in folders:
            if not folder_name and folder_name == ".":
                continue
            if folder_name == "..":
                if destination == self.root:
                    print("Error:Already at root folder")
                    return

                else:
                    destination = destination.parent

            else:
                found = False
                for item in destination.contents:
                    if isinstance(item, Folder) and item.name == folder_name:
                        destination = item
                        found = True
                        break
                if not found:
                    print(f"Error :Folder '{folder_name}' not found .")
                    return

        self.current_folder = destination

    def mkdir(self):
        pass

    def ls(self, path):
        pass

    def rm(self):
        pass

    def cp(self):
        pass

    def cat(self):
        pass

    def mv(self):
        pass






#test code for checking cd works well or not 



def print_current_folder(file_system):
    print(f"Current folder :{file_system.current_folder.name}")

file_system=FileMangment()

root = file_system.root
folder1 = Folder("folder1",parent=root)
folder2 = Folder("folder2",parent=folder1)
folder3 = Folder("folder3",parent=folder2)



root.add_item(folder1)
folder1.add_item(folder2)
folder2.add_item(folder3)


print("--- Test 1: Start at root ---")
print_current_folder(file_system)  # Expected: Current folder: root

print("\n--- Test 2: Navigate to folder1 ---")
file_system.cd("folder1")
print_current_folder(file_system) 

print("\n--- Test 3: Navigate to folder2 (relative path) ---")
file_system.cd("folder2")
print_current_folder(file_system)  

print("\n--- Test 4: Navigate to folder3 (relative path) ---")
file_system.cd("folder3")
print_current_folder(file_system)

print("\n--- Test 5: Navigate back to folder2 using '..' ---")
file_system.cd("..")
print_current_folder(file_system)

print("\n--- Test 6: Navigate back to root using absolute path ---")
file_system.cd("/")
print_current_folder(file_system)