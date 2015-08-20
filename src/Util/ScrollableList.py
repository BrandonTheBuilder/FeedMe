
class ScrollableList(list):
    
    def __init__(self, contents):
        self.index = 0
        self.end = len(contents)-1
        self.extend(contents)
        
    def current(self):
        return self[self.index]
    
    def previous(self):
        self.index -= 1
        if self.index < 0:
            self.index = self.end
        return self[self.index]
    
    def next(self):
        self.index += 1
        if self.index > self.end:
            self.index = 0
        return self[self.index]
        
        