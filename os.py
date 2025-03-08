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

    def to_dict():  # it is for json
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
            end_folder = self.navigate_path(path)

        contents = end_folder.list_contents()
        if not contents:
            print(f"{end_folder} is empty")
        else:

            print(f"Contents of '{end_folder.name}':")
            for item in contents:
                print(f"-item")

        def rm(self, path: str):
            """
            Remove a file or folder at the specified path.
            :param path: The path to the file or folder to remove (e.g., "folder1/file.txt").
            """

        if not path:
            print("Error: No path provided.")
            return

        folders = path.strip("/").split("/")
        item_name = folders[-1]
        parent_path = "/".join(folders[:-1])

        if parent_path:
            parent_folder = self.navigate_path(parent_path)
        else:
            parent_folder = self.current_folder

        if not parent_folder:
            print(f"Error: Parent folder '{parent_path}' not found.")
            return

        item = parent_folder.search_item(item_name)
        if not item:
            print(f"Error: Item '{item_name}' not found in '{parent_folder.name}'.")
            return

        parent_folder.remove_item(item_name)
        print(f"Item '{item_name}' removed successfully from '{parent_folder.name}'.")


def cp(self, source_path: str, destination_path: str):

    if not source_path or not destination_path:
        print("Error: Source or destination path not provided.")
        return

    source_folders = source_path.strip("/").split("/")
    source_item_name = source_folders[-1]
    source_parent_path = "/".join(source_folders[:-1])

    # Navigate to the source parent folder
    if source_parent_path:
        source_parent_folder = self.navigate_path(source_parent_path)
    else:
        source_parent_folder = self.current_folder

    if not source_parent_folder:
        print(f"{source_parent_path}' not found.")
        return

    source_item = source_parent_folder.search_item(source_item_name)
    if not source_item:
        print(f"Error: Source item '{source_item_name}' not found ")
        return

    destination_folders = destination_path.strip("/").split("/")
    new_item_name = destination_folders[-1]
    destination_parent_path = "/".join(destination_folders[:-1])

    if destination_parent_path:
        destination_parent_folder = self.navigate_path(destination_parent_path)
    else:
        destination_parent_folder = self.current_folder

    if not destination_parent_folder:
        print(
            f"Error: Destination parent folder '{destination_parent_path}' not found."
        )
        return

    if destination_parent_folder.search_item(new_item_name):
        print(f"Error: An item with the name '{new_item_name}' already exists ")

    if isinstance(source_item, Folder):

        new_folder = Folder(new_item_name, parent=destination_parent_folder)
        destination_parent_folder.add_item(new_folder)
        for item in source_item.contents:
            new_folder.add_item(item)
    else:
        new_file = File(new_item_name, data=source_item.data)
        destination_parent_folder.add_item(new_file)

    print(f"Item '{source_item_name}' copied to '{destination_path}' successfully.")

    def cat(self, file_name: str):

        file = self.current_folder.search_item(file_name)
        if not file or not isinstance(file, File):
            print(f"{file} does not exist.")

        if file.is_encrypted():
            password = input(f"please enter password for {file}")
            if not file.verify_password(password):
                print("Error:incorrect password")
                return

        print(f"the contents of the file are :")
        for line in file.data:
            print(line)

        def mv(self, source_path: str, destination_path: str):

            if not source_path or not destination_path:
                print("Error: Source or destination path not provided.")
                return

        source_folders = source_path.strip("/").split("/")
        source_item_name = source_folders[-1]
        source_parent_path = "/".join(source_folders[:-1])

        if source_parent_path:
            source_parent_folder = self.navigate_path(source_parent_path)
        else:
            source_parent_folder = self.current_folder

        if not source_parent_folder:
            print(f"Error: Source parent folder '{source_parent_path}' not found.")
            return

        source_item = source_parent_folder.search_item(source_item_name)
        if not source_item:
            print(
                f"Error: Source item '{source_item_name}' not found in '{source_parent_folder.name}'."
            )
            return

        destination_folders = destination_path.strip("/").split("/")
        new_item_name = destination_folders[-1]
        destination_parent_path = "/".join(destination_folders[:-1])

        if destination_parent_path:
            destination_parent_folder = self.navigate_path(destination_parent_path)
        else:
            destination_parent_folder = self.current_folder

        if not destination_parent_folder:
            print(
                f"Error: Destination parent folder '{destination_parent_path}' not found."
            )
            return

        if destination_parent_folder.search_item(new_item_name):
            print(
                f"Error: An item with the name '{new_item_name}' already exists in '{destination_parent_folder.name}'."
            )
            return

        # Move the item
        source_parent_folder.remove_item(source_item_name)
        source_item.name = new_item_name
        destination_parent_folder.add_item(source_item)

        print(f"Item '{source_item_name}' moved to '{destination_path}' successfully.")



def main():
    
    file_system = FileMangment()
    while True:
        user_input=input(">").strip()
        if not user_input :
            continue
        
        
        parts= user_input.split()
        command = parts[0]
        args = parts[1:]
        
        if command == "cd":
            if len(args) != 1:
                print("Usage: cd <path>")
            else:
                file_system.cd(args[0])
        elif command == "ls":
            if len(args) > 1:
                print("Usage: ls [path]")
            else:
                file_system.ls(args[0] if args else None)
        elif command == "mkdir":
            if len(args) != 1:
                print("Usage: mkdir <name> [path]")
            else:
                file_system.mkdir(args[0])
        elif command == "rm":
            if len(args) != 1:
                print("Usage: rm <path>")
            else:
                file_system.rm(args[0])
        elif command == "cp":
            if len(args) != 2:
                print("Usage: cp <source_path> <destination_path>")
            else:
                file_system.cp(args[0], args[1])
        elif command == "mv":
            if len(args) != 2:
                print("Usage: mv <source_path> <destination_path>")
            else:
                file_system.mv(args[0], args[1])
        elif command == "exit":
            print("Exiting...")
            break
        else:
            print(f"Error: Unknown command '{command}'.")
            



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
