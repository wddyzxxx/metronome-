import winsound
import time


class Beat:
    def __init__(self, num_of_beat, bpm):
        self.bpm = bpm
        self.num_of_beat = num_of_beat

    def make_sound(self):
        while True:
            interval = int((60 / self.bpm) * 4 / self.num_of_beat) * 1000
            # start = time.time()
            winsound.Beep(4000, interval)
            for _ in range(1, self.num_of_beat):
                winsound.Beep(1000, interval)
                # time.sleep(1)
                # end = time.time()
                # print(end - start)

def initiate():
    num_of_beat=int(input("请输入几分音符为一拍："))
    bpm=int(input("请输入想要的节拍速度："))
    a=Beat(num_of_beat, bpm)
    a.make_sound()

initiate()


