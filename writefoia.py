import csv
import re
import string
import sys
import os
import shutil
from docx import Document
from docx.shared import Inches
from docx.shared import Pt
from docx.enum.style import WD_STYLE
from docx.enum.text import WD_ALIGN_PARAGRAPH
import datetime

reload(sys)
sys.setdefaultencoding('utf8')

