import unicornhathd
from time import sleep

unicornhathd.brightness(0.5)
unicornhathd.clear()
unicornhathd.set_all(255, 0, 0)
unicornhat.show()
sleep(3)
unicornhat.off()