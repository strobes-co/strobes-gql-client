# How to Connect Strobes GraphQL Client to Strobes Platform

## What You Need to Know

This guide will help you connect the Strobes GraphQL Client to your Strobes platform. Think of this like setting up a secure connection between two systems so they can talk to each other.

## 📋 Prerequisites - What You Need Before Starting

**Before you can use the Strobes GraphQL Client, you need to have these things installed on your computer:**

### 1. Python Installation
**You need Python installed on your computer.**

**To check if Python is installed:**
1. **Open Command Prompt** (Windows) or **Terminal** (Mac/Linux)
2. **Type this command and press Enter:**
   ```bash
   python3 --version
   ```
3. **If you see a version number** (like "Python 3.9.0"), you're good to go!
4. **If you get an error**, you need to install Python

**To install Python:**
- **Windows:** Go to [python.org](https://python.org) and download the latest version
- **Mac:** Python usually comes pre-installed, or use Homebrew: `brew install python3`
- **Linux:** Use your package manager: `sudo apt install python3` (Ubuntu/Debian)

### 2. Install Required Packages
**After Python is installed, you need to install the required software packages.**

1. **Open Command Prompt or Terminal**
2. **Navigate to the Strobes GraphQL Client folder** (where you see the `requirements.txt` file)
3. **Install the requirements by typing:**
   ```bash
   pip3 install -r requirements.txt
   ```
4. **Wait for the installation to complete** (this might take a few minutes)

**What this does:** This installs all the necessary software that the Strobes GraphQL Client needs to work properly.

### 3. Virtual Environment (Recommended)
**It's recommended to use a virtual environment to keep things organized.**

1. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   ```

2. **Activate the virtual environment:**
   ```bash
   # On Windows:
   venv\Scripts\activate
   
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. **Install requirements in the virtual environment:**
   ```bash
   pip install -r requirements.txt
   ```

**You'll know it's working when you see `(venv)` at the beginning of your command line.**

---

**Once you have Python installed and the requirements set up, you can continue with the steps below!**

## Step 1: Get Your Connection Information

Before you can connect, you need to collect some information from your Strobes platform. Think of this like getting the address and key to a building:

**You'll need these 5 pieces of information:**
- **Host**: This is like the address of your Strobes platform (e.g., "strobes.company.com" or "192.168.1.100")
- **API Token**: This is like a special password that lets the client access your platform
- **Scheme**: This tells the system whether to use "http" or "https" (https is more secure)
- **Port**: This is like a specific door number (usually 80 for http, 443 for https)
- **Organization ID**: This is your company's unique identifier in the system

## Step 2: Get Your API Token and Organization ID

**This is like getting your special access card and company ID number.**

Follow these steps carefully:

1. **Open your web browser** and go to your Strobes platform website
2. **Log in** with your username and password
3. **Look for the Settings menu** (usually in the top-right corner or main menu)
4. **Click on "Settings"** and then look for **"API Access"**
5. **Click "Generate Token"** - this creates your special access password
6. **Copy the token** that appears (it will look like a long string of letters and numbers)
7. **Write down your Organization ID** - this should also be visible on the same page

**Important:** Keep this token safe! It's like your password to the system.

## Step 3: Set Up the Configuration File

**This is like filling out a form with your connection details.**

1. **Open File Explorer** (Windows) or **Finder** (Mac) and navigate to the Strobes GraphQL Client folder
2. **Go to this folder:** `examples/gql-client/`
3. **Find the file called `config.py`** and open it with any text editor (like Notepad, TextEdit, or VS Code)
4. **Replace the information** in the file with your details:

   Look for these lines and change them:
   ```python
   HOST = "your-strobes-host.com"        # Change this to your actual host
   API_TOKEN = "your-api-token-here"     # Change this to your actual token
   SCHEME = "https"                      # Usually "https" (more secure) or "http"
   PORT = 443                            # Usually 443 for https, 80 for http
   ORGANIZATION_ID = "your-org-id-here"  # Change this to your actual organization ID
   ```

**Example of what it should look like:**
```python
HOST = "strobes.mycompany.com"
API_TOKEN = "abc123def456ghi789jkl012mno345pqr678stu901vwx234yz"
SCHEME = "https"
PORT = 443
ORGANIZATION_ID = "3c5d440c-2b62-4446-bf99-24c492d6a0f5"
```

**Save the file** after making these changes!

## Step 4: Test Your Connection

**This is like testing if your key works before trying to open the door.**

1. **Open Command Prompt** (Windows) or **Terminal** (Mac/Linux)
2. **Navigate to the folder:** `examples/gql-client/`
3. **Type this command and press Enter:**
   ```bash
   python3 test_connectivity.py
   ```

**What you should see:**
- If it works: You'll see a success message saying the connection is working
- If it doesn't work: You'll see an error message - this means you need to check your configuration

**If you get an error, check:**
- Did you save the config.py file?
- Are all the details correct (host, token, organization ID)?
- Is your Strobes platform running and accessible?

## Step 5: What You Can Do Now

**Great! Once your connection is working, you can use these tools:**

### 📁 Asset Management (Creating and Managing Assets)
- **Create Web Assets**: Make new web applications, websites, or APIs in the system
- **Create Network Assets**: Add servers, computers, or network devices
- **Create Code Assets**: Add software code or applications
- **View All Assets**: See a list of all your assets and get reports

### 🐛 Bug Management (Creating and Managing Security Issues)
- **Create Web Bugs**: Report security problems found in websites or web applications
- **Create Network Bugs**: Report security issues found in network devices or servers
- **Create Code Bugs**: Report security problems found in software code
- **View All Bugs**: See a list of all security issues and get reports

### 🔧 Testing Tools
- **Test Configuration**: Make sure your settings are correct
- **Test Connection**: Check if you can connect to the platform

**Think of it like this:**
- **Assets** = Things you want to protect (websites, servers, software)
- **Bugs** = Security problems you've found that need to be fixed

## How to Use the Tools

**Here are some common things you might want to do:**

### 🔍 Test Your Connection
```bash
python3 test_connectivity.py
```
*This checks if everything is set up correctly*

### 📁 Create New Assets
```bash
# Create web assets (websites, web apps)
cd asset-creation/
python3 create_web_asset_no_duplicates.py

# Create network assets (servers, devices)
python3 create_network_asset_no_duplicates.py

# Create code assets (software, applications)
python3 create_code_asset_no_duplicates.py
```

### 📊 View Your Assets
```bash
cd ../asset-fetching/
python3 fetch_all_assets.py
```
*This shows you a list of all your assets*

### 🐛 Create Bug Reports
```bash
cd ../bug-creation/
python3 create_web_bugs.py      # For website security issues
python3 create_network_bugs.py  # For network security issues
python3 create_code_bugs.py     # For software security issues
```

### 📋 View Bug Reports
```bash
cd ../bug-fetching/
python3 fetch_all_bugs.py
```
*This shows you a list of all security issues*

**Remember:** Always start in the `examples/gql-client/` folder when running these commands!

## 🔒 Security Tips

**Keep your information safe!**

- **Keep your API token secret** - don't share it with anyone or put it in public places
- **Use HTTPS** when possible - this makes your connection more secure
- **Change your API token regularly** - like changing your password
- **Keep the config.py file secure** - make sure only you can access it
- **Don't share your configuration file** - it contains sensitive information

**Think of your API token like your password - keep it safe!**

## 🆘 Troubleshooting - Common Problems and Solutions

**If something doesn't work, try these solutions:**

### ❌ Connection Errors
**Problem:** Can't connect to the Strobes platform
**Solution:** 
- Check if your host address is correct
- Make sure your Strobes platform is running
- Try using "https" instead of "http"

### 🔐 Authentication Errors  
**Problem:** "Invalid token" or "Access denied" messages
**Solution:**
- Check if your API token is correct (copy it exactly)
- Make sure your token hasn't expired
- Generate a new token if needed

### 🏢 Organization Errors
**Problem:** "Organization not found" messages
**Solution:**
- Check if your Organization ID is correct
- Make sure you copied the entire ID (it's usually a long string)

### 📁 Import Errors
**Problem:** "File not found" or "Module not found" messages
**Solution:**
- Make sure you're in the right folder (`examples/gql-client/`)
- Check if you have Python installed
- Make sure you've activated the virtual environment
- Try installing requirements again: `pip install -r requirements.txt`

### 🐍 Python Not Found
**Problem:** "python3: command not found" or "python is not recognized"
**Solution:**
- Install Python from [python.org](https://python.org)
- Make sure Python is added to your system PATH
- Try using `python` instead of `python3` on some systems

### 📦 Package Installation Errors
**Problem:** "No module named 'sgqlc'" or similar import errors
**Solution:**
- Make sure you've installed the requirements: `pip install -r requirements.txt`
- Try upgrading pip: `pip install --upgrade pip`
- Check if you're in the virtual environment (should see `(venv)` in command line)

### 💡 Still Having Problems?
- Double-check all the information in your `config.py` file
- Make sure you saved the file after making changes
- Try the connection test again: `python3 test_connectivity.py`



---

## 🎉 You're All Set!

**Congratulations! You now know how to:**
- ✅ Connect to your Strobes platform
- ✅ Create and manage assets
- ✅ Create and manage security bug reports
- ✅ View reports and analyze data
- ✅ Troubleshoot common problems

**If you need help, refer back to this guide or contact your technical support team.** 