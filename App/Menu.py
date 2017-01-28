# Offensive Cyber Tools For Offensive Security/Penetration Testing Assignments 
# Connect on LinkedIn  https://www.linkedin.com/in/lismore or Twitter @patricklismore
#=========================================================================================================================================

# Offensive Cyber Tools
menu = {}
menu['1']="Shells" 
menu['2']="Exploits"
menu['3']="Scanners"
menu['4']="Payloads"
menu['5']="Scripts"
menu['6']="Utilities"
while True:
                print ""
                print "==============Offensive Cyber Tools================="
                print ""
                options=menu.keys()
                options.sort()

                for entry in options:
                        print entry, menu[entry]
                print ""
                selection=raw_input("Please Select:") 
                if selection =='1': 
                        print "Shells" 
                elif selection == '2': 
                          print "Exploits"
                elif selection == '3':
                          print "Scanners" 
                elif selection == '4':
                        print "Payloads"
                elif selection == '5':
                        print "Scripts"
                elif selection == '6':
                        print "Utilities"
                        break
                else: 
                  print "Unknown Option Selected!"
