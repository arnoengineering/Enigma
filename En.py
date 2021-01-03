import random
import numpy as np
# import alfa
file = '' # file stored rots


class Rotor:
    def __init__(self, num, pos):
        self.rot_li_in = []
        self.rot_li = []  # click from after init
        self.num = num  # if 0 fo x
        self.pos = pos

        self.rot(pos)
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
        self.save_rot()
        # todo save to file, return

    def read_rot(self):  # multi rot

        """try:
        read file[num].lines
        else:
        create"""
        with open(file) as f:
            rot_line = f.readlines()
        self.rot_li = rot_line

    def save_rot(self):
        """dict = {num: list}
        pandas.to_csv. append list
        """
        pass  # pand


class RotorList:
    def __init__(self):
        self.output = 0
        self.rot_num_pos = {}  # rot num, pos
        self.rot_obj = []
        self.rot_pos = []  # creat onl one ist
        self.rev_rots = []

        # input num, run click till num

    def rand_rot_ass(self):
        num = random.sample(range(0, 5), 3)
        pos = random.sample(range(0, 26), 3)
        self.rot_num_pos[num] = pos

    def mir(self):  # click before?
        for rot in self.rot_obj:
            rev_ls = [pair.reversed() for pair in rot.rot_ls]
            self.rev_rots.append(rev_ls)
        pass

    def rot_scram(self, inp):
        sl = [sorted(r.rot_ls, key=lambda x: x[0]) for r in self.rot_obj]  # , sorted(r2), sorted(r3)  # keys
        for ro in sl:
            inp = ro[inp][1]  # second val from imp
        self.output = inp

    def click(self):
        x = 0
        # for r in self.rot_num:
        while True:
            self.rot_pos[x] = (self.rot_pos[x] + 1) % 26
            self.rot_obj[x].rot()  # witch
            if self.rot_pos[x] != 0:
                break
            x = (x + 1) % len(self.rot_pos)

    def run_rot(self, inp):
        self.rot_scram(inp)
        # self.output += 1
        self.mir()
        self.rot_scram(self.output)
        self.click()

    def rot_init(self):
        # if len(self.rot_num) == 0:  # nothing added, do l hear
        #     pass
        for n, pos in (self.rot_num_pos.items()):
            r = Rotor(n, pos)  # numper of each rot

            self.rot_obj.append(r)   # have each do itself?

    def ret_rot(self):  # or file
        pass


class PlugBoard:
    def __init__(self):
        self.plugs = []
        # save plug init

    def swap(self, let):
        let = self.plugs[let][1]
        return let

    def create_pairs(self):
        self.plugs = np.random.choice(range(26), size=(10, 2), replace=False)

    def add_rev(self):
        plug_rev = [pair.reversed() for pair in self.plugs]
        self.plugs += plug_rev  # all in
        self.plugs = sorted(self.plugs, key=lambda x: x[0])


def enigma():
    # init rot
    rot_choice = list(input('Rotor xyz from 1-5; i.e. (234): '))
    plug_choice = list(input('rot(234): '))
    if len(rot_choice) == 0:
        rot_board.rand_rot_ass()  # rand num
        pass
    else:
        rot_start = input('Rotor start local from 0-25; i.e. (23,5,4): ').replace(' ', '').split(',')
        if len(rot_start) == 0:
            pass  # do what
        rot_board.rot_num_pos = dict(zip(rot_choice, rot_start))
    rot_board.rot_init()

    # in plug
    if len(plug_choice) == 0:
        plugs.create_pairs()
    else:
        pl = input('Rotor start local from 0-25; i.e. (23,5,4): ').replace(' ', '').split(',')  # fix pairs
        plugs.plugs = pl
    plugs.add_rev()


def let_con(let):
    pass


def on_let(let):
    # run plug
    let = plugs.swap(let)
    rot_board.run_rot(let)
    out_let = rot_board.output
    return plugs.swap(out_let)


def string_decode(st):
    n_lets = [on_let(let) for let in st]
    return n_lets


rot_board = RotorList()  # fix
plugs = PlugBoard()

# decode
string = input('code str:')
"""if st>0
 string
 else let,
 run till escape

# for s in string:"""
