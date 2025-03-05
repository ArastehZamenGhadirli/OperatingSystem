import re
import hashlib
import os 

class FileMangment:
    def __init__(self):
        
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
    def cd(self,path:str):
        if len(path)==0:
            self.current_folder = self.root
        
        folders=path.strip("/").split("/")  
        if path[0] !="/":
            destination=self.current_folder
        else :
            destination=self.root
        
        for folder_name in folders:
            if not folder_name and folder_name==".":
                continue
            if folder_name=="..":
                if destination==self.root :
                    print("Error:Already at root folder")
                
                else :
                    destination = destination.parent
            
            else :
                found=False 
                for item in destination.contents:
                    if isinstance(item)
                
                   
        
            
    def mkdir(self):
        pass
    def ls(self,path):
        pass
        
    def rm(self):
        pass
    def cp(self):
        pass
    def cat(self):
        pass
    def mv(self):
        pass
    
    
    
class File:
    def __init__(self,name,data=None,password_hash=None):
        self.data=data if data else []
        self.name=name
        self._password_hash=password_hash
    
    def hash_password(self,password):
        
        return hashlib.sha256(password.encode()).hexdigest()
    
    def is_encrypted(self):
        if self.name.startswith("."):
            return True
        else :
            False 
    
    def read(self):
        if self.is_encrypted():
            password =input(f"please enter a password for {self.name} : ")
            if self.hash_password(password) != self._password_hash:
                return "Incorrect Password"
        return self.data
    
    def write(self,new_data):
        return self.data.append(new_data)
        
    
    
    
    
    
        
    def to_dict():
        pass
    
   

class Folder:
    def __init__(self,name,parent=None):
        self.name=name
        self.contents=[]
        self.parent=parent

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
     
    
       
