from PIL import Image as ImagePIL
from os import remove

def crop(path):
	img = ImagePIL.open(path)
	x, y = img.size
	if y > x:
		cost = y / 2
		first_part_image = img.crop((0,0,x,cost + 20))
		second_part_image = img.crop((0,cost - 20,x,y))
		img.close()
		orig_filename, ext_filename = path.split("/")[-1].split(".")
		save_path = path[:-len(path.split("/")[-1])]
		#finnaly_name = u"{}{}.1.{}".format(save_path,orig_filename,ext_filename)
		first_part_image.save("{}{}.1.{}".format(save_path,orig_filename,ext_filename))
		second_part_image.save("{}{}.2.{}".format(save_path,orig_filename,ext_filename))
		remove(path)
	else:
		print "dont touch file: {}".format(path)
		return False
