from kivy.app               import App
from kivy.core.window       import Window
from kivy.garden.graph      import Graph, LinePlot
from kivy.uix.button        import Button
from kivy.uix.togglebutton  import ToggleButton
from kivy.uix.boxlayout     import BoxLayout
from kivy.uix.gridlayout    import GridLayout
from kivy.uix.anchorlayout  import AnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.slider        import Slider
from kivy.uix.widget        import Widget
from kivy.uix.label         import Label
from kivy.clock             import Clock

import time

##=====================================================================================
##----------------------------------import screens-------------------------------------
##=====================================================================================

import SCREEN_main

##=====================================================================================
##----------------------------------import module--------------------------------------
##=====================================================================================

import generator
import filterr
import log

##=====================================================================================
##
##=====================================================================================

class SCREEN(Screen):
    def __init__(self, **kw):
        super(SCREEN, self).__init__(**kw)       
        self.graph = LinePlot(line_width = 1.2, color = [.62,.93,.25,1])          
        self.ids.graph.add_plot(self.graph)
##=====================================================================================
##
##=====================================================================================        
    def start_stop(self, start_control):
    	if start_control == 'down':
    		generator.start = True
    		self.ids.start_control.text = 'СТОП'
    		self.ids.switch_log.touch_control = False
    		if self.ids.switch_log.active == True:
    			generator.write_to_log = True
    			log.time_of_creation = str(time.strftime('%d.%m.%Y_h%Hm%Ms%S'))
    			log.time_of_start    = time.perf_counter()               
    			log.txt_creator()
    		Clock.schedule_interval(self.get_voltage, 0.001)
    	else:
    		generator.start = False
    		self.ids.start_control.text = 'СТАРТ'
    		self.ids.switch_log.touch_control = None
    		Clock.unschedule(self.get_voltage)
##=====================================================================================
##
##=====================================================================================
    def get_voltage(self,dt):
    	self.graph.points = [(i,j) for i, j in enumerate(filterr.points)]
##=====================================================================================
##
##=====================================================================================
    def frequency_changes(self, frequency):
    	generator.frequency = frequency	
##=====================================================================================
##
##=====================================================================================
    def switch_noise(self, state):
    	if state == 'down':
    		generator.noise = True
    		self.ids.switch_noise.text = 'OFF'
    	else:
    		generator.noise = False
    		self.ids.switch_noise.text = 'ON'
##=====================================================================================
##
##=====================================================================================
    def signal_amplitude_changes(self, value):
    	generator.amplitude = value
##=====================================================================================
##
##=====================================================================================
    def noise_amplitude_changes(self, value):
    	generator.noise_amp = value
##=====================================================================================
##
##=====================================================================================
    def size_of_average(self, value):
    	filterr.averaging_coefficient = value

sm = ScreenManager()
sm.add_widget(SCREEN(name = "SCREEN"))

class Main_app(App):
	def build (self):
		return sm


if __name__ == "__main__":
    Window.size           = (1024,768)
    Window.minimum_width  = (800)
    Window.minimum_height = (600)  
    Window.clearcolor     = (.22,.22,.26,1)
    Window.show()
    Main_app().run()