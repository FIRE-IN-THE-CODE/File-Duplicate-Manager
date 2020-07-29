'''
==========
Issues
==========
- Missing erase feature
- Missing comparison feature
- Repeats iterating items
- Folder exclusion feature doesn't work
- Doesn't change into the directories listed
- Implement an option to tell the user selecting directory is required
'''

import os
import shutil
import getopt
import sys

folders_only = False
user_choice = False
target_folder = ''
excluded_folder = ''


def usage():
    print('File Duplicate Manager')
    print('\n')
    print('Description: ')
    print('    File Duplicate Manager is a program that helps' \
          + ' to increase storage space by erasing duplicate files in a directory.')
    print('Note: Always make backups if the directory being worked on has sensitive files.')
    print('\n')
    print('Options: ')
    print('	-a	--all		searches all files and sub-directories in the current directory')
    print('	-c	--choose	gives the option for the user to choose which file to delete (Safest option)')
    print('	-d	--dir		searches all files and sub-directories in a specific directory')
    print('	-e	--exclude	selects a directory to exclude from search')
    print('	-f	--folders	searches and erases only duplicate folders')
    print('	-h	--help		prints usage information')
    print("	-s	--select	select a single folder to compare it\'s contents with the rest in the directory")

    print('Author: www.github.com/FIRE-IN-THE-CODE')


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
    print('The main function worked.')  # Debugging only - main function is not executing
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


def start():
    print('The start function worked.')  # Debugging only
    opts, args = getopt.getopt(sys.argv[1:], 'acd:e:fh', ['all', 'choose', 'dir=', 'except=', 'folders', 'help'])
    for o, a in opts:
        if o in ('-c', '--choose'):
            user_choice = True
        elif o in ('-f', '--folders'):
            folders_only = True
        elif o in ('-h', '--help'):
            usage()
            exit(0)
        elif o in ('-e', '--except'):
            excluded_folder = a
        elif o in ('d', '--dir'):  # Bug - this doesn't execute for god knows why
            print('OPTION D HAS EXECUTED.')  # debugging only
            target_folder = a
            print('The target folder is : %s' % (target_folder))  # Debugging only
            main()
        elif o in ('-a', '--all'):
            main()


if __name__ == '__main__':
    print('The first condition statement worked.')  # Debugging only
    start()
