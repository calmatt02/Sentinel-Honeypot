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

<h2>Zero Protection</h2>

- <b>In the VM:</b> Now it's time to turn off the firewalls inside the VM. You can see that right now, when I ping the VM, nothing's really happening. Let's change that.

<p align="center">
<img src = "https://github.com/calmatt02/Sentinel-Honeypot/assets/72759045/385043af-45be-46b6-a3a7-8987dddc5353"
height = "60%" width="60%"/>
</p>

- <b> Letting the guards down!</b>

<p align="center">
<img src = "https://github.com/calmatt02/Sentinel-Honeypot/assets/72759045/200f4269-264d-4161-adf7-96f062345a5d"
height = "60%" width="60%"/>
</p>

- <b> Now we can successfully ping the VM!</b>

<p align="center">
<img src = "https://github.com/calmatt02/Sentinel-Honeypot/assets/72759045/d24f221b-2920-45a1-8f74-8878be0bdfe7"
height = "60%" width="60%"/>
</p>

<h2>Map of Cyber Attacks</h2>

- <b>Made this map with Python and folium library. If you'd like the full interactive map, I've uploaded the full html file.
You can even see the little black splotches near South Korea and Bulgaria. That's because the VM was bombarded with login requests from those two countries. So much so that I've exceeded my limit of free ip address tracking from ipgeolocation. Sadly, after about 12 hours of letting the VM run, the API token rejected any more entries, and so the log formatting broke.</b>

<p align="center">
<img src = "https://github.com/calmatt02/Sentinel-Honeypot/assets/72759045/e7e07712-e0c3-4c77-aadf-b40ac6d23a44"
height = "85%" width="85%"/>
</p>


