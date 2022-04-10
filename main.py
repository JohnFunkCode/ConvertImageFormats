# Simple utility to recursively copy and convert .bmp files to .jpg files while preserving the original file date & time

def recursive_copy_bmp_images_to_jpg():
    import glob
    import re
    import filedate
    from PIL import Image

    _input_file_extension = 'BMP'
    _ignore_case_regex_pattern = re.compile(_input_file_extension, re.IGNORECASE)
    _output_file_extension = 'jpg'

    for input_file in glob.glob('E:\\pictures\\**\\*.'+_input_file_extension, recursive=True):
        # create a new name
        newname = _ignore_case_regex_pattern.sub(_output_file_extension, input_file)
        print("Copying {} to {}".format(input_file, newname))
        # save a new version of the image
        image = Image.open(input_file)
        image = image.convert('RGB')
        image.save(newname, quality=100, subsampling=0)
        # change the filedate to match the original
        filedate.Utils.copy(input_file, newname)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    recursive_copy_bmp_images_to_jpg()
