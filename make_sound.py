import winsound
import time


class Beat:
    def __init__(self, num_of_beat, bpm):
        self.bpm = bpm
        self.num_of_beat = num_of_beat


    def secondary(self):
        interval = int((60000 / self.bpm) * 4 / self.num_of_beat)
        for _ in range(1, self.num_of_beat):
            winsound.Beep(1000, interval)

    def primary(self):
        interval = int((60000 / self.bpm) * 4 / self.num_of_beat)
        winsound.Beep(1500, interval)

    def metronome(self):
        while True:
            Beat.primary(self)
            Beat.secondary(self)


def initiate():
    num_of_beat=int(input("请输入几分音符为一拍："))
    bpm=int(input("请输入想要的节拍速度："))
    a=Beat(num_of_beat, bpm)
    a.metronome()

initiate()


