# **Raspi SSH Setup Guide for hw@scm**  

### **Purpose**  
This guide helps you quickly set up SSH access from a fresh laptop to your Raspberry Pi (`hw@scm`). It ensures secure, passwordless login and an easy way to connect ideally without remembering IP addresses.  

---

## **1. Generate an SSH Key (On Your Laptop)**  
If you haven’t already, generate an SSH key:  
```bash
ssh-keygen -t rsa -b 4096
```
- Press **Enter** to accept the default location (`~/.ssh/id_rsa`).  
- Optionally, set a **passphrase** (or leave it empty for easier login).  

---

## **2. Copy Your SSH Key to the Raspberry Pi**  
Run the following command to copy your key to `hw@scm` (or its IP `192.168.1.8`):  
```bash
ssh-copy-id hw@192.168.1.8
```
This allows **passwordless SSH login**.

---

## **3. Test SSH Connection**  
Now, try connecting:  
```bash
ssh hw@192.168.1.8
```

---

## **4. (Optional) Set an SSH Alias**  
Since `scm` doesn’t always have the same IP, you can create an alias for easier access.  

Edit your SSH config file:  
```bash
nano ~/.ssh/config
```
Add the following:  
```
Host scm
    HostName 192.168.1.8
    User hw
    IdentityFile ~/.ssh/id_rsa
```
Save and exit (`CTRL + X`, then `Y`, then `Enter`).  

Now, you can SSH with just:  
```bash
ssh scm
```