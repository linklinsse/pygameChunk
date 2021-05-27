from chunk import Chunk
import pygame
import random

class Chunk_map():

    def __init__(self, chunk_size = 10, map_size = 0):
        self.chunk_size = chunk_size
        self.map_size = map_size
        self.all_chunk = [[0 for i in range(map_size)] for j in range(map_size)]
        self.loaded_chunk = []
        self.old_loaded_chunk = []

        for i in range(map_size):
            for j in range(map_size):
                start = pygame.math.Vector2(x = chunk_size * i, y = chunk_size * j)
                end = pygame.math.Vector2(x = chunk_size * (i + 1), y = chunk_size * (j + 1))
                self.all_chunk[i][j] = Chunk(start = start, end = end)

    def update(self, entitys):
        for chunk in self.loaded_chunk:
            chunk.update(entitys)

        for chunk in self.old_loaded_chunk:
            if chunk not in self.loaded_chunk:
                chunk.unload(entitys)

    def load_chunk(self, x, y, entitys, margin_pos = 10):

        new_chunk = []

        if (x < 0 or y < 0):
            return

        i = int((x - margin_pos) / self.chunk_size)
        j = int((y - margin_pos) / self.chunk_size)

        if j > self.map_size - 1 or i > self.map_size - 1:
            return

        chunk = self.all_chunk[i][j]
        while (
                chunk and
                chunk.pos.start.x <= x + margin_pos and
                chunk.pos.start.y <= y + margin_pos and
                chunk.pos.end.x >= x - margin_pos and
                chunk.pos.end.y >= y - margin_pos
            ):
            while (
                chunk and
                chunk.pos.start.x <= x + margin_pos and
                chunk.pos.start.y <= y + margin_pos and
                chunk.pos.end.x >= x - margin_pos and
                chunk.pos.end.y >= y - margin_pos
            ):
                if chunk.loaded == False:
                    chunk.load(entitys)
                new_chunk.append(chunk)
                j += 1
                if j > self.map_size - 1:
                    break
                chunk = self.all_chunk[i][j]

            i += 1
            if i > self.map_size - 1:
                break
            j = int((y - margin_pos) / self.chunk_size)
            chunk = self.all_chunk[i][j]

        self.loaded_chunk = list(dict.fromkeys(self.loaded_chunk + new_chunk))

    def clear_chunk(self):
        self.old_loaded_chunk = self.loaded_chunk
        self.loaded_chunk = []

    def draw(self, surface, camera):
        for chunk in self.loaded_chunk:
            chunk.draw(surface, camera)
