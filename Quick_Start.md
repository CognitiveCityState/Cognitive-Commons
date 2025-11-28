Quick Start: Operational Guide for the Strategic Cognition Dual-Mode Engine

1. Environment Preparation

Python Version Requirement: Python 3.8+ (3.9/3.10 recommended)
System Compatibility: Windows/macOS/Linux all supported

2. Install Dependencies

Create and install project dependencies (virtual environment recommended):

1. Create a requirements.txt file in the project root directory with the following content:
dashscope>=1.14.0  
python-dotenv>=1.0.0  # Optional, for managing keys via .env files  
2. Execute the installation command:
pip install -r requirements.txt  
3. Configure API Key

The code calls Alibaba Cloud Tongyi Qianwen (Qwen) API, requiring configuration of DASHSCOPE_API_KEY:

3.1 Obtain API Key

• Visit the Alibaba Cloud Tongyi Console, register/login to your account

• Navigate to the "API-KEY Management" page, create and copy your API key (DASHSCOPE_API_KEY)

3.2 Set Environment Variables

Linux/macOS (Terminal):
export DASHSCOPE_API_KEY="your_api_key"  
#Optional: Make permanent (add to ~/.bashrc or ~/.zshrc)  
echo 'export DASHSCOPE_API_KEY="your_api_key"' >> ~/.bashrc && source ~/.bashrc  
Windows (PowerShell):
$env:DASHSCOPE_API_KEY="your_api_key"  
#Optional: Make permanent (add via System Properties → Environment Variables)  
Optional: Use .env File
Create a .env file in the project root directory (add to .gitignore):
DASHSCOPE_API_KEY=your_api_key  
Add loading logic at the start of your code:
from dotenv import load_dotenv  
load_dotenv()  # Load .env file  
4. Run the Code

Save the core code as main.py (or any name)
Execute the command:
python main.py  
5. Output Explanation

After running, the system will automatically execute:

• Phase 1: Strategic Extraction: Analyze the decision logic of Buffett's investment cases and extract strategic frameworks

• Phase 2: Strategic Implantation: Analyze AI healthcare tech stock investment opportunities based on the extracted framework

Final output: A complete strategic cognition report (including confidence classification, framework insights, etc.)

6. Notes

• Key Security: Never commit API keys to code repositories (.gitignore should include .env, key files, etc.)

• API Costs: Tongyi Qianwen API is billed by usage; monitor usage/costs in the Alibaba Cloud Console

• Network Requirements: Ensure network access to Alibaba Cloud API endpoints (https://dashscope.aliyuncs.com)

• Performance Optimization: Large model calls may take time; adjust the temperature parameter or model version (currently using qwen-plus) as needed

Common Issues

• API Call Failure: Check key validity, network connectivity, or Alibaba Cloud account balance

• Dependency Installation Errors: Upgrade pip and retry (pip install --upgrade pip)

• Abnormal Output Format: Confirm model responses match expected formats, or adjust prompt templates
