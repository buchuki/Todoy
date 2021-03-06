from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from .gesturebox import GestureBox
from path import path


class GestureContainer(GestureBox):
    def __init__(self, *args, **kwargs):
        super(GestureContainer, self).__init__(*args, **kwargs)
        self.add_gesture("down_swipe",
            'eNq1l91yIkcMhe/nReybpVr/0guwt6nyA6Qcm7Kp3dgUsNns20ejxsyQOGFTruFm4ND9taTTqJvb7ZftHz9WT5vD8dt+M3w+PXdtuH3cwXB383L/++Zm2GG+zQcNh7ubw3H/+mVzyI883H7dyXD7LuSuhg07HVGW83ev25fjOM3HafEv034ZRw076BGMIfzIKYDDuq0EHULBUEJDnMdo/hy/pWH9qa0aIXkDbOZuKk1lOPx2/9/LcC0jw1NfgZ1aCyEEFGaxTPjpjc4t8aq5slm+w+vwSh3sDGcy0DFCz9iwyRyO2IgacUQosf9E6F70ONOhEVh4a4oZIemH6Fj1R3ijE5GGgXCAIIbax+hYdFqIXqaiLEQvV/HsKkZjE5AWLiHK/DF6uYpnV0ExvTQT40am7jP6/9/uVK4SLEQvV4kWoperJAvRy1U6uwpg4gYkmGTlbEQTHZ2lOZulv57LX+8EVK5SLEPncpXPrjZ2x9xsetqa8/2OKKKR1cnCZS9jvU4vV5kWoperfHK1vCP1cPNsxRJp8gwPrOEUEM119Nav48tWtqXw5SvHhO87DjxEoHE6PsM30wAYq5cngPzEppQyVmApfDkrdMaDAUKeUtnEWrbM+QmSpyJLkAJgUFZKrhdHylqRpfBlrdhS+LJWJmsvWrmet/1IT1MMWSU8f89ofBWuZaxOxhIxWqAGs2KeFDrR00vM9bBhU5UceJ1eviotRC9bVRail6tqC9HLVJ1MJTU1b5EAJnKQiU6ei1mwEXgafh1uZapNpvK4J7IjJirQY0Kzg0aY5WbNy1q73iWtHDVaAl122mRnnj6QzLz/knPj4Amed9YIlHyaMFC/zoz/CB72m83L+X5vOl7wzYbbdV6kV21Yq1I+jjvz4X4mYheji61E8RK9XYjSRSgRoovQReyilciti9RFLRFPIs/F1kPKJCYxr29d1LnIPU63WfB5PnfxlBGVKLSK+YvHEaf0isUV+3EXPT2q9OjEip4eYYnSQ4meHlV61E4je3oV2Dq96mJPT3Dsd9NLcwTypUbj8J64FBjfwD3xcmYN5u9M61WoQq1BuzHhF2I3JmIu5joXpbEcAa39bUgrFS5U+WcQ0PBiCL3HpuuUrFjfwc+b7dPzcfwrmf/K1nmXz0kpf98+Hp9LzSqyd/H4+nWzv3952NQXVve5UT/9vn7d7V8fvz10mGdpV5a70iw/RPaqaiSrvwDFYvqM'
            )

    def on_gesture(self, gesture_name):
        if gesture_name == "down_swipe":
            # I am shocked that widgets don't have a root
            # property
            self.get_root_window().children[0].screen_manager.current = "add_todo_screen"


class Todoy(BoxLayout):
    '''The root widget for the TodoyApp'''
    screen_manager = ObjectProperty()

    def __init__(self):
        super(Todoy, self).__init__()
        self.init_storage()

    def add_habit(self, interval, habit_name):
        '''Add a new habit. This creates a file in the habits/interval directory
        for the new habit. Each day that the habit was marked complete is recorded
        in that file.

        :param interval: either of the strings "daily" or "weekly".
        :param habit_name: the name of the habit to be added.'''
        assert interval in 'daily', 'weekly'
        habit_filename = self.root_path.joinpath('habits', interval, habit_name)
        habit_filename.open('w').close()

    def init_storage(self):
        '''Set up the directories for storing todos. I don't really know how
        they are gonna look. Right now, I'm thinking directories of
        appropriately formatted text files.
        '''
        self.root_path = path('~').expanduser().joinpath('.todoy').mkdir_p()
        habits = self.root_path.joinpath('habits').mkdir_p()
        habits.joinpath('daily').mkdir_p()
        habits.joinpath('weekly').mkdir_p()


class TodoyApp(App):
    '''The todoy.kv is attached to this app. It will hook up all the other
    objects itself. :class:`Todoy` is the root object that contains all the
    other elements and directs of the logic.'''
    pass


if __name__ == '__main__':
    TodoyApp().run()
