import numpy as np

class TwoWheelRobot:
    """2륜로봇 클래스 
    __init__ : 
        pos ([float,float]): position, 
        ang (float): degree,
        vel ([float,float]): velocity, 
        R (float): radius of robot =0.5 fix 
    """
    def __init__(self, pos=[0,0],vel=[0,0],head=0):
        self.pos = pos
        self.vel = vel
        self.head = head
        self.R = args["ROBOT_RADIUS"]    # robot radius
        self.dt = 1/args["SAMPLING_FREQ"]   # time resolution
        self.traj = []
    
    def set_pos(self,p):
        self.pos = p
        
    def set_vel(self,v):
        self.vel = v 
    
    def get_params(self):
        x,y = self.pos[0], self.pos[1]
        vl,vr = self.vel[0], self.vel[1]  
        head = self.head
        dt = self.dt
        L = 2*self.R    # wheel-base
        
        return x,y,vl,vr,head,dt,L
    
    def set_params(self,x,y,vl,vr,head):
        self.pos = [x,y]
        self.vel = [vl,vr]
        self.head = head 
        
    def move(self):
        x,y,vl,vr,head,dt,L = self.get_params()
        head = np.deg2rad(head)
        
        if vl == vr: 
            x = x + vl*dt*np.cos(head)
            y = y + vr*dt*np.sin(head)
            
        elif vl != vr:
            w = (vr-vl)/L
            rot_R = (L/2)*(vr+vr)/(vr-vl)
            cx = x - rot_R*np.sin(head)
            cy = y + rot_R*np.cos(head)
            
            dh = w*dt 
            dh_rad = dh

            rotate_center = np.array([x-cx,y-cy]).T
            rotate_matrix = np.array([[np.cos(dh_rad), -np.sin(dh_rad)],
                                      [np.sin(dh_rad), np.cos(dh_rad)]])
            
            rotate_w = rotate_matrix @ rotate_center
            
            x = cx + rotate_w[0]
            y = cy + rotate_w[1]
            head += dh
        else: 
            # TODOS: 뭐... 다른 기능을 넣던지.. 
            pass
        
        head = np.rad2deg(head)
        if head>180: 
            head -= 360
        if head<-180:
            head += 360
            
        # update param 
        self.set_params(x,y,vl,vr,head) 
        self.record()
        
    def record(self):
        x,y,_,_,head,_,_ = self.get_params()
        self.traj.append([x,y,head])
    
    def reset(self):
        self.traj = []
    
    def get_record(self):
        return self.traj 
    
    def sense(): 
        """센서 달아서 주변 거리 탐지 만들기
        """
        pass
    
    def draw(self,ax,index_=None):
        if index_ is None: 
            x,y,vl,vr,head,dt,L = self.get_params()
        else: 
            x,y,head = self.traj[index_]
            L = self.L

        # draw robot body 
        draw_circle = plt.Circle([x,y], L/2)
        ax.add_patch(draw_circle)
        
        # draw line
        hx = x + L/2*np.cos(np.deg2rad(head))
        hy = y + L/2*np.sin(np.deg2rad(head))
        
        draw_line = plt.Line2D((x,hx),(y,hy),color='r')
        ax.add_line(draw_line)
        
        if args["PLOT_TRAJ"]:
            T = self.traj
            x,y = [x for x,_,_ in T], [y for _,y,_ in T]
            ax.plot(x,y)
                