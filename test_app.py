from flask import Flask, request, jsonify
import numpy as np
import pickle
import json
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from datetime import datetime, time
  
def test_app():
    assert 1000 == 1000


