import sys
import os

# Giả sử file Student_HOF.py nằm trong thư mục Model nằm cùng cấp với file hiện tại
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Model.Student_HOF import *
from Service.Business import *


# Thêm dữ liệu vào cơ sở dữ liệu
if __name__ == "__main__":
    # listStudent()
    # printDiemTB()
    print(diemById(1))
