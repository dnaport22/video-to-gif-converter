from VideoConverter import *

vc = VideoConverter()

vc.input_file_name('big.mp4')
vc.output_file_name('iphone.gif')
vc.output_format('iphone')
vc.generate_gif()
