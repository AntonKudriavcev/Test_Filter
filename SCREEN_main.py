from kivy.lang              import Builder

Builder.load_string("""
#:import MeshLinePlot kivy.garden.graph.MeshLinePlot
<SCREEN>: 
	AnchorLayout:
        padding: 3
        spacing: 3
        anchor_x : 'right'
        anchor_y : 'top'
        GridLayout:
            cols: 1
            size_hint: 1, 1
            AnchorLayout:
                anchor_x: 'center'
                anchor_y: 'top'
                size_hint: (1, .2)
                Widget:
                    canvas:
                        Color:
                            rgba: .22,.22,.26,1
                        Rectangle:
                            size: self.size
                            pos: self.pos
                BoxLayout:   
                    Label:
                        text:'S   I   G   N   A   L'
                        font_size: 20
                        bold: True
            Graph:
                id: graph
                size_hint : [1, 4]
                plot: MeshLinePlot
                xlabel: "Time"
                ylabel: "Voltage"
                ylabel_pos: 'right'
                x_ticks_major:25
                y_ticks_major:0.55            
                y_grid_label : True
                padding:5
                x_grid:True
                y_grid:True
                xmin:0
                xmax: 500
                ymin:0
                ymax:3.5                
            AnchorLayout:
                anchor_x : 'right'
                anchor_y : 'bottom'
                GridLayout:
                    cols:    3
                    spacing: 3
                    padding: 5
                    BoxLayout:
                        orientation: 'vertical'
                        Label:
                        	text: 'FREQUENCY'
                        	font_size:14
                        BoxLayout:
                        	orientation: 'horizontal'
                        	Slider:
                            	id: frequency
                            	size_hint: [4,1]
                            	value_track : True
                            	value_track_color :[.62,.93,.25,1]
                            	range: (1,5)
                            	step:  1
                            	value: 1
                            	sensitivity: 'handle'
                            	on_touch_move: root.frequency_changes(frequency.value)
                        	Label:
                            	text: "%d" % frequency.value
                            	font_size:16
                        Label:
                        	text: 'SIGNAL AMPLITUDE'
                        	font_size:14
                        BoxLayout:
                        	orientation: 'horizontal'
                        	Slider:
                            	id: sig_amplitude
                            	size_hint: [4,1]
                            	value_track : True
                            	value_track_color :[.62,.93,.25,1]
                            	range: (0,1.2)
                            	step:  0.1
                            	value: 1.2
                            	sensitivity: 'handle'
                            	on_touch_move: root.signal_amplitude_changes(sig_amplitude.value)
                        	Label:
                            	text: "%.1f" % sig_amplitude.value
                            	font_size:16
                        Label:
                        	text: 'NOISE AMPLITUDE'
                        	font_size:14
                        BoxLayout:
                        	orientation: 'horizontal'
                        	Slider:
                            	id: noise_amplitude
                            	size_hint: [4,1]
                            	value_track : True
                            	value_track_color :[.62,.93,.25,1]
                            	range: (0, 0.45)
                            	step:  0.05
                            	value: 0
                            	sensitivity: 'handle'
                            	on_touch_move: root.noise_amplitude_changes(noise_amplitude.value)
                        	Label:
                            	text: "%.2f" % noise_amplitude.value
                            	font_size:16

                        Label:
                            text: 'SIZE OF AVERAGING'
                            font_size:14
                        BoxLayout:
                            orientation: 'horizontal'
                            Slider:
                                id: averaging
                                size_hint: [4,1]
                                value_track : True
                                value_track_color :[.62,.93,.25,1]
                                range: (0, 16)
                                step:  1
                                value: 0
                                sensitivity: 'handle'
                                on_touch_move: root.size_of_average(averaging.value)
                            Label:
                                text: "%d" % averaging.value
                                font_size:16

                    BoxLayout:
                        orientation: 'vertical'
                        Label:
                        	text: 'NOISE'
                        ToggleButton :
                        	id: switch_noise
                        	active: False
                        	text: "ON"
                        	font_size: 20
                        	bold: True
                        	color: [0,0,0,1]
                        	background_color : [.62,.93,.25,1]
                        	background_normal : ''
                        	on_press: root.switch_noise(switch_noise.state)

                    BoxLayout:
                        orientation: 'vertical'
                        BoxLayout:
                        	padding: 3
                        	orientation: 'horizontal'    
                        	Switch :
                            	id: switch_log
                            	active: False
                        	Label:
                            	text: 'записывать лог'
                            	font_size: 12
                        ToggleButton:
                        	id: start_control
                        	text: "СТАРТ"
                        	font_size: 20
                        	bold: True
                        	color: [0,0,0,1]
                        	background_color : [.62,.93,.25,1]
                        	background_normal : ''
                        	on_press: root.start_stop(start_control.state)             
""")