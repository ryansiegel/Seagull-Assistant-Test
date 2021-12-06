import discord,asyncio,os
from datetime import datetime, timedelta, date
from discord.ext import commands, tasks
from urllib import parse, request
import re
from discord.utils import get
import random
import string
import pymysql
from time import sleep
import requests

bot = commands.Bot(command_prefix='!', description="This is a Helper Bot")
