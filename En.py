import random
import numpy as np
# import alfa
file = '' # file stored rots


def read_rot():  # multi rot
    with open(file) as f:
        rot_line = f.readlines()
    return rot_line


class Rotor:
    def __init__(self):
        self.rot_li = []
        # self.incon = incon

    def rot(self, cl=1):
        t_rot = []
        for t in self.rot_li:
            tu = []  # place
            for x in t:
                x = (x + cl) % 26  # forst
                tu.append(x)
            t_rot.append(tu)
        self.rot_li = t_rot

    def create_rotor(self):
        lis = range(0, 25)
        random.shuffle(lis)
        self.rot_li = [(num, y) for num, y in enumerate(lis)]
        # todo save to file, return


class RotorList:
    def __init__(self, rotor_list):
        if len(rotor_list) == 0:
            pass
            # init_rotor()
        else:
            pass
        self.output = ''
        self.in_rot_ls = []
        self.rot_obj = []
        self.rot_list = self.in_rot_ls
        self.rev_rots = []
        self.rot_num = []
        for x in range(len(self.rot_list)):
             self.rot_obj.append(Rotor())   # have each do itself?
        # input num, run click till num

    def rand_rot_ass(self):
        self.in_rot_ls = random.sample(range(0,26), 3)

    def mir(self):  # click before?
        for rot in self.rot_list:
            rev_ls = [pair.reversed() for pair in rot]
            self.rev_rots.append(rev_ls)
        pass

    def rot_scram(self, inp):
        sl = [sorted(r, key=lambda x: x[0]) for r in self.rot_list]  # , sorted(r2), sorted(r3)  # keys
        for ro in sl:
            inp = ro[inp][1]  # second val from imp
        self.output = inp

    def click(self):
        x = 0
        # for r in self.rot_num:
        while True:
            self.rot_list[x] = (self.rot_list[x] + 1) % 26
            self.rot_obj[x].rot()  # witch
            if self.rot_list[x] == 0:  # do befor break, save n
                x = (x + 1) % len(self.rot_list)
            else:
                break

    def run_rot(self, inp):
        self.rot_scram(inp)
        self.mir()
        self.rot_scram(self.output)
        self.click()

    def grab_rot(self): # or file
        pass


class PlugBoard:
    def __init__(self):
        self.plug_l = {}
        self.plugs = []
        self.plug_rev = []  # temp can rep by rexex
        # save plug init

    def swap(self, let):
        let = self.plug_l[let][1]  # keyvalue pair, pair ten, then apeend rev of paired ten
        return let

    def s_string(self, st):  # idea if whole str
        for x, y in self.plugs:
            st.replace(x, y).replace(y, x)

    def create_pairs(self):  # ask user if creat random or presart
        plug_r = range(26)
        self.plug_l = np.random.choice(plug_r, size=(10, 2), replace=False)
        self.plug_rev = [pair.reversed() for pair in self.plug_l]


# init rot
rot_board = RotorList()
rot_choice = list(input('Rotor xyz from 1-5; i.e. (234): '))
plug_choice = list(input('rot(234): '))
if len(rot_choice) == 0:  # class(rot_list); def in_rot  runs after init and ifelse here does rot setup
    # in rots:  first init then if choices assin val else creat and ret
    rot_board.rand_rot_ass()
    pass
else:
    rot_start = input('Rotor start local from 0-25; i.e. (23,5,4): ').replace(' ','').split(',')
    if len(rot_start) == 0:
        pass  # do what
    rot_board.in_rot_ls = rot_start  # what about rot num
if len(plug_choice):
    pass

string = input('code str:')
for s in string:
