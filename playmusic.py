from arcade import load_sound, play_sound, stop_sound

import time

sound = load_sound("music/yellow.mp3")
# 开始播放
player = play_sound(sound)

time.sleep(4)

# 停止播放
stop_sound(player)

