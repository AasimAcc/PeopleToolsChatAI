||**IP** |**Host Name**|**PI Home**|
| :- | :- | :- | :- |
|PUM Server|10\.10.1.56|Usny01OPUM001|<p>CS (10.10.1.57) – N:</p><p>FS (10.10.1.59) – P:</p>|
|CS – CA Server|10\.10.13.47|MCC04W32I001|<p>Image 1 - E:\psoft\CS92\_pi\_home</p><p>Image 2 - E:\psoft\pi\_home\_cs920.002</p>|
|FS – CA Server|10\.10.13.66|MCC04W32I002|E:\psoft\pi\_home\|


1. Download the Image file from My Oracle Support to the PUM server (10.10.1.56)

`                   `![](Aspose.Words.1c8c89c1-0e2b-4143-9c2a-89b3dc28d0b5.001.png)

`                    `![](Aspose.Words.1c8c89c1-0e2b-4143-9c2a-89b3dc28d0b5.002.png)

`                    `![](Aspose.Words.1c8c89c1-0e2b-4143-9c2a-89b3dc28d0b5.003.png)

`                   `![](Aspose.Words.1c8c89c1-0e2b-4143-9c2a-89b3dc28d0b5.004.png)

`                `![](Aspose.Words.1c8c89c1-0e2b-4143-9c2a-89b3dc28d0b5.005.png)

1. Select Download All option and download the files to c:\temp\<download folder>, i.e., e:\temp\cs9.20.002 folder.

`               `![](Aspose.Words.1c8c89c1-0e2b-4143-9c2a-89b3dc28d0b5.006.png)

`              `![](Aspose.Words.1c8c89c1-0e2b-4143-9c2a-89b3dc28d0b5.007.png)


`              `![](Aspose.Words.1c8c89c1-0e2b-4143-9c2a-89b3dc28d0b5.008.png)

1. Unzip the first zip file CS-920-UPD-002-OVA\_1of15.zip file in the <download folder>

`               `![](Aspose.Words.1c8c89c1-0e2b-4143-9c2a-89b3dc28d0b5.009.png)

1. Open PowerShell, and navigate to E:\temp\CS9.20.002\setup. In case you do not have permissions to run PowerShell scripts, run the following command: ***Set-executionpolicy remotesigned***

`                `![](Aspose.Words.1c8c89c1-0e2b-4143-9c2a-89b3dc28d0b5.010.png)

