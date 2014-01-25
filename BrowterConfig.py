#!/usr/bin/python
# -*- coding: UTF-8 -*-

import ConfigParser, os.path

class Config:
    description = "manage configuration for browter"
    def __init__(self, path=None):
    	if [path is None]:
    		path = "browter.ini"
    	self.path = path
    	self.config = ConfigParser.RawConfigParser(allow_no_value=True)

    def exists(self):
    	return os.path.isfile(self.path)

    def read(self):
    	self.config.read(self.path)

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
