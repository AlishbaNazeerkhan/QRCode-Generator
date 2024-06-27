import qrcode 
from PIL import Image

class QrCode:
    def __init__(self,version,error_correction,box_size,border,data,fill_color,back_color):
        self.version= version
        self.error_correction= error_correction
        self.box_size= box_size
        self.border= border
        self.data= data
        self.fill_color= fill_color
        self.back_color= back_color
        self.qr= None 

    #Set the properties of QR code.
    def set_properties_of_qr_code(self):
        self.qr= qrcode.QRCode(version= self.version,
                error_correction= self.error_correction,
                box_size= self.box_size,
                border= self.border,) 
        
        self.qr.add_data(self.data)
        self.qr.make(fit=True)
        

    # Create the QRCode.
    def create_qr_code(self):

        # set the properties
        self.set_properties_of_qr_code()
        img = self.qr.make_image(fill_color=(self.fill_color), back_color= (self.back_color))
        return img
        

        
    
if __name__=="__main__":
    version = 1
    error_correction = qrcode.constants.ERROR_CORRECT_Q
    box_size = 15
    border = 4
    data = "https://github.com/AlishbaNazeerkhan"
    fill_color = "#CFBDA5"
    back_color = "#000000"
    qr_code = QrCode(version,error_correction,box_size,border,data,fill_color,back_color)
    img = qr_code.create_qr_code()

    file_name = input("Enter filename with .png extension : ")
    img.save(f"{file_name}")
    print(f"QR code saved as {file_name}")

    
