<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Project Setup Instructions</h1>
<h2>1. Create a Virtual Environment</h2>
    
<p>Create a virtual environment using Python 3.12:</p>
    <pre><code>python3.12 -m venv venv</code></pre>

<h2>2. Activate the Virtual Environment</h2>
    <p>Activate the virtual environment:</p>
    <p><strong>On Windows:</strong></p>
    <pre><code>venv\Scripts\activate</code></pre>

<p><strong>On macOS/Linux:</strong></p>
    <pre><code>source venv/bin/activate</code></pre>

<h2>3. Install Required Packages</h2>
    <p>Install all required dependencies:</p>
    <pre><code>pip install -r requirements.txt</code></pre>

<h2>4. Set Up the .env File</h2>
    <p>Ensure your <code>.env</code> file contains the following API keys:</p>
    <ul>
        <li><strong>PHIDATA_API_KEY</strong> (for Phidata services)</li>
        <li><strong>GROQ_API_KEY</strong> (for Groq services)</li>
    </ul>
    <p>Example <code>.env</code> file:</p>
    <pre><code>PHIDATA_API_KEY=your_phidata_api_key_here 
    
GROQ_API_KEY=your_groq_api_key_here</code></pre>

<h2>5. Run the Agent</h2>
    <p>After setting up the virtual environment and installing the dependencies, execute the <code>financial_agent.py</code> file to run the agent:</p>
    <pre><code>python financial_agent.py</code></pre>

</body>
</html>
