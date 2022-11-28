'''
Ung dung quan li chi tieu cho phep xem, them, xoa
List chi tieu bao gom cac khoan chi
Moi khoan chi

khoan_chi = {
    "ten": "mua nha",
    "so_tien": 200000000,
    "ngay": 18/11/2022
}
chi_tieu.append(khoan_chi)
'''

def them(chi_tieu, khoan_chi):
    chi_tieu.append(khoan_chi)
    
    
def xem(chi_tieu, khoan_chi):
    for khoan_chi in chi_tieu:
        print(khoan_chi)
        
def xoa(chi_tieu, ten_chi_tieu):
    index = -1
    for i in range(len(chi_tieu)):
        if ten == chi_tieu[i]['ten']:
            index = i
            break
    if index == -1:
        print("Khong tim thay khoan chi ", ten)
    else:
        chi_tieu.remove(chi_tieu[index])

chi_tieu = []

while True:
    yeu_cau = input("An 1 de xem chi tieu\n\
                     An 2 de them chi tieu\n\
                     An 3 de xoa chi tieu")
    if (yeu_cau == 1):
        print("Hien thi cac chi tieu")     
        xem(chi_tieu)
    elif (yeu_cau == 2):
        print("Them 1 chi tieu moi")
        ten = input("Nhap vao ten khoan chi: ")
        so_tien = int(input("Nhap vao so tien"))
        ngay = input("Nhap vao ngay chi")
        khoan_chi = {
            "ten": ten,
            "so_tien": so_tien,
            "ngay": ngay
        }
        them(chi_tieu, khoan_chi)
    elif (yeu_cau == 3):
        print("Xoa 1 chi tieu")
        ten = input("Nhap vao ten khoan chi can xoa: ")
        xoa(chi_tieu, ten)
    else:
        print("Ban nhap khong dung yeu cau")
        
    y_o_n = input("Ban muon tiep tuc (Y/N)?: ")
    if y_o_n.upper() == "N":
        break
            
            
            
            
            
            
    
    
    
    
    
    
    
    
    
    
    