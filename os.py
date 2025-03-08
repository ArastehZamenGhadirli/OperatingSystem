import re
import hashlib
import os


class File:
    def __init__(self, name, data=None, password_hash=None):
        self.data = data if data else []
        self.name = name
        self._password_hash = password_hash

    
    
    def verify_password(self, password):
        """
        Verify the password for an encrypted file.
        :param password: The password to verify.
        :return: True if the password is correct, False otherwise.
        """
        return self.password_hash == self._hash_password(password)

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

    def to_dict():#it is for json 
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

    def navigate_path(self, path: str):
        if not path:
            self.current_folder = self.root
            return

        folders = path.strip("/").split("/")
        if path[0] == "/":
            destination = self.root
        else:
            destination = self.current_folder

        for folder_name in folders:
            if not folder_name or folder_name == ".":
                continue
            if folder_name == "..":
                if destination == self.root:
                    print("Error: Already at root folder.")
                    return
                else:
                    destination = destination.parent
            else:
                for item in destination.contents:
                    if isinstance(item, Folder) and item.name == folder_name:
                        destination = item
                        found = True
                        break
                if not found:
                    print(f"Error: Folder '{folder_name}' not found.")
                    return None

        return destination
    
    
    

    def cd(self, path: str):
        """
        Change the current folder to the specified path.
        :param path: The path to navigate to (e.g., "folder1/folder2").
        """
        destination = self.navigate_path(path)
        if destination:
            self.current_folder = destination
            print(f"Current folder: {self.current_folder.name}")

    def mkdir(self, name: str, path: str):

        destination = self.navigate_path(path)
        if not destination:
            print(f"Error {path} not found")
            return

        else:
            destination = self.current_folder

        if destination.search_item(name):
            print(f"Error: A folder or file with the name '{name}' already exists.")
            return

        new_folder = Folder(name, parent=destination)
        destination.add_item(new_folder)
        print(f"{new_folder} is succesfully added to {destination.name}")

    def ls(self, path):
        if path:
            end_folder=self.navigate_path(path)
        
        contents = end_folder.list_contents()
        if not contents:
            print(f"{end_folder} is empty")
        else :
            
            print(f"Contents of '{end_folder.name}':")
            for item in contents:
                print(f"-item")
            
        

    def rm(self,path):
        pass

    def cp(self):
        pass

    def cat(self,file_name:str):
        
        file = self.current_folder.search_item(file_name)
        if not file or not isinstance(file,File) :
            print(f"{file} does not exist.")
        
        if file.is_encrypted():
            password=input(f"please enter password for {file}")
            if not file.verify_password(password):
                print("Error:incorrect password")
                return
        
        print(f"the contents of the file are :")
        for line in file.data:
            print(line)

    def mv(self):
        pass


# test code for checking cd works well or not


def print_current_folder(file_system):
    print(f"Current folder :{file_system.current_folder.name}")


file_system = FileMangment()

root = file_system.root
folder1 = Folder("folder1", parent=root)
folder2 = Folder("folder2", parent=folder1)
folder3 = Folder("folder3", parent=folder2)


root.add_item(folder1)
folder1.add_item(folder2)
folder2.add_item(folder3)


print("--- Test 1: Start at root ---")
print_current_folder(file_system)

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

print("\n--- Test 7: Navigate to folder3 using absolute path ---")
file_system.cd("/folder1/folder2/folder3")
print_current_folder(file_system)

print("\n--- Test 8: Try to navigate to a non-existent folder ---")
file_system.cd("invalid_folder")
print_current_folder(file_system)