|<p>Windows PowerShell</p><p>Copyright (C) 2013 Microsoft Corporation. All rights reserved.</p><p></p><p>PS C:\Users\Administrator> **e:**</p><p>PS E:\> **cd temp\cs9.20.002\setup**</p><p>PS E:\temp\cs9.20.002\setup> **dir**</p><p></p><p></p><p>`    `Directory: E:\temp\cs9.20.002\setup</p><p></p><p></p><p>Mode                LastWriteTime     Length Name</p><p>----                -------------     ------ ----</p><p>d----          5/3/2016  10:24 AM            puppet</p><p>d----         7/27/2016  12:28 PM            scripts</p><p>-----         5/20/2016   7:11 PM         47 bs-manifest</p><p>-----         5/20/2016   7:11 PM      31759 psft-dpk-setup.ps1</p><p>-----         5/20/2016   7:11 PM      24169 psft-dpk-setup.sh</p><p></p><p></p><p>PS E:\temp\cs9.20.002\setup> **.\psft-dpk-setup.ps1**</p><p></p><p>Starting the PeopleSoft Environment Setup Process:</p><p></p><p>Extracting the Zip File CS-920-UPD-002-OVA\_10of15.zip:      [  OK  ]</p><p>Extracting the Zip File CS-920-UPD-002-OVA\_11of15.zip:      [  OK  ]</p><p>Extracting the Zip File CS-920-UPD-002-OVA\_12of15.zip:      [  OK  ]</p><p>Extracting the Zip File CS-920-UPD-002-OVA\_13of15.zip:      [  OK  ]</p><p>Extracting the Zip File CS-920-UPD-002-OVA\_14of15.zip:      [  OK  ]</p><p>Extracting the Zip File CS-920-UPD-002-OVA\_15of15.zip:      [  OK  ]</p><p>Extracting the Zip File CS-920-UPD-002-OVA\_1of15.zip:       [  OK  ]</p><p>Extracting the Zip File CS-920-UPD-002-OVA\_2of15.zip:       [  OK  ]</p><p>Extracting the Zip File CS-920-UPD-002-OVA\_3of15.zip:       [  OK  ]</p><p>Extracting the Zip File CS-920-UPD-002-OVA\_4of15.zip:       [  OK  ]</p><p>Extracting the Zip File CS-920-UPD-002-OVA\_5of15.zip:       [  OK  ]</p><p>Extracting the Zip File CS-920-UPD-002-OVA\_6of15.zip:       [  OK  ]</p><p>Extracting the Zip File CS-920-UPD-002-OVA\_7of15.zip:       [  OK  ]</p><p>Extracting the Zip File CS-920-UPD-002-OVA\_8of15.zip:       [  OK  ]</p><p>Extracting the Zip File CS-920-UPD-002-OVA\_9of15.zip:       [  OK  ]</p><p></p><p>Found PeopleSoft SES VMDK TGZ file parts in the DPK folder</p><p>E:\temp\cs9.20.002. If the VM is set up as a PeopleSoft Demo,</p><p>environment, we can automate the process of adding it to the VM.</p><p></p><p>Do you want to add the SES VMDK Disk to the VM? [Y|n]: **n**</p><p></p><p>Setting up the PeopleSoft Environment in VirtualBox:</p><p></p><p>Checking if VirtualBox Software is Installed on the Host:   [  OK  ]</p><p>Checking if VirtualBox Machine Folder has Enough Space:     [  OK  ]</p><p>Checking if VirtualBox Manager is Running on the Host:      [  OK  ]</p><p>Checking if PeopleSoft Appliance is Available to Import:    [  OK  ]</p><p></p><p>Found a PeopleSoft VirtualBox Appliance [VBOX\_8\_55\_06\_SHELL.ova]</p><p>in the DPK folder E:\temp\cs9.20.002. We can automate the process of</p><p>importing this appliance into VirtualBox if VirtualBox software is installed</p><p>on the Host.</p><p></p><p>Do you want to Import the PeopleSoft Appliance into VirtualBox? [Y|n]: **Y**</p><p></p><p>Checking if the PeopleSoft Appliance is already Imported:   [  OK  ]</p><p>Importing the PeopleSoft Appliance into VirtualBox:         [  OK  ]</p><p></p><p>The Network Adapter lets the VM be available either in a Sand-Box</p><p>mode or accessible to other hosts in the network.</p><p></p><p>1\. Host-Only Network Adapter</p><p>2\. Bridged Network Adapter</p><p>Enter 1 or 2: **2**</p><p></p><p>Setting up Bridged Network Adapter for the VM:              [  OK  ]</p><p>Setting up the Shared Folder E:\temp\cs9.20.002 on the VM:  [  OK  ]</p><p></p><p>Starting the VirtualBox Manager on the Host:                [  OK  ]</p><p>Starting the Imported PeopleSoft Appliance VM:              [  OK  ]</p><p></p><p>**The VirtualBox portion of the PeopleSoft environment setup is complete.**</p><p>**Access the auto launched VM to continue with the PeopleSoft environment**</p><p>**initialization process.**</p><p></p><p>PS E:\temp\cs9.20.002\setup></p>|
| :- |

1. Virtual Box will automatically launch VM to continue with the PeopleSoft environment setup… 

`                `![](Aspose.Words.1c8c89c1-0e2b-4143-9c2a-89b3dc28d0b5.011.png)


`                  `![](Aspose.Words.1c8c89c1-0e2b-4143-9c2a-89b3dc28d0b5.012.png)

`                     `![](Aspose.Words.1c8c89c1-0e2b-4143-9c2a-89b3dc28d0b5.013.png)

