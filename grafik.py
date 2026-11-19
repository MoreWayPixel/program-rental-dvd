import os

import inquirer
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MaxNLocator

from data import koleksi_dvd, data_transaksi
from tema import tema_admin
from utils import total_harga