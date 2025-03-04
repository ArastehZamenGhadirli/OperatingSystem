import re
import hashlib

class FileMangment:
    def __init__(self,path:str):
        
        self.path = self.root
        self.root=Folder("/")
        self.current_folder=self.root 
    #def execute(self,cmd):
    #    parts = cmd.strip().split()
    #    command = parts[0]
    #    args = parts[:1]
    #    if command == "cd":
    #        self.cd(args)
    #    elif command == "mkdir":
    #        self.mkdir(args)
    #def cd(self,args):
    #    path = args[0]
    #    if path == "/":
    #        self.current_folder = self.path
    #    else:
    #        self.current_folder = 
            
    def mkdir(self):
        pass
    def ls(self,path):
        pass
        
    
    
    
class File:
    def __init__(self,name,data="",password=None,is_encrypted=False):
        self.data=data if data else []
        self.name=name
        self._password=password
    
    def get_content(self):
        return self.content 
    
    def set_content(self,content):
        self.content=content
        
    def to_dict():
        pass
    
    def is_encrypted(self):
        if self.name.startswith("."):
            return True
        else :
            return False

class Folder:
    def __init__(self,name,files):
        self.name=name
        self.files=files

    def add_folder(self):
        