`                     `![](Aspose.Words.1c8c89c1-0e2b-4143-9c2a-89b3dc28d0b5.014.png)

`                   `![](Aspose.Words.1c8c89c1-0e2b-4143-9c2a-89b3dc28d0b5.015.png)

`                    `![](Aspose.Words.1c8c89c1-0e2b-4143-9c2a-89b3dc28d0b5.016.png)

`                    `![](Aspose.Words.1c8c89c1-0e2b-4143-9c2a-89b3dc28d0b5.017.png)



`                   `![](Aspose.Words.1c8c89c1-0e2b-4143-9c2a-89b3dc28d0b5.018.png)

- Gateway

  |<p>[root@hitscs92updi ~]# route -n</p><p>Kernel IP routing table</p><p>Destination     Gateway         Genmask         Flags Metric Ref    Use Iface</p><p>0\.0.0.0         **10.10.1.1**       0.0.0.0         UG    0      0        0 eth0</p><p>10\.10.1.0       0.0.0.0         255.255.255.0   U     0      0        0 eth0</p><p></p>|
  | :- |

- DNS Server

  |<p>[root@hitscs92updi ~]# cat /etc/resolv.conf</p><p>;generated by /opt/oracle/psft/dpk/scripts/psft-setup.sh</p><p>**nameserver 10.10.1.50**</p><p>search hitscs.local</p><p>[root@hitscs92updi ~]# grep nameserver /etc/resolv.conf</p><p>**nameserver 10.10.1.50**</p><p>[root@hitscs92updi ~]#</p>|
  | :- |


1. The screenshot below shows when the image is successfully created.      

`               `![](Aspose.Words.1c8c89c1-0e2b-4143-9c2a-89b3dc28d0b5.019.png)


1. Open putty and connect to the new Image.      

`                `![](Aspose.Words.1c8c89c1-0e2b-4143-9c2a-89b3dc28d0b5.020.png)

`               `**CS – 10.10.1.57**

`               `**FS – 10.10.1.59**

`               `**HC – 10.10.1.61**

`                  `![](Aspose.Words.1c8c89c1-0e2b-4143-9c2a-89b3dc28d0b5.021.png)


`                  `![](Aspose.Words.1c8c89c1-0e2b-4143-9c2a-89b3dc28d0b5.022.png)

1. Run the following commands to start the EMAgent.

   |<p>Use the root account to connect to 10.10.1.57 or 10.10.1.59</p><p>**cd /opt/oracle/psft/pt/ps\_home8.55.06/PSEMAgent**</p><p>**chmod 777 -R envmetadata**</p><p>**su – psadm2**</p><p>**cd $PS\_HOME**</p><p>**cd PSEMA\*** </p><p>**./StartAgent.sh**</p>|
   | :- |

1. Log in to your CA server, and verify connection to this new image. Go to Tools -> Options

`             `![](Aspose.Words.1c8c89c1-0e2b-4143-9c2a-89b3dc28d0b5.023.png) ![](Aspose.Words.1c8c89c1-0e2b-4143-9c2a-89b3dc28d0b5.024.png)

`            `![](Aspose.Words.1c8c89c1-0e2b-4143-9c2a-89b3dc28d0b5.025.png) ![](Aspose.Words.1c8c89c1-0e2b-4143-9c2a-89b3dc28d0b5.026.png)








1. Test Database connection. Go to File -> Open Database -> select **XX92UPDI**

   `  `![](Aspose.Words.1c8c89c1-0e2b-4143-9c2a-89b3dc28d0b5.027.png)

  














   Review configuration and correct any errors you may find. Click Next

`                    `/![](Aspose.Words.1c8c89c1-0e2b-4143-9c2a-89b3dc28d0b5.028.png)

`                      `Click Next

`                      `![](Aspose.Words.1c8c89c1-0e2b-4143-9c2a-89b3dc28d0b5.029.png)

`                     `Click Finish

`                     `![](Aspose.Words.1c8c89c1-0e2b-4143-9c2a-89b3dc28d0b5.030.png)







