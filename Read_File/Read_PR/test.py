import shutil
import os

def Copy_Bin_File(Drop_File):
    target_directory=r'C:\aa'
    Not_match='old.bin'
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
    else:
        print('File Already Exists ')
    
    absolute_input_path = os.path.abspath(Drop_File)
    print(absolute_input_path)
    Drop_file_name=os.path.basename(Drop_File)
    print(Drop_file_name)
    with open(Drop_file_name,'rb') as f:
        a=f.read()
    target_hex=b'\x5A\xA5\xF0'
    offset=a.find(target_hex)
    if offset != -1:
        if offset ==0x10:
            print(True)
            next_three_bytes = a[0x10:0x13]
            if next_three_bytes == target_hex:
                print(f"Hex value {target_hex.hex()} matches")
                target_path=os.path.join(target_directory,os.path.basename(Drop_File))
                shutil.copy(absolute_input_path,target_path)
            else:
                print(f"Hex value {target_hex}  not match")
                target_path=os.path.join(target_directory,Not_match)
                shutil.copy(absolute_input_path,target_path)
        else:
            print(False)
            print(f"offset value {offset:#x}  not match to Offset{hex(0x10)} ")
            target_path=os.path.join(target_directory,Not_match)
            shutil.copy(absolute_input_path,target_path)
    else:
        print("Hex Not Found")

    return target_path

x=r'C:\Users\Sk Official\Desktop\Read_File\X513EAN.302'
x=Copy_Bin_File(x)
print(f"File copied to: {x}")