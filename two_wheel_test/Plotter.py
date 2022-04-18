import matplotlib.pyplot as plt

class Plotter:
    def __init__(self, 
                 robot, 
                 f=plt.figure(figsize=(10,10)), 
                 env=None, 
                 obstacles=None):
        self.robot = robot 
        self.env = env 
        self.obstacles = obstacles
        self.f = f
        self.ax = self.f.add_subplot(111)
        self.ax.set_aspect('equal')
        self.ax.grid()        
        
    def set_env(self):
        if self.env:
            x_min, x_max, y_min, y_max = self.env.get_area
            self.f.set_xlim = (x_min, x_max)
            self.f.set_ylim = (y_min, y_max)
            # 만들어지면 테스트 
        else: 
            print("env setting please")
            pass
    
    def draw(self):
        """각 환경 및 로봇의 위치를 그리게끔 지시
        
        """
        # set aspect: axis equal 
        # self.f = plt.axes(xlim=(-10,10), ylim=(-10,10))
        # self.ax.clear()
        self.ax.cla()
        self.ax.set_aspect('equal')
        self.ax.grid()
        self.ax.set_xlim([-10, 10])
        self.ax.set_ylim([-10, 10])
        
        if self.env: 
            self.env.draw(self.ax)
        if self.obstacles:
            self.obstacles.draw(self.ax)
        self.robot.draw(self.ax)
        
        self.ax.set_title("title")
    