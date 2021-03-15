import os

while True:
	os.system("tput setaf 2")
	ch = int(input('''
             Press 1: To Check Available Disks
             Press 2: To create Physical Volume
             Press 3: Check All Physical Volumes Information
             Press 4: Check Physical Volumes Information By PV Name
             Press 5: To create Volume Groups
             Press 6: Check All Volume Groups Information
             Press 7: Check Volume Groups Information By Name 
             Press 8: To Create Logical Volume
             Press 9: Check All Logical Volume Information
             Press 10 : Check Logical Volume Information By Name
             Press 11: To format Logical Volume
             Press 12: To Mount Logical Volume 
             Press 13: To Extend Logical Volume
             Press 14: To reduce Logical Volume
             Press 15: To Extend Volume Group
             Press 16: To Resize(Format) The Newly Extended/Reduced Partition
             Press 17: To Exit

             Enter Your Choice: '''))

	if ch == 1:
            os.system("fdisk -l")

	elif ch==2:
             print("\n")
             os.system("tput setaf 7")
             Disk1 = input("\n\n Enter Name of Disk:")
             os.system("pvcreate {}" .format(Disk1))
             os.system("tput setaf 3")
             print("\n\t\t\t***Physical Volume Created Successfully***")
             os.system("tput setaf 7")
             
	elif ch==3:
            os.system("pvdisplay")
            

	elif ch==4:
            Disk1 = input("\n\n Enter Name of Disk:")
            os.system("pvdisplay {}" .format(Disk1))
            

	elif ch==5:
              print("\n")
              os.system("tput setaf 7")
              Disk1 = input("\n\n Enter the name of 1st PV:")
              Disk2 = input("\n\n Enter the name of 2st PV:")
              name1 = input("Enter the name of Volume Group:")
              os.system("vgcreate {} {} {}" .format(name1,Disk1,Disk2))
              os.system("tput setaf 3")
              print("\n\t\t\t***Volume Group Created Successfully***")
              os.system("tput setaf 7")
              

	elif ch==6:
            os.system("vgdisplay")

	elif ch==7:
            name1 = input("Enter the name of Volume Group:")
            os.system("vgdisplay {}".format(name1))

	elif ch==8:
              print("\n")
              os.system("tput setaf 7")
              name1 = input("Enter the name of Volume Group:")
              name2 = input("Enter the name of  Logical Volume:")
              size1 = input("Enter the size in GB for your Logical Volume:")
              os.system("lvcreate --size {}G --name {} {}" .format(size1,name2,name1))
              os.system("lvdisplay {}/{}" .format(name1,name2))
              os.system("tput setaf 3")
              print("\n\t\t\t***Logical Volume Created Successfully***")
              os.system("tput setaf 7")
              

	elif ch==9:
            os.system("lvdisplay")

	elif ch==10:
            name1 = input("Enter the name of Volume Group:")
            name2 = input("Enter the name of  Logical Volume:")
            os.system("lvdisplay {}/{}" .format(name1,name2))


	elif ch==11:
               print("\n")
               os.system("tput setaf 7")
               name1 = input("Enter the name of Volume Group:")
               name2 = input("Enter the name of  Logical Volume:")
               os.system("mkfs.ext4 /dev/{}/{}" .format(name1,name2))
               os.system("tput setaf 3")
               print("\n\t\t\t***Logical Volume Formatted Successfully***")
               os.system("tput setaf 7")
               

	elif ch==12:
            while True:
                nf=int(input("""
                Press 1:To Mount On New Folder
                Press 2:To Mount On Existing Folder
                Press 3:Exit

                Enter Your Choice :
                """))
                if nf==1:
                    os.system("tput setaf 7")
                    mount_point = input("Enter New Folder Name:")
                    os.system("mkdir {}" .format(mount_point))
                    name1 = input("Enter the name of Volume Group:")
                    name2 = input("Enter the name of  Logical Volume:")
                    os.system("mount /dev/{}/{} {}" .format(name1,name2,mount_point))
                    os.system("df -h")
                    os.system("tput setaf 3")
                    print("\n\t\t\t***Logical Volume Mounted Successfully***")
                
                elif nf==2:
                    os.system("tput setaf 7")
                    mount_point = input("Enter Folder Name:")
                    name1 = input("Enter the name of Volume Group:")
                    name2 = input("Enter the name of  Logical Volume:")
                    os.system("mount /dev/{}/{} {}" .format(name1,name2,mount_point))
                    os.system("df -h")
                    os.system("tput setaf 3")
                    print("\n\t\t\t***Logical Volume Mounted Successfully***")

                elif nf==3:
                    break

                else:
                    print("Invalid Option")

                input("Press Enter To Continue")
                os.system("clear")

	elif ch==13: 
            print("\n")
            os.system("tput setaf 7")
            size1 = input("Enter the size in GB to extend in Logical Volume:")
            name1 = input("Enter the name of Volume Group:")
            name2 = input("Enter the name of  Logical Volume:")
            os.system("lvextend --size +{}G /dev/{}/{}" .format(size1,name1,name2))
            os.system("tput setaf 3")
            print("\n\t\t\t***Logical Volume Extended Successfully***")
            print("\n\t\t\t*** Resize The Volume To Use Extended Storage***")
            os.system("tput setaf 7")


	elif ch==14: 
            print("\n")
            os.system("tput setaf 7")
            size1 = input("Enter the size in GB to reduce in Logical Volume:")
            name1 = input("Enter the name of Volume Group:")
            name2 = input("Enter the name of  Logical Volume:")
            os.system("lvreduce --size -{}G /dev/{}/{}" .format(size1,name1,name2))
            os.system("tput setaf 3")
            print("\n\t\t\t***Logical Volume Extended Successfully***")
            print("\n\t\t\t*** Resize The Volume To Use Extended Storage***")
            os.system("tput setaf 7")

	
	elif ch==15:
		VgName=input("Enter Volume Group Name:")
		DiskName=("Enter Disk Name :")
		os.system("vgextend {} {}".format(VgName,DiskName))            
	
	elif ch==16:
                print("\n")
                os.system("tput setaf 7")
                name1 = input("Enter the name of Volume Group:")
                name2 = input("Enter the name of  Logical Volume:")
                os.system("resize2fs /dev/{}/{}" .format(name1,name2))
                os.system("tput setaf 3")
                print("\n\t\t\t***Newly Extended Partition Successfully Formatted***")
                os.system("tput setaf 7")
                
	elif ch==17:
		os._exit(1)
            
	else:    
               os.system("tput setaf 7")
               print("\nEnter Valid Number")

	input("Press Enter To Continue")
	os.system("clear")




