# Sentinel-Honeypot
<h1> Azure Sentinel w/ Honeypot and Map of Cyber Attacks </h1>

<h2>Breakdown</h2>
<b>This project allowed me to gain practical knowledge of the cloud computing platform and Sentinel! In this project, 
we use Azure Sentinel and link the SIEM to a virtual machine that we'll also set up. A cool thing about Sentinel:
it allows for advanced protection, you can fine tune it to your own organization's needs, and there's advanced...unprotection.
We'll be adding our own inbound rule. The only rule: allow any and all traffic to come in contact in the vm. That's right! This
virtual machine will act as a honeypot. </b>
<br />
<br />

<p align="center">
<img src = "https://github.com/calmatt02/Sentinel-Honeypot/assets/72759045/866f5dc0-3fce-45c7-a11f-7e04ecb3ae04"
height = "85%" width="85%"/>
</p>
<h2> Languages Used</h2>

- <b>PowerShell:</b> We'll be extracting failed logon attempts from Windows Event Viewer, and tracking those attempts with a script that runs on loop.

- <b>Python:</b> We'll want to use the log data from one of our files to come up with a map with heat signatures from countries trying to access our VM. I know Sentinel has the option to create a map using a custom log entry, but if there's a chance to use Python, I'm taking it.

<h2>Utilities</h2>

- <b>ipgeolocation.io:</b> Cool API that let's us convert the IP address into a physical location.

<p align="center">
<img src = "https://github.com/calmatt02/Sentinel-Honeypot/assets/72759045/ce931250-a206-4f08-bca0-747c4daf4f0f"
height = "85%" width="85%"/>
</p>

<h2>Running the script</h2>

- <b>PowerShell ISE:</b> You can see the two failed attempts in purple! (It was me). The main idea is that, with the help of the ipgeolocation API, we can use the script to extract the ip and add in the funcitonality to to get the longitude and latitude which will come up with the ip addresse's owner's country. We even use the PowerShell script to parse this information, coming up with our own custom log file in the process. Credits to Josh Madakor for this script.

<p align="center">
<img src = "https://github.com/calmatt02/Sentinel-Honeypot/assets/72759045/a5d67a72-77a2-4d67-9886-7fe87478daab"
height = "85%" width="85%"/>
</p>


