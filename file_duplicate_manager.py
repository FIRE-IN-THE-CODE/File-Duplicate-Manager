import getopt
import sys
import functions


def usage():
    print('File Duplicate Manager')
    print('\n')
    print('Description: ')
    print('    File Duplicate Manager is a program that helps'
          + ' to increase storage space by erasing duplicate files in a directory.')
    print('Warning: Make a backup or use preview only mode if sensitive files are present.')
    print('\n')
    print('Options: ')
    print('	-a	--all		searches all files and sub-directories in the current directory')
    print('	-c	--choose	gives the option for the user to choose which file to delete (Safest option)')
    print('	-d	--dir		searches all files and sub-directories in a specific directory')
    print('	-e	--exclude	selects a directory to exclude from search')
    print('	-f	--folders	searches and erases only duplicate folders')
    print('	-h	--help		prints usage information')
    print("	-s	--select	select a single folder to compare it\'s contents with the rest in the directory")
    print('\n')
    print('Author: www.github.com/FIRE-IN-THE-CODE')


def main():
    folders_only = False
    user_choice = False
    target_folder = ''
    excluded_folder = ''

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
    main()
