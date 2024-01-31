def on_button_pressed_a():
    basic.show_number(steps)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    datalogger.delete_log()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.clear_screen()
    music.play(music.tone_playable(523, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(494, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(523, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(494, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(523, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(392, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(392, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global steps
    steps += 1
    datalogger.log(datalogger.create_cv("steps taken", steps))
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

steps = 0
basic.show_string("HELLO")
steps = 0
datalogger.set_column_titles("steps taken")