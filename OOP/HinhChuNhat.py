class HinhChuNhat:

    # constructor co tham so
    def __init__(self, chieuDai, chieuRong):
        self.chieuDai= chieuDai
        self.chieuRong= chieuRong


    # constructor khong tham so
    def __init__(self)-> None:
        pass
    
    # dien tich
    def dienTich(self):
        return self.chieuDai * self.chieuRong
    
    # chu vi
    def chuVi(self):
        return (self.chieuDai + self.chieuRong)/2
    
    # ham xuat thong tin
    def printInfor(self):
        print ('Chu vi hinh chu nhat: ',self.chuVi())
        print('Dien tich hinh chu nhat: ', self.dienTich())

    # getter setter
    def setChieuDai(self, chieuDai):
        self.chieuDai=chieuDai
    
    def setChieuRong(self, chieuRong):
        self.chieuRong=chieuRong

    def getChieuDai(self):
        return self.chieuDai
    
    def getChieuRong(self):
        return self.chieuRong

def main():
    # khoi tao constructor co tham so
    # hcn= HinhChuNhat(4,5)

    # khoi tao constructor khong tham so
    hcn= HinhChuNhat()
    hcn.setChieuDai(10)
    hcn.setChieuRong(5)
    hcn.printInfor()
    
if __name__=='__main__':
    main()