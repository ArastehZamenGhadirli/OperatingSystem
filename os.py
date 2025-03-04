import re
import hashlib
import os 

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
    def __init__(self,name,data=None ,password_hash=None):
        self.data=data if data else []
        self.name=name
        self._password_hash=password_hash
    
    def hash_password(self,password):
        
        return hashlib.sha256(password.encode()).hexdigest()
    
    def is_encrypted(self):
        return self.name.startswith(".")
    
    def read(self):
        
    def get_content(self):
        return self.content 
    
    def set_content(self,content):
        self.content=content
        
    def to_dict():
        pass
    
   

class Folder:
    def __init__(self,name,files):
        self.name=name
        self.contents=[]

    def add_item(self,item):
        self.contents.append(item)
    
    def remove_item(self,item_name):
        for item in self.contents:
            if item.name==item_name:
                self.contents.remove(item)
            else :
                return f"{item_name} not found !!"
    
    def search_item(self,item_name):
        for item in self.contents:
            if item.name==item_name:
                return item 
            else :
                return None
    
    def list_contents(self):
        return [item.name for item in self.contents]
     
    
       
