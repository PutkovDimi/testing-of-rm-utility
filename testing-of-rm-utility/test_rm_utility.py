# -*- coding: utf-8 -*-

import subprocess as sub
from basic_integration_test import BasicIntegrationTest

TOUCH = 'touch '  # creating files command
MKDIR = 'mkdir '  # creating directories command
DIR = 'dir'  # name of directory we create in the script
FILE = 'file'  # name of file we create in the script
RM = 'rm '  # an utility which we are testing here


class TestRmUtility(BasicIntegrationTest):

    def creating_directories_for_testing():
        """ Creates a directoty with a file
            and a single file for testing
        """
        proc = sub.Popen(MKDIR + DIR, shell=True, stdout=sub.PIPE)
        proc.communicate()
        proc = sub.Popen(TOUCH + DIR + '/' + FILE, shell=True,
                         stdout=sub.PIPE)
        proc.communicate()
        proc = sub.Popen(TOUCH + FILE, shell=True, stdout=sub.PIPE)
        print ("CREATING FILE FOR TESTING IS COMPLETED SUCCESSFULLY... ok\n")

    creating_directories_for_testing()

    def test_bad_test_with_dirs(self):
        """ Checks that rm can not remove 
            a directory without any flags
        """
        proc = sub.Popen(RM + DIR, shell=True, stdout=sub.PIPE)
        proc.communicate()
        print("\nRM CAN'T REMOVE A DIR WITHOUT FLAGS\n")
        self.assertNotEquals(proc.returncode, 0)

    def test_correct_test_with_files(self):
        """ Checks that rm can remove
            a file without any flags
        """
        proc = sub.Popen(RM + FILE, shell=True, stdout=sub.PIPE)
        proc.communicate()
        print("\nRM CAN REMOVE A FILE WITHOUT FLAGS\n")
        self.assertEquals(proc.returncode, 0)

    def test_correct_test_with_dirs(self):
        """ Checks that rm can remove
            a directory using -r flag
        """
        proc = sub.Popen(RM + '-r ' + DIR, shell=True, stdout=sub.PIPE)
        proc.communicate()
        print("\nRM CAN REMOVE AN UNEMPTY DIR USING '-r' FLAG\n")
        self.assertEquals(proc.returncode, 0)
