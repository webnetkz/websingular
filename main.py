# coding=utf-8           # -*- coding: utf-8 -*-
import random
import requests
import base64
import json
import sys
import locale
import os
import re
import time
from functions import get_new_webdriver

def startApp():
  get_new_webdriver("https://www.dublinbet2020.com")


if __name__ == '__main__':
  startApp()
