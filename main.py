import time, struct, os, colorama
from pypresence import *
import pypresence

print("""
██████╗░██╗░██████╗░█████╗░░█████╗░██████╗░██████╗░░░░░░░██████╗░██████╗░░█████╗░
██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗░░░░░░██╔══██╗██╔══██╗██╔══██╗
██║░░██║██║╚█████╗░██║░░╚═╝██║░░██║██████╔╝██║░░██║█████╗██████╔╝██████╔╝██║░░╚═╝
██║░░██║██║░╚═══██╗██║░░██╗██║░░██║██╔══██╗██║░░██║╚════╝██╔══██╗██╔═══╝░██║░░██╗
██████╔╝██║██████╔╝╚█████╔╝╚█████╔╝██║░░██║██████╔╝░░░░░░██║░░██║██║░░░░░╚█████╔╝
╚═════╝░╚═╝╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░░░░░░░╚═╝░░╚═╝╚═╝░░░░░░╚════╝░
""")

startup_info = open('data/startup.data')
stratup_data = startup_info.read()

if stratup_data == '0':
    print("[*] Source Code: https://github.com/ItsBlackZlol/mortal-rpc")
    print("[*] Please follow these instructions - ")

    clientid = input("\n[1] Enter your application's client ID >>> ")
    rpcstatus = input("[2] Enter your RPC status >>> ")
    rpcdetails = input("[3] Enter your RPC details >>> ")

    largeiconpic = input("[3] Enter your application's large icon's picture name >>> ")
    largeicontext = input("[4] Enter your application's large icon's name >>> ")
    smalliconpic = input("[5] Enter your application's small icon's picture name >>> ")

    with open('data/clientid.data', 'w') as f:
        f.writelines(clientid)
        f.close()
    with open('data/rpcstatus.data', 'w') as f:
        f.writelines(rpcstatus)
        f.close()
    with open('data/rpcdetails.data', 'w') as f:
        f.writelines(rpcdetails)
        f.close()
    with open('data/largeiconpic.data', 'w') as f:
        f.writelines(largeiconpic)
        f.close()
    with open('data/largeicontext.data', 'w') as f:
        f.writelines(largeicontext)
        f.close()
    with open('data/smalliconpic.data', 'w') as f:
        f.writelines(smalliconpic)
        f.close()
    with open('data/startup.data', 'w') as f:
        f.writelines('1')
        f.close()


if stratup_data == '1':
    print("[*] Source Code: https://github.com/ItsBlackZlol/mortal-rpc")
    print("[*] Discord Server: https://discord.gg/UXxC2F4rVx")
    print("\n[1] Start your RPC status")
    print("[2] Edit your RPC status")
    editorstart = input("[?]: ")

    if editorstart == '1':
        pass
    if editorstart =='2':
        clientid = input("\n[1] Enter your application's client ID >>> ")
        rpcstatus = input("[2] Enter your RPC status >>> ")
        rpcdetails = input("[3] Enter your RPC details >>> ")

        largeiconpic = input("[3] Enter your application's large icon's picture name >>> ")
        largeicontext = input("[4] Enter your application's large icon's name >>> ")
        smalliconpic = input("[5] Enter your application's small icon's picture name >>> ")

        with open('data/clientid.data', 'w') as f:
            f.writelines(clientid)
            f.close()
        with open('data/rpcstatus.data', 'w') as f:
            f.writelines(rpcstatus)
            f.close()
        with open('data/rpcdetails.data', 'w') as f:
            f.writelines(rpcdetails)
            f.close()
        with open('data/largeiconpic.data', 'w') as f:
            f.writelines(largeiconpic)
            f.close()
        with open('data/largeicontext.data', 'w') as f:
            f.writelines(largeicontext)
            f.close()
        with open('data/smalliconpic.data', 'w') as f:
            f.writelines(smalliconpic)
            f.close()

clientid_info = open('data/clientid.data')
clientid = clientid_info.read()

rpcstatus_info = open('data/rpcstatus.data')
rpcstatus = rpcstatus_info.read()

rpcdetails_info = open('data/rpcdetails.data')
rpcdetails = rpcdetails_info.read()

largeiconpic_info = open('data/largeiconpic.data')
largeiconpic = largeiconpic_info.read()

largeicontext_info = open('data/largeicontext.data')
largeicontext = largeicontext_info.read()

smalliconpic_info = open('data/smalliconpic.data')
smalliconpic = smalliconpic_info.read()

RPC = Presence(clientid)
RPC.connect()

RPC.update(state=rpcstatus, details=rpcdetails, large_image=largeiconpic, small_image=smalliconpic, large_text=largeicontext, start=time.time())
print("[*] RPC is running! Check out your Discord profile!")
