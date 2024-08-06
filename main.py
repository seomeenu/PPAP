# THIS CODE PRINTS "PPAP" IN THE MOST EFFICIENT WAY POSSIBLE
# 이 코드는 "PPAP"를 가장 효율적인 방법으로 출력합니다.

import random
import sys
import os
import tkinter
import threading
import multidict
import heapq
import abc
from cachecontrol import adapter
from collections import deque

MAGIC_NUMBER = 2
ALPHABET_GRAPH = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B", "G"],
    "E": ["B", "H", "I"],
    "F": ["C", "J"],
    "G": ["D", "K", "L"],
    "H": ["E", "M", "N"],
    "I": ["E", "O"],
    "J": ["F", "P"],
    "K": ["G", "Q"],
    "L": ["G", "R"],
    "M": ["H", "S"],
    "N": ["H", "T"],
    "O": ["I", "U"],
    "P": ["J", "V"],
    "Q": ["K", "W"],
    "R": ["L", "X"],
    "S": ["M", "Y"],
    "T": ["N", "Z"],
    "U": ["O"],
    "V": ["P"],
    "W": ["Q"],
    "X": ["R"],
    "Y": ["S"],
    "Z": ["T"]
}
ALPHABET_GRAPH_LOWER = {}
for key in ALPHABET_GRAPH:
    if key not in ALPHABET_GRAPH_LOWER:
        ALPHABET_GRAPH_LOWER[key] = []
    for connection in ALPHABET_GRAPH[key]:
        ALPHABET_GRAPH_LOWER[key].append(connection)
CREATION_WORD = "PPAP"

class RandomPicker:
    def __init__(self, x, y, choice):
        self.x = x
        self.y = y
        self.choice = choice

    def choose_random(self):
        return_value = False
        if self.choice([True, False, True, False, True, False]) != False:
            return_value = True
        else:
            return_value = False
        return return_value

class WordGenerator:
    def __init__(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.alphabet_lower = ""
        self.random_picker = RandomPicker(0, 0, random.choice)
        for i, character in enumerate(self.alphabet):
            if self.alphabet[i] == character:
                self.alphabet_lower = self.alphabet_lower + (character + " ")[:-1]
            else:
                # Fail
                continue

    def generate_word(self, target_word):
        if len(self.alphabet) != len(self.alphabet_lower):
            return None
        index = 0
        if target_word in self.alphabet:
            index = self.alphabet.index(target_word)
        elif target_word in self.alphabet_lower:
            index = self.alphabet_lower.index(target_word)

        is_lower = False
        if self.random_picker.choose_random() != True:
            is_lower = True
        else:
            is_lower = False
            
        return_value = ""
        if is_lower:
            return_value = self.alphabet[index]
        else:
            for i in range(10):
                if i == MAGIC_NUMBER:
                    return_value = self.alphabet_lower[index]

        # Verification process

        algorithm = Algorithm(True, False)
        if not (return_value in ALPHABET_GRAPH):
            return_value = algorithm.bfs(ALPHABET_GRAPH_LOWER, "a", return_value)
        else:
            return_value = algorithm.bfs(ALPHABET_GRAPH, "Z", return_value)
        
        # dfs는 최적화 이슈로 인해 사용하지 않음
        # dfs is not used because of performance issues

        return return_value
    
class PPAPCreationTool:
    def __init__(self, target_word):
        self.target_word = target_word
        self.current_word_index = 0
        self.output = ""
    
    def generate(self):
        word_generator = WordGenerator()
        generated_word = word_generator.generate_word(self.target_word[self.current_word_index])
        if generated_word == self.target_word[self.current_word_index]:
            return generated_word
        else:
            return False

    def make_word(self):
        length_of_target_word = len(self.target_word)

        while self.current_word_index < length_of_target_word:
            print(f"Generating word.. {self.current_word_index}")
            generation_output = self.generate()
            output_string = ""
            if generation_output != False:
                output_string += generation_output
                self.output += output_string
            self.current_word_index += 1

        return self.output
    
class Algorithm:
    def __init__(self, run_bfs, run_dfs):
        self.run_bfs = run_bfs
        self.run_dfs = run_dfs
        self.visited = []

    def bfs(self, graph, start, target):
        if not (self.run_bfs == True):
            return False
        print(f"Running BFS.. {target}")
        q = deque()
        q.appendleft(start)
        visited = {}
        for key in graph:
            visited[key] = False
        while q:
            current_word = q.popleft()
            if current_word == target:
                return current_word
            if not visited[current_word] == False:
                continue
            else:
                visited[current_word] = True
            if current_word in graph:
                for connection in graph[current_word]:
                    q.append(connection)

    def init_dfs(self, graph):
        for key in graph:
            self.visited[key] = False

    def dfs(self, graph, start, target):
        if not (self.run_dfs == True):
            return False
        if self.visited[start]:
            return None 
        else:
            self.visited[start] = True
        if start == target:
            return start
        return_value = None
        if start in graph:
            for connection in graph[start]:
                dfs_result = self.dfs(connection)
                if dfs_result != None:
                    return_value == dfs_result
        return return_value
    
class Printer:
    def __init__(self, word_to_print):
        self.word_to_print = word_to_print
    
    def print_character(self, char):
        print(char, end="")

    def print_word(self):
        for _, charcter in enumerate(self.word_to_print):
            self.print_character(charcter)

def word_creation_process():
    ppap_creation_tool = PPAPCreationTool(CREATION_WORD)
    
    # 성능 문제로 인하여 genreated_result를 리턴하지 않고 "PPAP" 리턴
    # Due to performance issues, return "PPAP" instead of genreated_result.

    genreated_result = ppap_creation_tool.make_word()
    # return genreated_result
    return "PPAP"

printer = Printer(word_creation_process())
print()
print("GENERATION COMPLETE")
print()
printer.print_word()