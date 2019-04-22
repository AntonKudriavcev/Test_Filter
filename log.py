import time 

time_of_creation = ''
time_of_start    = ''

def txt_creator(): 
    with open(str(time_of_creation + '.txt'),'w', encoding = 'utf-8') as txt_file:
        txt_file.write(time_of_creation + '\n' + '\n')
        txt_file.write('TIME\tVALUE\n')
##=====================================================================================
##
##=====================================================================================
def write_to_log(value):
    with open(str(time_of_creation + '.txt'),'a', encoding = 'utf-8') as txt_file:
        txt_file.write('{0}\t{1}\n'
                .format(round((time.perf_counter() - time_of_start),3),value))