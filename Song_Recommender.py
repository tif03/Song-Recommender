#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 18:13:28 2022

@author: tiffanyyu
"""
import random


song_dict = { "Dominic Fike": ["3 Nights", "Phone Numbers", "Why"], 
             "LANY": ["Malibu Nights", "ILYSB", "pink skies"], 
             "Lorde": ["Ribs", "Perfect Places", "Royals"], 
             "Taylor Swift": ["Our Song", "Red", "betty"], 
             "keshi": ["beside you", "drunk", "2 soon"], 
             "Conan Grey": ["People Watching", "Crush Culture", "Maniac"]}

def song_choice():
    print("Song Suggester!!\n=================\nInput an artist and get a song\nType stop to stop")
    print("Type add song to add a song\n")
    print("who do you want to listen to: ")
    usr_input = input()
    
    while usr_input != "stop":
        if usr_input == "add song":
            print("who is the song by: ")
            artist_input = input()
            if artist_input in song_dict.keys():
                print("song title: ")
                song_input = input()
                if song_input not in song_dict[artist_input]:
                    song_dict[artist_input] = song_input
                    print("Thanks for the recommendation! Song added to database")
                else:
                    print("Song already in database")
            
            elif artist_input not in song_dict.keys():
                print("song title: ")
                song_input = input()
                song_dict.update({artist_input, song_input})
                print("Thanks for the recommendation! Song added to database")
                
            print("\nwho else: ")
            usr_input = input()
            
        
        if usr_input not in song_dict.keys():
            print("This artist is not in the database! Would you like to add them (type yes or no)?")
            y_n = input()
            if y_n == "yes":
                print("list 3 songs: ")
                usr_3_songs = input().split(", ")
                song_dict.update({usr_input : usr_3_songs})
            if y_n == "no":
                break
            print("\nwho else: ")
            usr_input = input()
        
        else:
            val = random.randrange(len(song_dict[usr_input]))
            print("listen to: " + song_dict[usr_input][val])
            print("\nwho else: ")
            usr_input = input()

    
def main():
    song_choice()
    
    
if __name__ == '__main__':
    main()