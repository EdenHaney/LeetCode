class RecentCounter:

    def __init__(self):
        self.pings: list = []
        

    def ping(self, t: int) -> int:
        self.pings.append(t)
        while self.pings and (t - self.pings[0]) > 3000:
            self.pings.pop(0)
        return len(self.pings)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)