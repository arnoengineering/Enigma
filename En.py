import random
import numpy as np
import collections
import pandas as pd
import json
# import alfa
file_rot = 'rots.json'  # file stored rots
file_pos = 'pos.json'


def let_num(let):
    let = let.lower()
    let = ord(let) - 97
    return let


def num_let(n):
    let = chr(n + 97)
    return let


class Rotor:
    def __init__(self, num, pos=0):
        self.rot_li = []  # click from after init
        self.read_rot(num)
        self.pos = pos
        self.rot(pos)
        # self.incon = incon

    def rot(self, cl=1):
        t_rot = collections.deque(self.rot_li)
        t_rot.rotate(cl)
        self.rot_li = list(t_rot)

    def create_rotor(self):
        lis = list(range(0, 25))
        random.shuffle(lis)
        self.rot_li = lis
        self.save_rot()
        # todo save to file, return

    def read_rot(self, num):  # multi rot
        with open(file_rot) as fr:
            f = json.load(fr)
        rot_l = f['Rotors'][str(num)]
        rot_line = [let_num(i) for i in rot_l]
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
        self.mir_r = None

        # input num, run click till num

    def rand_rot_ass(self):
        num = random.sample(range(1, 5), 3)
        pos = random.sample(range(0, 26), 3)
        for x, y in zip(num,pos):
            self.rot_num_pos[x] = y

    def mir(self, inp):  # click before?
        inp = self.mir_r.rot_li[inp]
        self.output = inp

    def rot_scram(self, inp, rev=False):
        if rev:
            for ro in reversed(self.rot_obj):
                inp = ro.rot_li.index(inp)  # second val from imp
        else:
            for ro in self.rot_obj:
                inp = ro.rot_li[inp]  # second val from imp
        self.output = inp

    def click(self):
        x = 0
        # for r in self.rot_num:
        while True:
            no = self.rot_obj[x]
            no.pos = (no.pos + 1) % 26
            no.rot()  # witch
            if no.pos != 0:
                break
            x = (x + 1) % 3

    def run_rot(self, inp):
        self.click()

        self.rot_scram(inp)

        # self.output += 1
        self.mir(self.output)

        self.rot_scram(self.output, True)


    def rot_init(self):
        # if len(self.rot_num) == 0:  # nothing added, do l hear
        #     pass
        for n, pos in (self.rot_num_pos.items()):
            r = Rotor(n, pos)  # numper of each rot

            self.rot_obj.append(r)   # have each do itself?
        self.mir_r = Rotor(6)

    def ret_rot(self):  # or file
        pass


class PlugBoard:
    def __init__(self):
        self.plugs = list(range(26))
        # save plug init

    def swap(self, let):
        return self.plugs[let]

    def create_pairs(self):
        ar = np.random.choice(range(26), size=(10, 2), replace=False)
        for a in ar:
            self.plugs[a[0]] = a[1]
            self.plugs[a[1]] = a[0]

    def add_rev(self):
        # self.plugs = sorted(self.plugs, key=lambda x: x[0])
        pass


def enigma():
    # init rot
    is_file = '' # input('from file [y],n: ')
    # is_rot = ''  # infut f
    if is_file == 'y' or len(is_file) == 0:
        with open(file_pos) as fr:
            f = json.load(fr)
        # todo if rotoor alrady assigned
        rot_board.rot_num_pos = f['Rotors']
        plugs.plugs = f['PlugBoard']
    else:
        rot_choice = list(input('Rotor xyz from 1-5; i.e. (234): '))
        plug_choice = list(input('rot(234): '))
        if len(rot_choice) == 0:
            rot_board.rand_rot_ass()  # rand num
        else:
            rot_start = input('Rotor start local from 0-25; i.e. (23,5,4): ').replace(' ', '').split(',')
            if len(rot_start) == 0:
                rot_start = np.random.choice(range(26), size=(3, 1), replace=False)
            rot_board.rot_num_pos = dict(zip(rot_choice, rot_start))


        # in plug
        if len(plug_choice) == 0:
            plugs.create_pairs()
        else:
            pl = input('Rotor start local from 0-25; i.e. (23,5,4): ').replace(' ', '').split(',')  # fix pairs
            plugs.plugs = pl
        print('plugs: ', plugs.plugs)
        print('rot #',rot_board.rot_num_pos)
        # plugs.add_rev()
    rot_board.rot_init()


def on_let(let):
    # run plug
    let = let_num(let)
    let = plugs.swap(let)
    rot_board.run_rot(let)
    out_let = rot_board.output
    return chr(plugs.swap(out_let)+97)


def string_decode(st):
    n_lets = [on_let(let) for let in st]
    return n_lets


rot_board = RotorList()  # fix
plugs = PlugBoard()
enigma()
# decode
li = input('live: ')
if li == 'y':
    out_st = ''
    while True:
        in_p = input('')
        if in_p == ']':
            print(out_st)
            break
        l2 = on_let(in_p)

        out_st += l2

string = input('code str:')
ret_let = string_decode(string)
ret_st = ''.join(ret_let)
print(ret_st)
