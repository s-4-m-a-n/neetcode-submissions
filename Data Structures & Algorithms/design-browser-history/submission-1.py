class BrowserHistory:

    def __init__(self, homepage: str):
         self.history = [homepage]
         self.curr_pos = 0

    def visit(self, url: str) -> None:
        self.curr_pos += 1
        self.history = self.history[:self.curr_pos]
        self.history.append(url)
        
    def back(self, steps: int) -> str:
        self.curr_pos = max(0, self.curr_pos-steps)
        return self.history[self.curr_pos]
        
    def forward(self, steps: int) -> str:
        self.curr_pos = min(len(self.history)-1, self.curr_pos + steps)
        return self.history[self.curr_pos]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)