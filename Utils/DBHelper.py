# -*- coding:utf-8 -*-

import MySQLdb

class DBHelper():
    def __init__(self, dbname, username, passwd, port=3306):
        self._dbname = dbname
        self._username = username
        self._passwd = passwd
        self._port = port

    def createTable(self, tablename):
        '''

        :param tablename:
        :return:
        '''

    def removeTable(self, tablename):
        '''

        :param tablename:
        :return:
        '''

