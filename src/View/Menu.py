'''
Created on 22 jul 2015

@author: Emil
'''
import Tkinter as tk
from PIL import Image, ImageTk
from Tkconstants import LEFT, X, CENTER, RIDGE, N, RIGHT, W, E
from tkFont import BOLD
import tkFont
from View import GlobalFunc
import Controller

class Menu(object):
    START_GAME = "Start new game"
    SETTINGS = "Settings"
    MENU_HEADING = "Menu"
    INFO_MENU = "Menu (Esc)"
    INFO_EXIT = "Exit (x)"
    EXIT = "Exit"
    BACK = "Back"
    CREDITS_HEADING = "Credits"
    CREDITS_MUSIC = "Music"
    CREDITS_SOURCE = "Development"
    CREDITS_SOUND = "Sound effects"
    CREDITS_IMAGES = "Images"
    
    USER_NAME_FRAME = "usrNm"
    USER_NAME_WRAPPER = "usrNmWrp"
    
    FRAME_SETTING = "menu_settings"
    FRAME_ROOT = "menu_root"
    FRAME_START_GAME = "menu_start_game"
    FRAME_AI_SETTING = "menu_ai_setting"
    
    __root = None
    __controller = None
    
    def __init__(self, root, controller, *args, **kwargs):
        self.__root = root
        self.__controller = controller
    
    def DisplayMenu(self, event=None):
        GlobalFunc.RemoveAllChildren(self.__root)
            
        menuFrame = tk.Frame(self.__root)
        menuFrame.config(borderwidth=5, relief=RIDGE, background=Controller.Master.MasterController.RED)
        menuFrame.pack(anchor=CENTER)
            
        labelMenu = tk.Label(menuFrame, text=self.MENU_HEADING, background=Controller.Master.MasterController.RED)
        labelMenu.config(font=("Arial Black", 25, BOLD))
            
        menuFont = tkFont.Font(labelMenu, labelMenu.cget("font"))
        menuFont.configure(underline=True)
        labelMenu.config(font=menuFont)
        labelMenu.pack(fill=X, padx=10, pady=5)
            
        labelNewGame = tk.Label(menuFrame, text=self.START_GAME, background=Controller.Master.MasterController.RED)
        labelNewGame.config(font=("Arial Black", 20, BOLD))
        labelNewGame.bind("<Button-1>", lambda e:self.__controller.StartNewGame(e))
        labelNewGame.pack(fill=X, padx=10)
            
        labelSettings = tk.Label(menuFrame, text=self.SETTINGS, background=Controller.Master.MasterController.RED)
        labelSettings.config(font=("Arial Black", 20, BOLD))
        labelSettings.bind("<Button-1>", lambda e:self.__controller.ShowSettings())
        labelSettings.pack(fill=X, padx=10)
        
        labelSettings = tk.Label(menuFrame, text=self.CREDITS_HEADING, background=Controller.Master.MasterController.RED)
        labelSettings.config(font=("Arial Black", 20, BOLD))
        labelSettings.bind("<Button-1>", lambda e:self.__controller.Credits())
        labelSettings.pack(fill=X, padx=10)
        
        labelExit = tk.Label(menuFrame, text=self.EXIT, background=Controller.Master.MasterController.RED)
        labelExit.config(font=("Arial Black", 20, BOLD))
        labelExit.bind("<Button-1>", lambda e, root = self.__root:GlobalFunc.CloseWindow(e, root))
        labelExit.pack(fill=X, padx=10)
    
    def AddMenuText(self, menuArea):
        
        label = tk.Label(menuArea, text=self.INFO_MENU, justify=LEFT)
        label.bind("<Button-1>", self.__controller.OpenMenu)
        label.pack(side=LEFT, padx=5)
        
        labelClose = tk.Label(menuArea, text=self.INFO_EXIT, justify=LEFT)
        labelClose.bind("<Button-1>", lambda e, root=self.__root: GlobalFunc.CloseWindow(e, root))
        labelClose.pack()
        
    #TODO! Change settings to valid settings
    def ShowSettings(self, settings):
        musicToggle = settings.Music
        self.__menuVisible = False
        GlobalFunc.RemoveAllChildren(self.__root)
        
        settings = tk.Frame(self.__root)
        settings.config(borderwidth=5, relief=RIDGE, background=Controller.Master.MasterController.RED)
        settings.pack(anchor=CENTER)
        
        settingsHeading = tk.Label(settings, text=self.SETTINGS, background=Controller.Master.MasterController.RED)
        settingsHeading.config(font=("Arial Black", 25, BOLD))
            
        settingsFont = tkFont.Font(settingsHeading, settingsHeading.cget("font"))
        settingsFont.configure(underline=True)
        settingsHeading.config(font=settingsFont)
        
        settingsHeading.pack()
        
        soundFrame = tk.Frame(settings)
        soundFrame.pack()
        
        if musicToggle:
            music = self.GenerateLabel(soundFrame, "Music: ON")
            music.bind("<Button-1>", lambda e:self.__controller.MusicOff(music))
        else:
            music = self.GenerateLabel(soundFrame, "Music: OFF")
            music.bind("<Button-1>", lambda e:self.__controller.MusicOn(music))
        
        labelBack = tk.Label(settings, text=self.BACK, background=Controller.Master.MasterController.RED)
        labelBack.config(font=("Arial Black", 16, BOLD))
        labelBack.bind("<Button-1>", self.__controller.OpenMenu)
        labelBack.pack(fill=X)
        
    def ShowCredits(self, credits):
        GlobalFunc.RemoveAllChildren(self.__root)
        
        menuFrame = tk.Frame(self.__root)
        menuFrame.config(borderwidth=5, relief=RIDGE, background=Controller.Master.MasterController.RED)
        menuFrame.pack(anchor=CENTER)
            
        labelCredits = tk.Label(menuFrame, text=self.CREDITS_HEADING, background=Controller.Master.MasterController.RED)
        labelCredits.config(font=("Arial Black", 25, BOLD))
        labelCredits.pack(fill=X)
        
        sourceFrame = tk.Frame(menuFrame)
        sourceFrame.config(background=Controller.Master.MasterController.RED)
        sourceFrame.pack(fill=X)
        
        self.GenerateSecondLevelHeading(sourceFrame, self.CREDITS_SOURCE)
        
        for s in credits.Source:
            self.GenerateLabel(sourceFrame, s)
        
        musicFrame = tk.Frame(menuFrame)
        musicFrame.config(background=Controller.Master.MasterController.RED)
        musicFrame.pack(fill=X)
        
        self.GenerateSecondLevelHeading(musicFrame, self.CREDITS_MUSIC)
        
        for s in credits.Music:
            self.GenerateLabel(musicFrame, s)
            
        soundEffectFrame = tk.Frame(menuFrame)
        soundEffectFrame.config(background=Controller.Master.MasterController.RED)
        soundEffectFrame.pack(fill=X)
        
        self.GenerateSecondLevelHeading(soundEffectFrame, self.CREDITS_SOUND)
        
        for s in credits.SoundEffects:
            self.GenerateLabel(soundEffectFrame, s)
            
            
        imageFrame = tk.Frame(menuFrame)
        imageFrame.config(background=Controller.Master.MasterController.RED)
        imageFrame.pack(fill=X)
        
        self.GenerateSecondLevelHeading(imageFrame, self.CREDITS_IMAGES)
        
        for s in credits.Images:
            self.GenerateLabel(imageFrame, s)
        
        labelBack = tk.Label(menuFrame, text=self.BACK, background=Controller.Master.MasterController.RED)
        labelBack.config(font=("Arial Black", 16, BOLD))
        labelBack.bind("<Button-1>", self.__controller.OpenMenu)
        labelBack.pack(fill=X)
        
    def GenerateSecondLevelHeading(self, root, text, font=("Arial Black", 20, BOLD)):
        sourceHeading = tk.Label(root, text=text, background=Controller.Master.MasterController.RED)
        sourceHeading.config(font=font)
        sourceHeading.pack(fill=X)
        
    def GenerateLabel(self, root, text, font=("Arial", 20)):
        label = tk.Label(root, text=text, background=Controller.Master.MasterController.RED)
        label.config(font=font)
        label.pack(fill=X)
        
        return label