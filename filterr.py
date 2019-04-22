

points        = []
signal_buffer = []  

U_ref            = 3.3
number_of_digits = 4095  

averaging_coefficient = 0

def send_to_filter(value):
	if averaging_coefficient == 0:
		if len(points) == 501:
			del(points[0])
		points.append(int(value,16)*U_ref/number_of_digits)

	else:
		signal_buffer.append(int(value,16)*U_ref/number_of_digits)
		if len(signal_buffer) == averaging_coefficient:
			point  = sum(signal_buffer) / len(signal_buffer)
			del(signal_buffer[0])
			if len(points) == 501:
				del(points[0])
			points.append(point)
##=====================================================================================
##
##=====================================================================================
		elif (len(signal_buffer) > averaging_coefficient):
			for i in range (int(len(signal_buffer) - averaging_coefficient)):
				point  = sum(signal_buffer) / len(signal_buffer)
				del(signal_buffer[0])
				if len(points) == 501:
					del(points[0])
				points.append(point)

def del_points():
	signal_buffer.clear()
	points.clear()


