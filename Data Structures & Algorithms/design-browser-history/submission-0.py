class BrowserHistory:
    def __init__(self, homepage: str):
        self.front_history = []
        self.back_history = [homepage]
        
    def visit(self, url: str) -> None:
        self.front_history = []
        self.back_history.append(url)

    def back(self, steps: int) -> str:
        while steps and len(self.back_history) > 1:
            self.front_history.append(self.back_history.pop())
            steps -= 1
        return self.back_history[-1]

    def forward(self, steps: int) -> str:
        while steps and self.front_history:
            self.back_history.append(self.front_history.pop())
            steps -= 1
        return self.back_history[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)