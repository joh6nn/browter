#!/usr/bin/python
# -*- coding: UTF-8 -*-

import ConfigParser, os.path, sqlite3

class Config:
    description = "manage configuration for browter"
    def __init__(self, path=None):
    	if [path is None]:
    		path = "browter.ini"
    	self.path = path
    	self.config = ConfigParser.RawConfigParser(allow_no_value=True)
        self.config.read(self.path)

        self.settings = {}
        self.browsers = {}
        for opt in self.config.options('settings'):
            self.settings[opt] = self.config.get('settings', opt)

        for opt in self.config.options('browsers'):
            self.browsers[opt] = self.config.options(opt)

        connection = sqlite3.connect('browter.sqlite');
        self.db    = connection.cursor();

        self.db.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
        if 0 == len(self.db.fetchall()):
            self.db.execute('''CREATE TABLE browsers (name text, command text)''')
            self.db.execute('''CREATE TABLE patterns (pattern text, browser_name text)''')
            self.db.execute('''CREATE TABLE settings (name text, type text, number real, price real)''')

    def exists(self):
    	return os.path.isfile(self.path)

    def save(self):
    	with open(self.path, 'wb') as cfgfile:
    		self.config.write(cfgfile)

    def add_browser(self, browser):
    	#add browser to list of available browsers
    	self.config.set("browsers", browser);

    	#add section for patterns
    	self.config.add_section(browser);

    def add_pattern(self, browser, pattern):
    	self.config.set(browser, pattern);

    def del_browser(self, browser):
    	self.config.remove_option("browsers", browser)
    	self.config.remove_section(browser)

    def del_pattern(self, pattern):
    	self.config.remove_option("pattern", pattern)
