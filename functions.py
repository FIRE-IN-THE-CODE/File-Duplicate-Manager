import os
import shutil


def list_generator(new_list):
    print(new_list)  # Debugging
    new_list = []
    for x in new_list:
        dir_detect(x)
    return new_list


def dir_detect(sus_variable):
    print(sus_variable)  # Debugging
    if os.path.isdir(sus_variable):
        os.chdir(sus_variable)
    else:
        list_generator(sus_variable)
        os.chdir('../')


def main():
    gen_items = []

    try:
        print('Analyzing the target directory: %s' % (target_folder))
        os.chdir(target_folder)
    except FileNotFoundError:
        print('Error: The directory "%s" was not found.' % (target_folder))
        exit(0)

    if len(
            excluded_folder) > 0:  # Debugging - keep an eye on this condition because the delete function wasn't made yet
        print('[*] Excluding the folder "%s" from analysis.' % (excluded_folder))
    for i in os.listdir():
        print(i)  # Debugging only
        if i != excluded_folder:
            gen_items.append(i)
    for i in gen_items:
        dir_detect(i)
    if user_choice:
        print('[!] Duplicate files discovered.')  # Make this for only when scanning is enabled
        # Following line is out for debugging - variables are also undeclared
        # print ('One was discovered in %s and the other in %s.' %[Directory one, directory 2])
    print(
        'Options: 1 - delete the file in the first directory, 2 - delete the file in the second directory, 3 - do nothing')
