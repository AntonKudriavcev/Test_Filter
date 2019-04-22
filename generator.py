from   math         import sin, pi
import time
from   threading    import Thread 
import bufffer
import random
import log

U_0       = 1.65
amplitude = 1.2
frequency = 1
fi_0      = 0 

noise_amp = 0 

sampl_freq  = 50

U_ref            = 3.3
number_of_digits = 4095  

num_of_bits      = 12

start = False
noise = False

write_to_log = False

def voltage_level():
	i = 0
	while 1:
		if start == True:

			time_start = time.time()
			t     = i/sampl_freq

			if noise == False:
				voltage = (U_0 + amplitude*sin(2*pi*frequency*t + fi_0))
			else:
				voltage = (U_0 + amplitude*sin(2*pi*frequency*t + fi_0)) + random.uniform(-noise_amp, noise_amp)
##=====================================================================================
##
##=====================================================================================
			volt_digits_number = int(round(voltage*number_of_digits/U_ref, 0))
			bytes_volt = int.to_bytes(volt_digits_number, 3 , byteorder = 'big', signed = False)
			bits = bytes_volt.hex()[3:]
			bufffer.put_to_queue(bits)
##=====================================================================================
##
##=====================================================================================
			if write_to_log == True:
				log.write_to_log(bits)
			try:
				time.sleep((1 / sampl_freq) - (time.time() - time_start))
			except:
				time.sleep(1 / sampl_freq)
##=====================================================================================
##
##=====================================================================================
			i+=1
			if i == 500:
				i = 0

		else:
			bufffer.clear_buf()
			time.sleep(0.001)

get_level_thread = Thread(target = voltage_level)
get_level_thread.daemon = True
get_level_thread.start()










